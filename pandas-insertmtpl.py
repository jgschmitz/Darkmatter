import glob
import os
import sklearn
print 1,2,3,4,5,6,7,8,9,10
files = glob.glob("file_*.csv")
result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
