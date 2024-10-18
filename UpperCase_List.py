# traditional - approach
fruits = ['apple','mango','orange'] 

new = [] 

for fruit in fruits: 
    new.append(fruit.upper())
    
print(new) 

# optimal - approach
fruits = ['apple','mango','orange'] 

new  = [f.upper() for f in fruits] 

print(new)

#optimal - approach --> using the if condition
fruits = ['apple','mango','pear'] 

new  = [f.upper() for f in fruits if len(f) >= 5] 

print(new)
