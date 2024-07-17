from Adafruit_BBIO.PWM import start, set_duty_cycle, stop

class SparkMaxPWMController:
    def __init__(self, pwm_pin):
        self.pwm_pin = pwm_pin
        start(self.pwm_pin, 0)

    def set_speed(self, speed):
        # Convert speed (-1 to 1) to duty cycle (0 to 100)
        duty_cycle = ((speed + 1) / 2) * 100
        set_duty_cycle(self.pwm_pin, duty_cycle)

    def stop(self):
        stop(self.pwm_pin)

# Example usage
if __name__ == "__main__":
    motor = SparkMaxPWMController("P9_14")  # Use the appropriate pin for your setup

    # Set motor speed to 50% forward
    motor.set_speed(0.5)
    # Wait for a few seconds
    import time
    time.sleep(2)

    # Set motor speed to 50% reverse
    motor.set_speed(-0.5)
    time.sleep(2)

    # Stop the motor
    motor.stop()
