#!/usr/bin/env python
with open("./submission.conf", "r") as fin:
    run_config = {}
    for line in fin:
        key, value = line.strip('\n').strip('\r').split(' ')
        run_config[key] = value
        tmp = line.strip().split()
        if line.strip().split()[0] == "problem_id":
            print tmp[1]

run_config["uoj_offline"] = "on"
with open("./work/submission.conf", "w") as fout:
    for key in run_config:
        fout.write("%s %s\n"%(key, run_config[key]))