# Inheriting object not needed in 3 but python agnostic
class pet: 
    def __init__(self, name):
        self.name = name

    def call(self):
        print("Come here: ", self.name)

    def __str__(self):
        return "pet"

# What if we want to have different animals "say" different things
class dog(pet): 
    def sound(self):
        print("Woof!")

class cat(pet): 
    def sound(self):
        print("Meow!")

class fish(pet): 
    def sound(self):
        print("Blub!")

jax = dog("dog")
jax.call()
jax.sound()

# Issue with this example is that I'm still operating on the same "axis". Their internal data is changing, rather than the structure (IE, we're inputting the same data, vs functionality)
kitty = cat("kitty")
kitty.call()
kitty.sound()

## Issue: How many pet classes do we want to make? Particularly, what happens when we add a new "axis?"
## This seems to be a "Creational" issue
## For example, if we want to treat adopted and bought differently, we double (or triple) the subclasses

class storePet(pet):
    def store(self):
        print("I was bought from a store!")

## Now we have dog(pet) AND dog(storePet)

## An Abstract Factory method is to recplace straightforward calls

class pet_factroy:
    def __init__(self, pet):
        self.pet = pet

    def __str__(self):
        return "Pet object"
    
class dog