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

class Jp2EnPublisher(Node):
    def __init__(self):
        super().__init__('jp2en_publisher')
        self.translator = googletrans.Translator()

        # qos_policy = rclpy.qos.QoSProfile(depth=10, reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT)
        self.pub_text = self.create_publisher(String, '/text_prompt',10)
        self.input_thread = threading.Thread(target=self.read_input)
        self.input_thread.start()

    def read_input(self):
        self.get_logger().info(f'Enter message in Japanese')
        while rclpy.ok():
            text_jp = input("JP message: ")
            text_en = self.translator.translate(text_jp, src='ja', dest='en').text

            msg = String()
            msg.data = text_en
            self.pub_text.publish(msg)
            self.get_logger().info(f'EN message: {text_en}')

def main():
    rclpy.init()
    node = Jp2EnPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()