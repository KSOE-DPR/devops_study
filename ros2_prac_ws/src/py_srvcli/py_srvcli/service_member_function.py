from example_interfaces.srv import AddTwoInts
from tutorial_interfaces.srv import CustomSrv
import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv  = self.create_service(CustomSrv, 'custom_srv',self.CustomSrv_callback)

    def CustomSrv_callback(self, request, response):
        response.sum = request.a 
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response
    
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def test_fib():
    assert fib(7) == 13

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()