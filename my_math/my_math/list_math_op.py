#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
def add_lists(list1, list2):
    """
    Adds two lists of numbers element-wise.
    Returns:
    - A list containing the element-wise sum of list1 and list2.
    """
    # Check if the lists have the same length
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length to perform element-wise addition.")

    # Use a list comprehension to add the elements element-wise
    result = [x + y for x, y in zip(list1, list2)]
    
    return result


def multiply_lists(list1, list2):
    """
    Multiplies two lists of numbers element-wise.
    Returns:
    - A list containing the element-wise sum of list1 and list2.
    """
    # Check if the lists have the same length
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length to perform element-wise addition.")

    # Use a list comprehension to add the elements element-wise
    result = [x * y for x, y in zip(list1, list2)]
    
    return result

def get_larger_elements(list1, list2):
    """
    Compares two lists element-wise and returns the larger elements from each list.

    Returns:
    - A tuple containing two lists:
      - The first list contains the larger elements from list1 and list2.
      - The second list contains the smaller elements from list1 and list2.
    """
    # Check if the lists have the same length
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length for comparison.")

    # Initialize lists to store the larger and smaller elements
    larger_elements = []
    smaller_elements = []

    # Compare the elements element-wise and store the results
    for x, y in zip(list1, list2):
        if x >= y:
            larger_elements.append(x)
            smaller_elements.append(y)
        else:
            larger_elements.append(y)
            smaller_elements.append(x)

    return larger_elements, smaller_elements

class MyMathNode(Node):

    def __init__(self):
        super().__init__('my_math_node')
        self.get_logger().info('My Math Node is running.')

    # Define your math operations and other functionality here

    # Example usage:
    list1 = [1, 4, 7, 2]
    list2 = [3, 2, 8, 6]

    result = add_lists(list1, list2)
    print(result)  # Output: [6, 8, 10, 12]

    result = multiply_lists(list1, list2)
    print(result)  # Output: [5, 12, 21, 32]

    larger, smaller  = get_larger_elements(list1, list2)
    print("Smaller Elements:", smaller)     # Output: [1, 2, 7, 2]
    print("Larger Elements:", larger)       # Output: [3, 4, 8, 6]


def main(args=None):
    rclpy.init(args=args)

    my_math_node = MyMathNode()
    try:
        rclpy.spin(my_math_node)
    except KeyboardInterrupt:
        my_math_node.get_logger().info('My Math Node stopped cleanly.')
    finally:
        my_math_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()