#!/usr/bin/python3
"""
Module docs
"""

import sys

code_dict = {}
total_size = 0
file_size_index = -1
status_code_index = -2
valid_index = {200, 301, 400, 401, 403, 404, 405, 500}
i = 0

try:
    for line in sys.stdin:
        stripped = line.split()
        try:
            file_size = int(stripped[file_size_index])
            total_size += file_size
        except (IndexError, ValueError):
            pass
        try:
            code = int(stripped[status_code_index])
            if code in valid_index:
                if code in code_dict:
                    code_dict[code] += 1
                else:
                    code_dict[code] = 1
        except (IndexError, ValueError):
            pass

        i += 1

        if i != 0 and i % 10 == 0:
            print("File size: {:d}".format(total_size))
            for c in sorted(code_dict):
                print("{}: {}".format(c, code_dict[c]))

    print("File size: {:d}".format(total_size))
    for c in sorted(code_dict):
        print("{}: {}".format(c, code_dict[c])

except KeyboardInterrupt:
    print("File size: {:d}".format(total_size))
    for c in sorted(code_dict):
        print("{}: {}".format(c, code_dict[c]))
    raise
