#!/usr/bin/env python3
import subprocess, sys

action = sys.argv[1]
args = sys.argv[2:]

def run(cmd):
    result = subprocess.run(cmd, shell=True, text=True)
    print(result.stdout)
    return result.returncode

if action == "status":
    run("git status")
elif action == "branch":
    run(f"git checkout -b {args[0]}")
elif action == "add":
    run(f"git add {' '.join(args)}")
elif action == "commit":
    run(f"git commit -m \"{args[0]}\"")
elif action == "push":
    run(f"git push {args[0]} {args[1]}")
