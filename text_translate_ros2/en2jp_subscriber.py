import rclpy
from rclpy.node import Node
import logging
# msgs
from std_msgs.msg import Header, Bool, String
# add
from builtin_interfaces.msg import Time
from tf2_ros import Buffer, TransformListener
from collections import deque
import threading

import googletrans

class En2JpSubscriber(Node):
    def __init__(self):
        super().__init__('en2jp_subscriber')
        self.translator = googletrans.Translator()

        # qos_policy = rclpy.qos.QoSProfile(depth=10, reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT)
        self.sub_text = self.create_subscription(String(), '/text', self.CB_main,10)

    def CB_main(self, msg):
        text_en = msg.data
        text_jp = self.translator.translate(text_en, src='en', dest='ja').text
        self.get_logger().info(f'EN message: {text_en}')
        self.get_logger().info(f'JP message: {text_jp}')
        
def main():
    rclpy.init()
    node = En2JpSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()