#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool, Float64
from sensor_msgs.msg import Joy

class Topic2Joy:
    def __init__(self):

        # メッセージを格納する変数を初期化
        self.button_datas = []
        for i in range(15):
          self.button_datas.append(0)

        self.axis_datas = []
        for i in range(4):
          self.axis_datas.append(0)

        node_name = rospy.get_name()

        self.bs1 = rospy.Subscriber(node_name + '/button1', Bool, self.button_callback1)
        self.bs2 = rospy.Subscriber(node_name + '/button2', Bool, self.button_callback2)
        self.bs3 = rospy.Subscriber(node_name + '/button3', Bool, self.button_callback3)
        self.bs4 = rospy.Subscriber(node_name + '/button4', Bool, self.button_callback4)
        self.bs5 = rospy.Subscriber(node_name + '/button5', Bool, self.button_callback5)

        self.bs6 = rospy.Subscriber(node_name + '/button6', Bool, self.button_callback6)
        self.bs7 = rospy.Subscriber(node_name + '/button7', Bool, self.button_callback7)
        self.bs8 = rospy.Subscriber(node_name + '/button8', Bool, self.button_callback8)
        self.bs9 = rospy.Subscriber(node_name + '/button9', Bool, self.button_callback9)
        self.bs10 = rospy.Subscriber(node_name + '/button10', Bool, self.button_callback10)

        self.bs11 = rospy.Subscriber(node_name + '/button11', Bool, self.button_callback11)
        self.bs12 = rospy.Subscriber(node_name + '/button12', Bool, self.button_callback12)
        self.bs13 = rospy.Subscriber(node_name + '/button13', Bool, self.button_callback13)
        self.bs14 = rospy.Subscriber(node_name + '/button14', Bool, self.button_callback14)
        self.bs15 = rospy.Subscriber(node_name + '/button15', Bool, self.button_callback15)

        self.as1 = rospy.Subscriber(node_name + '/axis1', Float64, self.axis_callback1)
        self.as2 = rospy.Subscriber(node_name + '/axis2', Float64, self.axis_callback2)
        self.as3 = rospy.Subscriber(node_name + '/axis3', Float64, self.axis_callback3)
        self.as4 = rospy.Subscriber(node_name + '/axis4', Float64, self.axis_callback4)

        # パブリッシャーの設定
        self.joy_pub = rospy.Publisher('joy', Joy, queue_size=10)

    # button data callbacks
    def button_callback1(self, msg):
        self.button_datas[0] = int(msg.data)

    def button_callback2(self, msg):
        self.button_datas[1] = int(msg.data)

    def button_callback3(self, msg):
        self.button_datas[2] = int(msg.data)

    def button_callback4(self, msg):
        self.button_datas[3] = int(msg.data)

    def button_callback5(self, msg):
        self.button_datas[4] = int(msg.data)

    def button_callback6(self, msg):
        self.button_datas[5] = int(msg.data)

    def button_callback7(self, msg):
        self.button_datas[6] = int(msg.data)

    def button_callback8(self, msg):
        self.button_datas[7] = int(msg.data)

    def button_callback9(self, msg):
        self.button_datas[8] = int(msg.data)

    def button_callback10(self, msg):
        self.button_datas[9] = int(msg.data)

    def button_callback11(self, msg):
        self.button_datas[10] = int(msg.data)

    def button_callback12(self, msg):
        self.button_datas[11] = int(msg.data)

    def button_callback13(self, msg):
        self.button_datas[12] = int(msg.data)

    def button_callback14(self, msg):
        self.button_datas[13] = int(msg.data)

    def button_callback15(self, msg):
        self.button_datas[14] = int(msg.data)

    # axis data callbacks
    def axis_callback1(self, msg):
        self.axis_datas[0] = msg.data

    def axis_callback2(self, msg):
        self.axis_datas[1] = msg.data

    def axis_callback3(self, msg):
        self.axis_datas[2] = msg.data

    def axis_callback4(self, msg):
        self.axis_datas[3] = msg.data

    def publish_joy(self):
        joy_msg = Joy()
        joy_msg.axes = self.axis_datas
        joy_msg.buttons = self.button_datas
        self.joy_pub.publish(joy_msg)

if __name__ == '__main__':

    rospy.init_node('topic_to_joy')
    r = rospy.Rate(100)
    t2j = Topic2Joy()

    while not rospy.is_shutdown():
      t2j.publish_joy()
      r.sleep()

    
