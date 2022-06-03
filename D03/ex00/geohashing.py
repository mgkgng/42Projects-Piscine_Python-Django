import antigravity, sys

if __name__=="__main__":
	if len(sys.argv) != 4:
		print("Error: Wrong number of arguments.")
		exit(1)
	antigravity.geohash(sys.argv[1], sys.argv[2], sys.argv[3])