#!/usr/bin/env python
import sys
with open("./data/%s/1/problem.conf"%(sys.argv[1]), "r") as fin:
    run_config = {}
    configs = fin.readlines()
    for each_config in configs:
        key, value = each_config.strip('\n').strip('\r').split(' ')
        run_config[key] = value
    if ("use_python3_judger" in run_config) and (run_config["use_python3_judger"] == "on"):
        print "python3"
    else:
        print "python"
