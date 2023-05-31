import os
import time

import cv2
import face_recognition
import numpy as np

from src.python.configs import Config
from src.python.func_processor import FuncProcessor
from src.python.keyboard_simulator import Keyboard
from src.python.thread import TimerThread


class FaceReg:
    isCallable = True
    KEY_MAP_FLAGE = "keyMap"
    FUNC_MAP_FLAGE = "funcMap"

    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.keyboard = Keyboard()
        self.configuration = Config()
        self.func_processor = FuncProcessor()

        # create a thread for reduce key handler times
        self.timer = TimerThread(5.0, self.timer_callback)
        self.timer.start()

    def timer_callback(self):
        self.isCallable = True

    def start(self):
        self.face_reg()

    def face_reg(self, image_path="images"):
        # Load the known faces
        known_face_encodings, known_face_names = self.load_known_faces(image_path)

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        # Get a reference to webcam #0 (the default one)

        while True:

            # Grab a single frame of video
            ret, frame = self.video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding,
                                                             self.configuration.tolerance)
                    name = "Unknown"

                    if True in matches:
                        # If a match was found in known_face_encodings, use the first one
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]

                    face_names.append(name)

            process_this_frame = not process_this_frame
            if len(face_names) > 0:
                if self.isCallable:
                    # print(face_names)
                    self.face_processor(face_names)
            # Display the results if hasVideo is Ture
            if self.configuration.hasVideo:
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # Draw a box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

                # Display the resulting image
                cv2.resizeWindow('Video', self.configuration.window_width, self.configuration.window_height)
                cv2.imshow('Video', frame)

                # Hit 'q' on the keyboard to quit!
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                # Release handle to the webcam

            time.sleep(0.25)
        if self.configuration.hasVideo:
            self.video_capture.release()
        cv2.destroyAllWindows()

    # Function to load and encode all the known faces
    def load_known_faces(self, folder_path):
        global image_path, file_name
        known_face_encodings = []
        known_face_names = []

        # Iterate over all files in the folder
        for file_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, file_name)
            if not os.path.isfile(image_path):
                continue

        # Load the image file
        image = face_recognition.load_image_file(image_path)

        # Encode the face
        face_encoding = face_recognition.face_encodings(image)
        if len(face_encoding) > 0:
            known_face_encodings.append(face_encoding[0])
            # Use file name as the person's name
            known_face_names.append(os.path.splitext(file_name)[0])

        return known_face_encodings, known_face_names

    def face_processor(self, face_names: str):
        for i in face_names:
            if i.lower() in self.configuration.user_map:
                # Key map process
                if self.KEY_MAP_FLAGE in self.configuration.user_map[i.lower()]:
                    user_shortcuts_list = self.configuration.user_map[i.lower()][self.KEY_MAP_FLAGE]
                    if user_shortcuts_list is not None:
                        self.keyboard.send_keys_multiply(user_shortcuts_list)

                # Func map process
                if self.FUNC_MAP_FLAGE in self.configuration.user_map[i.lower()]:
                    user_process_list = self.configuration.user_map[i.lower()][self.FUNC_MAP_FLAGE]
                    if user_process_list is not None:
                        self.func_processor.minimize_window(user_process_list)

        self.isCallable = False
