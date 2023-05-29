import math
import random

class game:
    def __init__(self, A, B):
        self.low = A
        self.high = B
    
    def generate(self):
        self.number = random.randint(self.low, self.high)
        self.count = 0
    
    def gess(self):
        gess_number = int(input())
        self.count += 1
        if gess_number == self.number:
            return True, self.count
        return False, 0

print("Please input range")
a, b = map(int, input().split())

print("Give Gess limit")
limit = int(input())

play = game(a, b)

flag = True

while flag:
    print("I am generating a number please gess a number in the limit", limit)
    play.generate()
    
    for _ in range(limit):
        find, cut = play.gess()
        
        if find:
            print("You gess correct number in count",cut)
            break
        else:
            print("please gess a another number")
    print("Do you want to play again, if yes please input 1")
    t = int(input())
    if t != 1:
        print("Thankyou for playing")
        flag = False
    
        