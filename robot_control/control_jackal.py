from robot_control_class_jackal import RobotControl

robotcontrol = RobotControl()

robotcontrol.move_straight_time("forward", 0.3, 5)
robotcontrol.turn("clockwise", 0.3, 7)