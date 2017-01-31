#
# print "Problem 1: Output if number is positive, negative, or zero."
# number = long(raw_input("Input a number:"))
# if number < 0:
#     outcome = "negative"
# elif number == 0:
#     outcome = "zero"
# else:
#     outcome = "positive"
# print ("The inputted number is " + outcome + ".")
#
# #-------------------------------------------------------------------#
#
# print "Problem 2: Output if which number is bigger."
# first = long(raw_input("Input first number:"))
# second = long(raw_input("Input second number:"))
# if first > second:
#     outcome = "First is larger"
# elif first == second:
#     outcome = "They are equal"
# else:
#     outcome = "Second is larger"
# print (outcome)
# #-------------------------------------------------------------------#
#
# print "Problem 3: Compute sum from input number down to 0."
# number = long(raw_input("Input number:"))
# sum=0
# if number < 0:
#     print "That number is negative, sorry!"
# else:
#     while number > 0:
#         sum+=number
#         number-=1
#     print ("The sum is " + str(sum))
#
#
# #-------------------------------------------------------------------#
#
# print "Problem 4: Compute factorial of a number."
# number = long(raw_input("Input number:"))
# if number < 0:
#     print "That number is negative, sorry!"
# else:
#     factorial=1
#     while number > 0:
#         factorial*=number
#         number-=1
#     print ("The factorial is " + str(factorial))

#-------------------------------------------------------------------#
#
# print "Problem 5: Compute divisors of a number."
# number = int(raw_input("Input number:"))
# if number < 0:
#     print "That number is negative, sorry!"
# else:
#     divs=[]
#     div=number-1
#     while div > 0:
#         if number%div==0:
#             divs.append(div)
#         div-=1
#     print ("The divisors are " + str(divs))
#
#
# #-------------------------------------------------------------------#
#
# print "Problem 6: Compute greatest common divisors of 2 numbers."
# first = int(raw_input("Input first number:"))
# second = int(raw_input("Input second number:"))
# if (first or second) < 0:
#     print "One of those numbers is negative, sorry!"
# else:
#     divs_1=[]
#     divs_2=[]
#     div_1=first-1
#     div_2=second-1
#     while div_1 > 0:
#         if first % div_1 == 0:
#             divs_1.append(div_1)
#         div_1 -= 1
#     while div_2 > 0:
#         if second % div_2 == 0:
#             divs_2.append(div_2)
#         div_2 -= 1
#     for d in divs_1:
#         print "d is " +str(d)
#         if d in divs_2:
#             ans=d
#             break
#     print ("The greatest common divisor is: " + str(ans))
#
#

#-------------------------------------------------------------------#
#
# print "Problem 7: Compute the least common multiple of 2 numbers."
# first = int(raw_input("Input first number:"))
# second = int(raw_input("Input second number:"))
# if (first or second) < 0:
#     print "One of those numbers is negative, sorry!"
# else:
#     max=first*second
#     divs = []
#     div=max
#     while div > 0:
#         if max%div==0:
#             divs.append(div)
#         div-=1
#     divs.sort()
#     #print "divs is: " + str(divs)
#     for i in divs:
#         if ((i%first==0) and (i%second==0)):
#             lcm=i
#             break
#     divs.reverse()
#     if i==divs[0]:
#         lcm=i
#     print "The least common multiple of "+str(first)+" and "+str(second)+ " is " + str(lcm)

#-------------------------------------------------------------------#
#
# #inp = raw_input()
# inp="8"
# while inp != "":
#     print "Problem 8: Determine if number is prime."
#     number = int(raw_input("Input number:"))
#     if number < 0:
#         print "Number is negative, sorry!"
#     else:
#         result="Yes, its prime"
#         for i in range(number):
#             if (i==0) or (i==1) or (i==number):
#                 continue
#             if number%i==0:
#                 result="Not a prime"
#                 break
#         print result
#     inp = "y"

#----------------------------------make list of primes

#inp = raw_input()
#
# print "Problem 8: Print all primes up to a max number."
# number = int(raw_input("Input number:"))
# if number < 0:
#     print "Number is negative, sorry!"
# else:
#     primes=[]
#     for n in range(number+1):
#         #print n
#         for i in range(n+1):
#             #print i
#             if (i==0) or (i==1):
#                 continue
#             if (n == i):
#                 #print "appending " + str(n)
#                 primes.append(n)
#             if n%i==0:
#                 break
#
#     print "Prime numbers up to " +str(number) + " are " + str(primes)

    # ----------------------------------series

    # inp = raw_input()

print "Problem 9: Calculate number in series."
number = int(raw_input("Input number:"))
if number < 0:
    print "Number is negative, sorry!"
else:
    a=0
    for i in range(number+1):
        if i == 0:
            a= 1
        else:
            a=(2*a)+1
    print "a in series is : " + str(a)


 # ----------------------------------solve equation
    # (a + (b - c) * d - e) * f = 75`
#where a, b, c, d, e, and f are unique integers in the range [1, 6]