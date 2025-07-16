import time

class FPSCounter:
    def __init__(self):
        self.start_time = None
        self.frame_count = 0
        self.fps = 0

    def start(self):
        self.start_time = time.time()
        self.frame_count = 0

    def update(self):
        self.frame_count += 1

    def stop(self):
        if self.start_time is None:
            return 0
        elapsed = time.time() - self.start_time
        if elapsed > 0:
            self.fps = self.frame_count / elapsed
        else:
            self.fps = 0
        return round(self.fps, 2)

    def get_fps(self):
        return round(self.fps, 2)
