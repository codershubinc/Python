# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).


species = 'Dog'
age = 2
 
if species == 'Dog' and age < 2:
    print('Puppy food')
elif species == 'Cat' and age > 5:
    print('Senior cat food')
else:
    print('generic food')