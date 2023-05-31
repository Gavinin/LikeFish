import yaml


class Config:
    def __init__(self):
        self.timeout = 5.0
        self.tolerance = 0.4
        self.user_map: {} = {}
        self.window_width = 800
        self.window_height = 600
        self.hasVideo = True
        __yaml_file_name__ = "config.yaml"
        with open(__yaml_file_name__, 'rb') as f:
            config = yaml.safe_load(f)
            self.tolerance = 0.1 * config.get('tolerance', 4)
            self.user_map: {} = config.get('userMap', {})
            self.window_width = config['window']['width']
            self.window_height = config['window']['height']
            self.hasVideo = config['hasVideo'] == 'true'
