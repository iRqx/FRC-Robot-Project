# main.py

from swerve_drive import SwerveDrive

def main():
    swerve_drive = SwerveDrive()

    # Example: drive forward
    swerve_drive.drive(1, 'forward')

if __name__ == "__main__":
    main()
