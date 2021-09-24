#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import String
from bicycle_model.msg import steering_velocity
from bicycle_model.msg import coordinates
l=2               #bicycle length
time_step=1                             #time step is 1 sec which is the rate of ros as we chose in publisher
theta=math.pi/6
def callback(data):
	global theta
	pub = rospy.Publisher('/user_info', coordinates, queue_size=10)
	message=coordinates()
	steer= data.steering
	vel= data.velocity
	x_dot=(vel*math.cos(theta))       
	y_dot=(vel*math.sin(theta))       
	theta_dot=(vel*math.tan(steer))/l
	message.x=x_dot*time_step
	message.y=y_dot*time_step
	theta=theta_dot*time_step
	message.theta=theta
	rospy.loginfo(message)
	pub.publish(message)
	rate = rospy.Rate(10)
	rate.sleep()
	


def listener() :
	rospy.init_node('data_processing', anonymous=True)
	rospy.Subscriber("/s_v", steering_velocity, callback)
	rospy.spin()
	
if __name__== '__main__' :
	listener()
