#Fibonacci Series in Recursion

def fibo(n):
    if(n<=1):
        return(n) #Check for the condition it true return the number itself
    else:
        return(fibo(n-1)+fibo(n-2))
n=int(input("Enter the number to find its series"))
#Get user input for the number
print("Fibonacci Series is")
for i in range(n):
    print(fibo(i))
    
