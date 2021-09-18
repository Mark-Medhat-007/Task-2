#!/usr/bin/env python3
import rospy 
from bicycle_model.msg import steering_velocity

def talker():
	pub = rospy.Publisher('/s_v', steering_velocity, queue_size=10)
	rospy.init_node('user_info_driver', anonymous=True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		message=steering_velocity()
		message.steering = 15
		message.velocity =10           #simulating one point
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()
		
if __name__==  '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
