def cube(n):
    return n**3
if __name__ == "__main__":
  import sys 
if len(sys.argv) != 2:
    script_name = sys.argv[0]
    n=int(sys.argv[1])
else:
    n=4
    print("The cube is: ", cube(n))
