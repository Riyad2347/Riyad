import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

name_node = 'turtlesim_linear'

class LINEARController:
    def __init__(self, ref=3, spd=1)
    self.ref = ref
    self.spd =spd
     