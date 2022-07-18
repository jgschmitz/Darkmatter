import glob
import os
import sklearn
from gestalt
files = glob.glob("file_*.csv")
result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

