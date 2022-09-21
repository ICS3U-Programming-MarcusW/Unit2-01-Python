#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Sep. 21, 2022
# This program calculates and displays the area and perimeter of a
# circle with radius 15 mm.
import math


def main():
    print("For a circle that has a radius")
    print("of 15 mm:")
    print("")
    print("Area = {} mm^2".format(math.pi * 15**2))
    print("Perimeter = {} mm".format(2 * math.pi * 15))


if __name__ == "__main__":
    main()