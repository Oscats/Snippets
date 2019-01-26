...
def robotInit(self):
# In order to instatiate a four motor drivetrain, first, you need to set up left and right objects. 
    self.frontLeft = wpilib.Spark(1)
    self.rearLeft = wpilib.Spark(2)
    # Left drive
    self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

    self.frontRight = wpilib.Spark(3)
    self.rearRight = wpilib.Spark(4)
    # Right drive
    self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)
    
    #Then you combine them as a single drivetrain.
    self.drive = DifferentialDrive(self.left, self.right)
  ...
  ...
  def teleopPeriodic(self):
    ...
    # Then you invoke the arcade (or tank) drive to actually make the robot move.
    self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())
    ...
  
