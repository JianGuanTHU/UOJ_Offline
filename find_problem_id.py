#!/usr/bin/env python
with open("./submission.conf", "r") as fin:
    for line in fin:
        tmp = line.strip().split()
        if line.strip().split()[0] == "problem_id":
            print tmp[1]
