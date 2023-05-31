import platform

import psutil


class FuncProcessor:
    def __init__(self):
        self.current_os = platform.system()

    def minimize_window(self, process_names):
        if self.current_os == 'Darwin':
            self.minimize_process_osx_by_name(process_names)
        else:
            self.minimize_processes(process_names)

    def minimize_processes(self, process_names):
        procs = psutil.process_iter(['pid', 'name'])
        for proc in procs:
            if proc.info['name'] in process_names:
                pid = proc.info['pid']

                if self.current_os == 'Windows':
                    import win32gui
                    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32gui.SW_MINIMIZE)
                elif self.current_os == 'Linux':
                    import subprocess
                    subprocess.run(['xdotool', 'windowminimize', str(pid)])

    def minimize_process_osx_by_name(self, process_name_list):
        import subprocess
        for i in process_name_list:
            subprocess.run(['osascript', '-e',
                            f'tell application "System Events" to click (first button of (every window of (application process "{i.lower()}")) whose role description is "minimize button")'])
