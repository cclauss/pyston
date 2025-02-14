import os
import subprocess
import sys

exe = os.path.abspath(sys.executable)

def run(bench, *args, retries=3):
    for i in range(retries):
        code = subprocess.call([exe, bench] + list(args))
        if code == 0:
            return
    raise Exception((bench, args, code))

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    run("macrobenchmarks/benchmarks/djangocms.py", "800") # approx 21s
    run("macrobenchmarks/benchmarks/flaskblogging.py", "1800") # approx 10s
