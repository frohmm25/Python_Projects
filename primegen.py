def isprime(x):
    quot = x-1
    while quot > 1:
        if x%quot == 0:
            return False
        else:
            quot -= 1
    if quot == 1:
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
