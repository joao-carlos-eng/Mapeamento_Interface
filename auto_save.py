# auto_save.py
import os
import json


class AutoSave:
    def __init__(self, directory="autosaves"):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _get_log_path(self, file_path):
        base_name = os.path.basename(file_path)
        return os.path.join(self.directory, base_name + '.log')

    def save_state(self, file_path, state):
        log_path = self._get_log_path(file_path)
        with open(log_path, 'w') as log_file:
            json.dump(state, log_file)

    def load_state(self, file_path):
        log_path = self._get_log_path(file_path)
        if os.path.exists(log_path):
            with open(log_path, 'r') as log_file:
                return json.load(log_file)
        return None

    def remove_state(self, file_path):
        log_path = self._get_log_path(file_path)
        if os.path.exists(log_path):
            os.remove(log_path)
