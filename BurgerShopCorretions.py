
Burgers = {"Hamburger":10.25, "Cheeseburger":11.50,"Double Cheeseburger":13.00,"Chicken Club":11.00, "Chicken Sandwich":9.00, "Turkey Sandwich":8.50,"Fish Sandwich":9.00, "Buffalo Chicken":12.00}
Sides = {"Fries":2.00,"Onion Rings":2.40, "Side Salad":3.25, "Tater Tots":2.25}
Beverages={"soda":1.00,"beer":3.00,"water":0.0}
ComboSz={"Small":1.50,"Medium":2.00,"Large":2.75}
Condiments={"ketchup","mustard","relish","Mayo","barbeque sauce"}
class FoodItem:
    cost = 0
    name = ""
    foodItem=[]
    def __init__(self,name,cost):
        self.nm = name
        self.cst = cost
        
        

class Burger(FoodItem):
    #isWellDone = True
    #OLTP means Onion Lettuce Tomato Pickle  
 # isWelldone, OLTP=True, isVegan=False
    def __init__(self, name, cost= 0):
        #self.WD = isWelldone
        #self.BLT = OLTP
        #self.veg = isVegan
        self.n = name
        self.c = cost
        #super().__init__(self.n, self.c)
    def display(self):
        print("Burger: ", self.n,"\t")
        print("Price: ","$", self.c)
        print("---------------------")
    def total(self):
        return self.c

    
#class Sandwich(Burger):
 #   chicken = True
  #  fried= False
   # def __init__(self, name, ck, frd, OLTP=True, cost=0, size=""):
    #    self.chicken= ck
     #   self.fried= frd
      #  super().__init__(name, OLTP, cost, size)
class Side(FoodItem):
    def __init__(self, name, cost):
            self.n = name
            self.c = cost
           # super().__init__(self.n, self.c)
    def display(self):
       print("Side: ", self.n,"\t")
       print("Price: ","$", self.c)
       print("------------------------------------")
    def total(self):
        return self.c

class Beverage(FoodItem):
    def __init__(self, name, cost):
             self.n= name
             self.c = cost
             #super().__init__(name, cost)
    def display(self):
       print("Drink: ", self.n, "\t")
       print("Price: $", self.c)
       print('-------------------------------')
    def total(self):
        return self.c
class Combo(Burger,Side,Beverage):
    def __init__(self,size,b,s,d):
        self.cz=size
        self.burg=b
        self.side = s
        self.drink = d
        super().__init__(self.name, self.cost)
    def display(self,):
        print("Burger :",self.burg, self.side,self.drink)
    items =[]

class Ordering:
    def Burg_Input():
        b = Burger()
        return b
    def Side_Input():
        s = Side()
        return s
    def Drink_Input():
        d = Beverage()
        return d
    def Combo_Input():
        cc = Combo(ComboSz,Burger,Side,Beverage)
        return cc
    
    def takeOrder():
        receipt=[]
        total=0
        print("Hello and Welcome to the Burger Shop!")
        Ordername = input("Let me get a name for the order: ")
        print("What burger would you like? we have: ",list(Burgers.keys()))
        Burg=input('Enter an entree: ')
        while Burg not in ((Burgers.keys())):
               print("Sorry we dont have that")
               Burg=input('Enter an entree: ')

        b=Burger(Burg,Burgers[Burg])
        receipt.append(b)
        print("Would you like a combo with that or just the entree?")
        wantCombo = int(input("Enter 1 for combo or 2 for just entree: "))
        if wantCombo==1:
            size=input("What size combo do you want? \n Enter Small, Medium or Large")
            if size not in ComboSz:
                print("Sorry, we dont have this size")
            else:
                receipt.append(size)
            print("What side would you like? We have",list(Sides.keys()))
            side = input("Enter a side and what size you want: ")
            while side not in Sides.keys():
                    print("sorry we dont have that")
                    side=input("Please choose a valid side")
            s=Side(side,Sides[side])
            receipt.append(s)
            print("What drink would you like? We have",list(Beverages.keys()))
            drink = input("enter a beverage: ")
            while drink not in Beverages:
                    print("sorry we dont have that")
                    drink=input("enter a beverage")
            d=Beverage(drink,Beverages[drink])
            receipt.append(d)
            cc=Combo(size,b,s,d)
            cc.display()
        elif wantCombo==2:
            cont_Order=""
            print(f"Ok so Ive got a {Burg}")
            while True:
                cont_Order=input("Anything else I can get for you? \n Press 1 for yes or 2 for no: ")
                if cont_Order=="1":
                    order = input("Ok, Please input another item: ")
                    if (order in Burgers):
                        b=Burger(order,Burgers[order])
                        receipt.append(b)
                        print(f"great! Ive got an {order}")
                    elif (order in Sides):
                        s=Side(order, Sides[order])
                        receipt.append(s)
                        print(f"great! Ive got an {order}")
                    elif (order in Beverages):
                        d=Beverage(order,Beverages[order])
                        receipt.append(d)
                        print(f"great! Ive got an {order}")
                    else:
                        print("We dont offer that item here")
                   # if Burgers.keys() and Sides.keys() and Beverages.keys() in receipt:
                        #print("combo")
                elif cont_Order=='2':
                    break
                    
                else:
                    print("invalid input, try again")
            for i in receipt:
                i.display()
            confirm=input("Everthing look good on the screen? \n hit 1 for yes or 2 for no: ")
            if confirm=='1':
                subtotal=0
                for i in receipt:
                    print(i.display())
                    subtotal+=i.total()
                print("Subtotal: ",subtotal)
                tax=(subtotal*.0825)
                tax=round(tax,2)
                print("Tax: ",tax,"\n--------------------")
                total=subtotal+(tax) #total including tax rate of 8.25%
                total=round(total,2)
                print("Your total is: ", total)
                while True:
                    try:
                        tip=float(input("Enter a value or 0 for no tip: "))
                        if tip>0.00:
                            print("Thank You!")
                            tip=round(tip,2)
                            tip_total=total+tip
                            print("the final price is: ",tip_total)
                            False
                            break
                        else:
                            pass
                    except ValueError:
                        print("Please enter a valid tip value or 0 for no tip: ")
            else:
                print("We dont have that")

    takeOrder()
  


     