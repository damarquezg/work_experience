from robot_control_class import RobotControl

robotcontrol = RobotControl()

a = robotcontrol.get_laser(0)

while a > 1:
    robotcontrol.move_straight()
    a = robotcontrol.get_laser(0)
    print ("Current distance to wall: %f" % a)

robotcontrol.stop_robot()

print ("Wall is at %f metres! Stop the robot!" % a)