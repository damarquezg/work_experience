from robot_control_class import RobotControl

robotcontrol = RobotControl()

def get_laser_values(a,b,c):
    r1 = robotcontrol.get_laser(a)
    r2 = robotcontrol.get_laser(b)
    r3 = robotcontrol.get_laser(c)

    return [r1, r2, r3]

l = get_laser_values(0, 150, 300)

print ("Reading 1: ", l[0])
print ("Reading 2: ", l[1])
print ("Reading 3: ", l[2])