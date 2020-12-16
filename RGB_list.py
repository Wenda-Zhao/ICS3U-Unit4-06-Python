#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program for nested loop


def main():
    # this function for nested loop

    R = 0
    G = 0
    B = 0

    # process & output
    for R in range(256):
        for G in range(256):
            for B in range(256):
                print("RGB ({0}, {1}, {2})".format(R, G, B))


if __name__ == "__main__":
    main()
