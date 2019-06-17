import sys
import subprocess
import numpy as np
import glob

# imput arguments for the script
filename = sys.argv[1]
dm_start = sys.argv[2]
dm_end = sys.argv[3]

# run PEASOUP
cmd = 'peasoup -v -i {0} --dm_start {1} --dm_end {2}'.format(filename, dm_start, dm_end)
print cmd
subprocess.call(cmd, shell=True)

