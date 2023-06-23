# Functional Prompt
# flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)


'''
Make sure to answer the following questions about your coding process:

Q: How does this solution ensure data immutability?
    A: Data has been created and cannot be changed.
        
Q: Is this solution a pure function? Why or why not?
    A: Yes it is because it's output value follows solely from its input values, without any observable side effects.
    
Q: Is this solution a higher order function? Why or why not?
       A: Describing the result you want rather than explicitly specifying the steps required to get there.
       
Q: Would it have been easier to solve this problem using a different programming style?
     A: Very possible. I do not hava a good answer to that. 
     
Q: Why in particular is functional programming a helpful paradigm when solving this problem?
        A: Paradigms are important because they define a programming language and how it works
'''
# Object Oriented Prompt

# Watto needs a new system for organizing his inventory of podracers.
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.


class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Define a repair() method that will update the condition of the podracer to "repaired".


    def repair(self):
        self.condition = "repaired"


# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price):

    def boost(self):
        self.max_speed *= 2


# Define another class that inherits Podracer and call this one SebulbasPod.
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price):

    def flame_jet(self, other):
        other.condition = "trashed"


'''
Make sure to answer the following prompts about your coding experience:

Q: How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    A:  Abstraction, Encapsulation, Inheritance, Polymorphism. 

Q:Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    A: Probably not because of the easiness of reusing the code through inheritance. 
    
Q:How in particular did Object Oriented Programming assist in the solving of this problem?
    A: Object-oriented programming is ultimately about taking a huge problem and breaking it down to solvable chunks.
'''