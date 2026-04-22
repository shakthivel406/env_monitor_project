import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker

class ZoneVisualizer(Node):
    def __init__(self):
        super().__init__('zone_visualizer')
        self.publisher = self.create_publisher(Marker, '/zone_markers', 10)
        self.timer = self.create_timer(1.0, self.publish_zones)

    def create_zone(self, id, x, y, color):
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "zones"
        marker.id = id
        marker.type = Marker.CUBE
        marker.action = Marker.ADD

        marker.pose.position.x = x
        marker.pose.position.y = y
        marker.pose.position.z = 0.0

        marker.scale.x = 2.0
        marker.scale.y = 2.0
        marker.scale.z = 0.1

        marker.color.r = color[0]
        marker.color.g = color[1]
        marker.color.b = color[2]
        marker.color.a = 0.3

        return marker

    def publish_zones(self):
        hall = self.create_zone(1, 1.5, 0.0, (0.0, 1.0, 0.0))     # Green
        room = self.create_zone(2, -1.5, 0.0, (0.0, 0.0, 1.0))    # Blue
        kitchen = self.create_zone(3, 0.0, -1.5, (1.0, 0.0, 0.0)) # Red

        self.publisher.publish(hall)
        self.publisher.publish(room)
        self.publisher.publish(kitchen)

def main(args=None):
    rclpy.init(args=args)
    node = ZoneVisualizer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
