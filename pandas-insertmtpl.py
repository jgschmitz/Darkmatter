import glob
import os
import sklearn
import tensorflow as TF


files = glob.glob("file_*.csv")

result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
