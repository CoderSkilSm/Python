# sort based on modulo 10

ls = [38,19,22] 

def condition(num): 
    return num  % 10 
    
ls.sort(key = condition) 
print(ls)

# another approach --> using lambda function
ls = [38,19,22] 

ls.sort(key = lambda n:n%10)

print(ls)
