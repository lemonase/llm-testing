#!/usr/bin/env python3
import random

def generate_ascii_christmas_tree(height):
  """Generates an ASCII representation of a Christmas tree with ornaments.

  Args:
    height: The height of the tree in characters.

  Returns:
    A string representing the ASCII Christmas tree.
  """

  tree = ""

  # Generate the branches
  for i in range(height - 1):
    # Calculate the number of spaces and asterisks for this level
    spaces = height - i - 1
    asterisks = 2 * i + 1

    # Add the spaces
    tree += " " * spaces

    # Add the asterisks
    tree += "*" * asterisks

    # Add a newline character
    tree += "\n"

    # Add ornaments to this level of the tree
    num_ornaments = random.randint(0, 2)
    ornaments = ["^", "*", "%"]
    for ornament in range(num_ornaments):
      ornament_position = random.randint(0, asterisks - 1)
      ornament_type = random.choice(ornaments)
      tree = tree[:spaces + ornament_position] + ornament_type + tree[spaces + ornament_position + 1:]

  # Generate the trunk
  trunk_height = height // 3
  for i in range(trunk_height):
    tree += " " * (height - 1) + "#" + "\n"

  # Return the tree
  return tree


if __name__ == "__main__":
  # Get the height of the tree from the user
  height = int(input("Enter the height of the tree: "))

  # Generate the tree
  tree = generate_ascii_christmas_tree(height)

  # Print the tree
  print(tree)

