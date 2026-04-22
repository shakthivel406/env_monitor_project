import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class EnvMonitor(Node):
    def __init__(self):
        super().__init__('env_monitor')

        self.x = 0.0
        self.y = 0.0

        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        # 🔥 Timer ensures continuous output
        self.timer = self.create_timer(1.0, self.process_data)

    def odom_callback(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

    def process_data(self):
        x = self.x
        y = self.y

        zone = "UNKNOWN"
        temp = 0
        gas = False

        # 🔴 Kitchen FIRST
        if y < -1.0:
            zone = "KITCHEN"
            temp = 35

            if -0.5 < x < 0.5 and -2.0 < y < -1.0:
                gas = True

        elif x > 0:
            zone = "HALL"
            temp = 25

        elif x < 0:
            zone = "ROOM"
            temp = 22

        print("\n==============================")
        print(f"📍 LOCATION: {zone}")
        print(f"🌡️ TEMPERATURE: {temp}°C")

        if gas:
            print("🚨 ALERT: GAS LEAK DETECTED !!!")
        else:
            print("✅ STATUS: SAFE")

        print("==============================")


def main(args=None):
    rclpy.init(args=args)
    node = EnvMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
