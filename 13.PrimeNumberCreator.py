
def is_prime(x):
    if x>1:
        for i in range(2,x):
            if (x%i)==0:
                return False
        return True


maxNum=int(input("Enter tha max number: "))
primeList=[]
for i in range(1,maxNum+1):
    if is_prime(i)==True:
        primeList.append(i)
print(primeList)


