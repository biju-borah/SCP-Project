import random
import copy

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
        # print(self.contents)
    
    def draw(self,no):
        temp = copy.deepcopy(self.contents)
        if no > len(self.contents):
            return self.contents
        else:
            for i in range(no):
                j = random.randrange(0,len(temp))
                temp.pop(j)
            return temp
                
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    M = 0
    for i in range(num_experiments):
        temp = 0
        ball = dict()
        l = hat.draw(num_balls_drawn)
        # print(l)
        for j in l:
            t = 0
            for k in l:
                if j == k:
                    t += 1
            ball[j] = t
        for key, value in expected_balls.items():
            if key in ball and ball[key] >= value:
                # print("test")
                temp += 1
        if temp == len(expected_balls):
            M += 1
    return M/num_experiments



hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)