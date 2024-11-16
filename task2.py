import matplotlib.pyplot as plt
import numpy as np


def draw_pythagoras_tree(ax, x, y, length, angle, level):
    if level == 0:
        return

    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    ax.plot([x, x_end], [y, y_end], color="green", lw=1)

    new_length = length * np.sqrt(2) / 2

    left_angle = angle + np.pi / 4
    draw_pythagoras_tree(ax, x_end, y_end, new_length, left_angle, level - 1)

    right_angle = angle - np.pi / 4
    draw_pythagoras_tree(ax, x_end, y_end, new_length, right_angle, level - 1)


def main():
    recursion_depth = int(input("Enter the recursion depth for the Pythagoras tree: "))

    fig, ax = plt.subplots(figsize=(10, 10))

    ax.set_aspect('equal')
    ax.axis('off')

    initial_x = 0
    initial_y = 0
    initial_length = 1
    initial_angle = np.pi / 2  # Start pointing upwards

    draw_pythagoras_tree(ax, initial_x, initial_y, initial_length, initial_angle, recursion_depth)

    plt.show()


if __name__ == "__main__":
    main()
