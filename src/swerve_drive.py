from Adafruit_BBIO.PWM import start, set_duty_cycle, stop
import time

class SwerveDrive:
    def __init__(self, motor_pins, encoder_pins, gyro):
        self.motor_pins = motor_pins
        self.encoder_pins = encoder_pins
        self.gyro = gyro
        for pin in motor_pins:
            start(pin, 0)  # Initialize PWM pins

    def set_speed(self, speeds):
        for pin, speed in zip(self.motor_pins, speeds):
            duty_cycle = ((speed + 1) / 2) * 100  # Convert speed (-1 to 1) to duty cycle (0 to 100)
            set_duty_cycle(pin, duty_cycle)

    def stop(self):
        for pin in self.motor_pins:
            stop(pin)

    def read_sensors(self): 
        encoder_values = [self.read_encoder(pin) for pin in self.encoder_pins]
        gyro_value = self.read_gyro()
        return encoder_values, gyro_value

    def read_encoder(self, pin):
        # Hypothetical function to read encoder value from the pin
        # Replace with actual implementation
        return 0  # Placeholder value

    def read_gyro(self):
        # Hypothetical function to read gyro value
        # Replace with actual implementation
        return self.gyro.read()  # Example method call on a gyro object

# Example usage
if __name__ == "__main__":
    motor_pins = ["P9_14", "P9_16"]  # Example motor pins
    encoder_pins = ["P8_12", "P8_14"]  # Example encoder pins
    gyro = Gyro()  # Hypothetical gyro object

    swerve_drive = SwerveDrive(motor_pins, encoder_pins, gyro)
    swerve_drive.set_speed([0.5, 0.5])  # Set speed for motors

    time.sleep(2)  # Run motors for 2 seconds

    swerve_drive.stop()  # Stop motors

    encoders, gyro_value = swerve_drive.read_sensors()
    print("Encoder values:", encoders)
    print("Gyro value:", gyro_value)
