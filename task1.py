import time
import random
# File should have 1 input that reads an integer
# generates 3 files: tdata<x>.py tbest<x>.py and tworst<x>.py where x is the integer
# each datafile will be importable so we can read the variable that is stored within it. 

class project():
    def __init__(self):
        n=self.get_input()
        self.generate_files(n)

    def get_input(self):
        while True:
            try:
                n=int(input("Enter number of data: "))
                if n > 0:
                    return n
                else:
                    print("Please enter a positive integer.")
            except:
                print("Please enter an integer")

    def generate_files(self,n):
        best=list(range(1,n+1))
        worst=list(range(n,0,-1))
        data=random.sample(range(1,n+1),n)

        self.write(f"tbest{n}.py",best)
        self.write(f"tworst{n}.py",worst)
        self.write(f"tdata{n}.py",data)

        print("Files generated!")

    def write(self, filename,data):
        with open (filename,"w")as f:
            f.write(f"data={data}")

project()

