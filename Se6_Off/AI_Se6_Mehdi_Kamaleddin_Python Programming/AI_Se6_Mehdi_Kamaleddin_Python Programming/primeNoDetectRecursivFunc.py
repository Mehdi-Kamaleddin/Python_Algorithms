def primeDetector(numm): #parent function for taking "numm" as the number we want to detect primes from 0 to num
    primes=[]   #list for gathering primes

    def testNum(num):   #each number, from "num" to 1...==dividend
        if num>0:
            r=[]    #divisors which its remainder is 0: numbers which "num" is dividable to it
            print('-------------------------------------------------')
            print(num,'NUM:')  
            def remind(d):  #remainder function which detect the any dividables(divisors which the num's remainder to it, is 0) to the given number (num)
                print('Devisor=',d) #"d" is the any divisors, started from "num" to "1"
                if d>1: #minus 1 from num. till it is bigger than 1
                    if num % d==0:
                        r.append(d) #d is the true divisor which is appended to the list "r"
                        print(r,':list of divisors which Remainders=0')
                        d-=1    #minus 1 from num (d=d-1) : at first, "d" was equal to "num"
                    else:
                        d-=1    #minus 1 from num (d=d-1) : at first, "d" was equal to "num"
                    return remind(d) #back to the remind function to test the "d-1", as a divisor for the "num" 
                                     #the remind OUTPUT which is itself new INPUT (recursive function)
                else:   #when "d" reach to "1":
                    if len(r)==1:   #counting total "num's dividable devisors": if len(r)<=1: num only is dividable to itself
                        print(num,' is PRIME______NUM')
                        primes.append(num)  #adding num to the list of primes:)

                    return (testNum(num-1)) #when there is no other divisors for the num (d rezh to 1), it is time to go to the next number to detect and tes if it is primeness or not
                                            #the remind OUTPUT, which is testNum new INPUT
            print(primes,':Primes from number',numm,'to',num)

            return remind(num)  #for calling the "remind function" to be executed throughout "testNum function"
                                #the testNum OUTPUT, which is remind INPUT 
    return testNum(numm)    #for starting, the testNUm function by "numm"(calling testNum for being executed): the first number to test if it is prime or not (it is under controll of the primeDetetor function)
                            #the primeDetector OUTPUT, which is testNum INPUT

    
primeDetector(17)

