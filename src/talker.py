import rospy
from std_msgs.msg import String
    
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        hello_str = "ROS UNIDA %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass




"""import rospy
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1 mensaje por segundo
    msg_count = 0
    while not rospy.is_shutdown() and msg_count < 20:
        hello_str = "Fabian Nicolas Fleitas Espinoza - %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        msg_count += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
"""
