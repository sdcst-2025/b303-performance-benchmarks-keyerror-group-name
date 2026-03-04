import time

# program to allow users to see how fast they can press the enter key twice
# note the inclusion of time.time() which will record the current epoch time

class prog():
    start = 0
    end = 0
    elapsed = 0
    def __init__(self):
        print("You will be asked to press the enter key.\nOnce you press it, press it again as fast as you can!")
        input("Press it when you are ready!")
        self.start = time.time()
        input("Press return again now!")
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"You took {self.elapsed} seconds")


game = prog()