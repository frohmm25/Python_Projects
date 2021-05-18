def isprime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def findprime(x):
    while isprime(x) == False:
        x += 1
    if isprime(x) == True:
        return x    
    
    
def genprime(x):
    while x < 10000000:
        if isprime(x)==True:
            print(findprime(x))
        x+=1
