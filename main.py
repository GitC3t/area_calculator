import math
class Area():
    def __init__(self) -> None:
        #main variables
        self.width = None
        self.height = None
        #circle
        self.radius = None
        #trapeziod
        self.shorter = None
        self.longer = None
        #system
        self.mainInput = None
        self.reset = None
    def quadrilateral(self):
        self.width = float(input("Width: "))
        self.height = float(input("Height: "))
        print(f"The area of this shape is {self.width*self.height}.")
    def triangle(self):
        self.width = float(input("Width: "))
        self.height = float(input("Height: "))
        print(f"The area of this shape is {0.5*self.width*self.height}.")
    def circle(self):
        self.radius = float(input("Radius: "))
        print(f"The area to this shape is {math.pi*self.radius**2}.")
    def trapezoid(self):
        self.longer = float(input("Longer base: "))
        self.shorter = float(input("Shorter base: "))
        self.height = float(input("Height: "))
        print(f"The area to this shape is {0.5*(self.longer+self.shorter)*self.height}.")
        
        
        
        
    def main(self):
        opt = False
        while(opt == False):
            area = Area()
            self.mainInput = input("\n Q for a quadrilateral \n T for a triangle \n C for a circle \n TP for a trapezium \n \n Here:  ")
            
            if(self.mainInput == "Q" or self.mainInput == "q"):
                area.quadrilateral()
            elif(self.mainInput == "C" or self.mainInput == "c"):
                area.circle()
            elif(self.mainInput == "T" or self.mainInput == "t"):
                area.triangle()
            elif(self.mainInput == "TP" or self.mainInput == "tp" or self.mainInput == "Tp"):
                area.trapezoid()
            #AFTER DONE#
            
            self.reset = input("Would you like to reset? Y-N: ")
            if(self.reset == "Y" or self.mainInput == "y"):
                print("Opting out, bye bye! :)")
                opt = True
                break
            else:
                #main variables
                self.width = None
                self.height = None
                #circle
                self.radius = None
                #trapeziod
                self.shorter = None
                self.longer = None
                #system
                self.mainInput = None
            
            
area = Area()
area.main()
