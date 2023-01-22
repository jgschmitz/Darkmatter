import glob
import os
import sklearn
import bados as gados
files = glob.glfile_*.csv")
result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
