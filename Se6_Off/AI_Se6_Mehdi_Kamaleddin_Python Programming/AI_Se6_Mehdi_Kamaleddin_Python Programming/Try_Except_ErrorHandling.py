# while True:
#     num1=input('first number: ')
#     if num1=='q':
#         break
#     num2=input('second number: ')
#     if num2=='q':
#         break
#     else:
#         division=int(num1)/int(num2)
#         print(division)
        
        
        
while True:
    num1=input('first number: ')
    if num1=='q':
        break
    num2=input('second number: ')
    if num2=='q':
        break
    try:
        division=int(num1)/int(num2)
    except ZeroDivisionError:
        print("zero can NOT be dividable")
        
    except ValueError:
        print(' please input an intiger value not string!!!')
    else:
        print(division)