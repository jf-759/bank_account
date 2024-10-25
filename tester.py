# Created the Dog class
class Dog:
    pass

# Instatiation
jess_dog = Dog()

# TODO: Create an instance of Dog and assign it to a variable


# Create attributes for jess_dog object, using dot notation.
# Like variables, if attribute did not exist, it is created when you first assign it a value.

jess_dog.name = "Tara"
jess_dog.age = 1
jess_dog.color = "brown"
jess_dog.cuteness_level = 10

# TODO: Add four attrbutes to your dog instance. Give each a value that describes your dog.


# Update attributes similar to how you would update a variable.

jess_dog.age += 1
print(f"My age is {jess_dog.age}")

# TODO: Update the some of the attributes of your dog instance. Assign a new value 
# to one of the existing attributes of your dog. 


# The name attribute 
print(f"My name is {jess_dog.name}")

# TODO: Print one or more of your dog's attributes:


# Delete a property from an object with del

del jess_dog.name
print(f"My name is {jess_dog.age}")

# TODO: Delete one of the attributes of your dog. 


# Rather than having to print all of the attributes one by one, we can use __dict__
print(jess_dog.__dict__)

# TODO: Check the attrbutes of your dog by printing yourdog.__dict__. This should 
# show you all of the attribues that exist on your dog. 
