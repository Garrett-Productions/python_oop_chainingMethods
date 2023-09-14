#This is called chaining. In order for this to work, each method must return self. By returning self, if we recall how functions work, each method call will now be equal to the instance that called it.

# user1.display_info().enroll().spend_points(50).display_info()
# user2.enroll().spend_points(80).display_info()

class User:
    # .. constructor
    
    def display_info(self):
        # your code
    
        # new return statement, returns this same object
        return self

#The practice of having OOP return its own instance is pretty common and is done in other programming languages, 
# though the variable name in some languages is not self, but instead this.
#This only works with methods that do not need to return anything. 
# If your method needs to return something other than self, it is not possible to chain the method.

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self


    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return self
        else:
            self.is_rewards_member = True 
            self.gold_card_points = 200
            return self



    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Sorry you're broke.")
        return self



Garrett = User("Garrett", "Turner", "GarrettTurnerProductions@gmail.com", 28)

Garrett.display_info().enroll().spend_points(50)
Garrett.display_info() #this line here I'm displaying info again to check to make sure my chaining method is functioning correctly, it is. I returned self on all 3 methods created.

#We created 2 more instances of the user class below

# Baker = User("Justin", "Baker", "JustinBaker268@gmail.com", 29)
# Big_jerm = User("Jeremy", "Brinson", "BigJerm@aol.com", 28)

# Baker.display_info()
# Big_jerm.display_info()

# #We are enrolling the 2nd User Below 

# Baker.enroll()
# Baker.display_info()

# #Our 2nd User is spending 80 points Below

# Baker.spend_points(80)
# Baker.display_info()

# #Does our user have enough points to spend?

# Baker.spend_points(200)


# Baker.display_info()