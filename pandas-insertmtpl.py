import glob
import os
import sklearn
import bados as
files = glob.glfile_*.csv")
result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
