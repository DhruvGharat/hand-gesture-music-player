class GestureController:
    def __init__(self):
        self.prev_x = None  # stores previous wrist x-position

    def count_fingers(self, lm):
        fingertips = [8, 12, 16, 20]  # detectIndex, Middle, Ring, Pinky tips
        finger_count = 0

        for tip in fingertips:
            if lm[tip].y < lm[tip - 2].y:
                finger_count += 1

        return finger_count

    def detect_swipe(self, x):
        if self.prev_x is None:
            self.prev_x = x
            return None

        diff = x - self.prev_x
        self.prev_x = x

        # Lower threshold = more sensitive
        if diff > 0.03:
            return "RIGHT"
        elif diff < -0.03:
            return "LEFT"
        return None

