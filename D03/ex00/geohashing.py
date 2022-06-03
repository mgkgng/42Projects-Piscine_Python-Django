import antigravity, sys

def checkArg(a1, a2):
	try :
		float(a1)
		float(a2)
	except Exception as e:
		print(e)
		print("Error: Argument cannot be converted to float.")
		exit(1)
	return (True)

if __name__=="__main__":
	if len(sys.argv) != 4:
		print("Error: Wrong number of arguments.")
		exit(1)
	if (checkArg(sys.argv[1], sys.argv[2]) == True):
		antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode())