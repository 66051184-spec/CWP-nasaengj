import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    print("parameters: " + str(len(params)))
    for param in params:
        print(param + ": " + str(len(param)))
