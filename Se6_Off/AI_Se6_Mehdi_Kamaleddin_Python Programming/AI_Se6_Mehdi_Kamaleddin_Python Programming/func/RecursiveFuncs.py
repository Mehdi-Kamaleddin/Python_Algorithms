###calcyulating the n fibonacci number series

#fibonacci=0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci(n:int)->int:
    if n ==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    


def factorial(n: int)-> int:
    if not isinstance(n, int):
        print("Factorial only operates if n is an int input")
    elif n<0:
        print("Factorial operates on only positive numbers") 
    elif n==0:
        return 1
    else:
        return n * factorial(n-1)



# n=0
# x=6
# total=1
# while n <x:
#     total=total*(x-n)
#     n+=1

# print(total)

