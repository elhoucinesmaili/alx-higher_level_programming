#!/usr/bin/python3
import sys

if __name__ == "__main__":
    import hidden_4

    # Get all the names defined by the module
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
