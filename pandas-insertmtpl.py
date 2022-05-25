import glob
import os
print 1,2,3,4,5
files = glob.glob("file_*.csv")

result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
