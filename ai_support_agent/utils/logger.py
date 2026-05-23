import datetime

class Logger:
    def __init__(self, log_path):
        self.log_path = log_path

    def log(self, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {message}\n")
            f.flush()  # Ensure data is written immediately
