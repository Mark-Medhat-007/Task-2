#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import String
from bicycle_model.msg import steering_velocity
from bicycle_model.msg import coordinates
l=4               #bicycle length
theta=30
z=0.0
def callback(data):
	pub = rospy.Publisher('/user_info', coordinates, queue_size=10)
	message=coordinates()
	steer= data.steering
	vel= data.velocity
	x_dot=(vel*math.cos(theta))       #X dot is the x as the the time step is 1 sec which is the rate of ros as we chose in publisher 
	y_dot=(vel*math.sin(theta))       #also y dot is y
	theta_dot=(vel*math.tan(steer))/l
	message.x=x_dot
	message.y=y_dot
	message.theta=theta_dot
	rospy.loginfo(message)
	pub.publish(message)
	rate = rospy.Rate(1)
	rate.sleep()



def listener() :
	rospy.init_node('data_processing', anonymous=True)
	rospy.Subscriber("/s_v", steering_velocity, callback)
	rospy.spin()
	
if __name__== '__main__' :
	listener()
