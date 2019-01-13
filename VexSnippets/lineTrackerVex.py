import vex
import sys

#region config
bump_        = vex.DigitalInput(5)
limit        = vex.DigitalInput(8)
right_sensor = vex.LineTracker(1)
left_sensor  = vex.LineTracker(2)
right_motor  = vex.Motor(2)
left_motor   = vex.Motor(3)
#endregion config

# main thread
sys.wait_for(bump_.is_on)
right_motor.run(20)
left_motor.run(20)
while True:
  if right_sensor.line_tracker_percent() > 70:
    right_motor.off()
  elif left_sensor.percent() > 70:
    left_motor.off()
  elif limit.is_on():
    break
  else:
    right_motor.run(20)
    left_motor.run(20)
while True:
  if bump_.is_on():
    break
  else:
    right_motor.off()
    left_motor.off()
    sys.sleep(3)
    right_motor.run(-(20))
    left_motor.run(-(20))
    sys.sleep(0.5)
    left_motor.run(-(25))
    right_motor.run(20)
    sys.sleep(3.5)
    right_motor.run(20)
    left_motor.run(20)
    while True:
      if right_sensor.line_tracker_percent() > 70:
        right_motor.off()
      elif left_sensor.percent() > 70:
        left_motor.off()
      elif limit.is_on():
        break
      elif bump_.is_on():
        break
      else:
        right_motor.run(20)
        left_motor.run(20)
left_motor.run(20)
right_motor.run(20)
while True:
  if right_sensor.line_tracker_percent() > 70:
    right_motor.off()
  elif left_sensor.percent() > 70:
    left_motor.off()
  elif limit.is_on():
    right_motor.off()
    left_motor.off()
    break
  else:
    right_motor.run(20)
    left_motor.run(20)

