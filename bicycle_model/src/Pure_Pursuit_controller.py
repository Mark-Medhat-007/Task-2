#!/usr/bin/env python3
import rospy 
from bicycle_model.msg import steering_velocity
import math
bicycle_velocity=10
look_ahead_x=0
look_ahead_y=0
required_look_ahead=40
x_bicycle=0
y_bicycle=0
l=1.5                              #length of bicycle model
k=2
def talker():
	global look_ahead_x
	global look_ahead_y
	global x_bicycle
	global y_bicycle
	pub = rospy.Publisher('/s_v', steering_velocity, queue_size=10)
	rospy.init_node('user_info_driver', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		while(look_ahead_x<1500):                                  #x is to identify that the while loop found the intersection by look ahead distance
			look_ahead_y=200*math.sin(0.1*look_ahead_x)
			look_ahead_x=look_ahead_x+1
			ld=math.sqrt((look_ahead_x-x_bicycle)**2+(look_ahead_y-y_bicycle)**2)
			if (ld>(required_look_ahead-10) and ld<(required_look_ahead+10)):
				break
		if not (look_ahead_x-x_bicycle==0):
			slope =(look_ahead_y-y_bicycle)/(look_ahead_x-x_bicycle)
		
		alpha=math.atan(slope)
		
		if alpha > math.pi/2 and alpha <= math.pi:					
			alpha=	math.pi/2
		if alpha > math.pi and alpha < 3*math.pi/2:						
			alpha=	-math.pi/2
		ld=math.sqrt((look_ahead_x-x_bicycle)**2+(look_ahead_y-y_bicycle)**2)
		
		if (ld==0):
			steering_angle=math.pi/2
		else:
			steering_angle=math.atan((2*l*math.sin(alpha))/ld)
		
		if steering_angle>(math.pi/6) :
			steering_angle=(math.pi/6)
		
		if steering_angle<(-math.pi/6) :
			steering_angle=(-math.pi/6)
		
		y_bicycle=look_ahead_y 
		x_bicycle=look_ahead_x
		message=steering_velocity()
		message.steering = steering_angle
		message.velocity = bicycle_velocity	       #simulating one point
		rospy.loginfo(message)
		pub.publish(message)

		rate.sleep()
		
if __name__==  '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
