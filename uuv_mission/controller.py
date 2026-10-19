class PDController:
    def __init__(self, kp: float, kd: float):
        # give the controller a proportional gain and a derivative gain
        self.kp = kp
        self.kd = kd
        self.prev_error = 0.0 # the initial error is zero

    def __call__(self, reference: float, measurement: float) -> float:
        error = reference - measurement
        output = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return output