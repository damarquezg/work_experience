from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser(0)

print ("The distance measured is: ", a, " m.")
