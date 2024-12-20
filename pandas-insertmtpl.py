files = glob.glob("path/to/your/files/file_*.csv")
####If the files are large, you can use a generator for better memory efficiency:

result = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
