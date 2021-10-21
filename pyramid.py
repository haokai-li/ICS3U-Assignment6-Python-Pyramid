#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program calculates the volume of a pyramid

import math


def calculate_volume_pyramid(length, width, height):
    # This function calculates the volume of a pyramid

    # process
    volume = (length * width * height) / 3

    return volume


def main():
    # This function just call other functions

    print("This Program calculates the volume of a pyramid.")
    print("Please enter the length, width and height.")
    print("")

    # input
    user_length_string = input("Please enter the length of a pyramid(cm): ")
    user_width_string = input("Please enter the width of a pyramid(cm): ")
    user_height_string = input("Please enter the height of a pyramid(cm): ")
    print("")

    try:
        user_length_number = float(user_length_string)
        user_width_number = float(user_width_string)
        user_height_number = float(user_height_string)

        # call functions
        calculated_volume_pyramid = calculate_volume_pyramid(
            length=user_length_number,
            width=user_width_number,
            height=user_height_number,
        )

        # output
        print("The volume of the pyramid is {} cm³.".format(calculated_volume_pyramid))

    except Exception:
        # output
        print("You didn't enter an integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
