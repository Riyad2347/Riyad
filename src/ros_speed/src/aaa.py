#!/usr/bin/env python
#from __future__ import print_function

import roslib
import sys
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('check', anonymous=True)

    rospy.Subscriber('scan', LaserScan, laserdata)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def laserdata(data):
    for i in range (180, 185):
        lidar_dis = data.ranges[i]

        print("%dth value" %i, lidar_dis)

    print("")
    
    for j in range (50, 70):
        lidar_dis1 = data.ranges[j]

        print("%dth value" %j, lidar_dis1)


    for k in range (90, 110):
        lidar_dis2 = data.ranges[k]

        print("%dth value" %k, lidar_dis2)


    for l in range (0, 10) and (340, 359):
        lidar_dis3 = data.ranges[l]

        print("%dth value" %l, lidar_dis3)

    if lidar_dis < 0.3:
        print("STOP")

    if lidar_dis1 < 0.3:
        print("L")

    if lidar_dis2 < 0.3:
        print("R")

    if lidar_dis3 < 0.3:
        print("B")


class motor_control:
	
	def __init__(self):
	 self.rate = rospy.Rate(10)
	 self.timer_to_sending_data=0
	 
	 self.speed = rospy.Publisher('/commands/motor/speed', Float64, queue_size=1)
	 self.position = rospy.Publisher('/commands/servo/position', Float64, queue_size=1)

	 while not rospy.is_shutdown(): 
	  self.speed_value=1700
        if lidar_dis < 0.3:
           self.speed_value=0
	  self.position_value=0.56
	  self.speed.publish(self.speed_value)
	  self.position.publish(self.position_value)
	  self.rate.sleep()


def main(args):
	rospy.init_node('motor_control',anonymous=True)

	motor_control()
	rospy.spin()

if __name__=='__main__':
	
	main(sys.argv)
	

