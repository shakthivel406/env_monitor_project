import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class Patrol(Node):
    def __init__(self):
        super().__init__('patrol_node')
        self.publisher = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.timer = self.create_timer(2.5, self.send_goal)
        self.index = 0

        # Zone coordinates
        self.goals = [
            (1.5, 0.0),   # Hall
            (-1.5, 0.0),  # Room
            (0.0, -1.5)   # Kitchen
        ]

    def send_goal(self):
        x, y = self.goals[self.index]

        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.header.stamp = self.get_clock().now().to_msg()

        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.orientation.w = 1.0

        self.publisher.publish(goal)

        self.get_logger().info("🤖 Navigating to next zone...")
        self.get_logger().info(f"➡️ Target: ({x}, {y})")

        self.index = (self.index + 1) % len(self.goals)

def main(args=None):
    rclpy.init(args=args)
    node = Patrol()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
