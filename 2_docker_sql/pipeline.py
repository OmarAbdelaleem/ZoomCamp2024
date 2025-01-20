import sys  # sys is a built-in module in python
import pandas as pd # pandas is a third-party module

print(sys.argv) # sys.argv is a list in Python, which contains the command-line arguments passed to the script.

day = sys.argv[1] # sys.argv[0] is the script name itself and sys.argv[1] is the first argument passed to the script.

# Some fancy stuff with pandas

print('job finished successfully for day = {day}')   