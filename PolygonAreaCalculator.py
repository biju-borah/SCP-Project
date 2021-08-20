class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __repr__(self):
        string = "Rectangle(height=" + str(self.height) + ",width=" + str(self.width) + ")"
        return string
    def set_width(self,width):
        if type(self) is Square:
            self.width = width 
            self.height = width        
        self.width = width
    def set_height(self,height):
        if type(self) is Square:
            self.width = height 
            self.height = height 
        self.height = height
    def get_area(self):
        return self.height * self.width
    def get_perimeter(self):
        return ((self.width*2) + (self.height*2))
    def get_diagonal(self):
        return (((self.width ** 2) + (self.height ** 2)) ** .5)
    def get_picture(self):
        for i in range(self.height):
            for j in range(self.width):
                print("*",end="")
            print("")
    def get_amount_inside(self,other):
        width1 = self.width
        width2 = other.width
        height1 = self.height
        height2 = other.height
        count1 = 0
        count2 = 0
        if width1<width2 or height1<height2:
            return 0
        else:
            count1 = width1//width2
            count2 = height1//height2
            return count1*count2
    
class Square(Rectangle):
    def __init__(self,side):
        self.side = side
        super().__init__(side,side)
    def __repr__(self):
        string = "Square(side=" + str(self.side) + ")"
        return string
    def set_side(self,side):
        super().__init__(side,side)
        self.side = side

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
rect.get_picture()
 
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
sq.set_width(6)
sq.get_picture()