
# # # # # # def factorial(n):
# # # # # #     if n ==1:
# # # # # #         return 1
# # # # # #     if n == 0:
# # # # # #         return 1 
# # # # # #     recurse = n * factorial(n-1)  
# # # # # #     print(recurse) 
# # # # # #     return recurse


# # # # # # factorial(5) 




# # # # # print("x")
# # # # # if  4>5:

# # # # #       print(7)
# # # # # print(4)


# # # # print("boy")
# # # # if 4>5:
# # # #     print(7)


# # # # else:
# # # #     print(8)



# # # score = int(input("Enter your exam score:\n:>"))

# # # if score <= 100:
# # #     if score >= 90:
# # #         print('A')
# # #     elif score >= 80: 
# # #         print("B")
# # #     elif score >= 70:
# # #           print("C")
# # #     elif score >= 60:
# # #          print ("D")
# # #     elif score >= 50:
# # #          print ("E") 
# # #     elif score >= 40:
# # #         print ("F")   
# # # else : 
# # #      print("Comrade go learn work.")           




# # my_str = "this is a lovely string"
# # a = list(map(lambda f:f.upper(),my_str))

# # print("".join(a))


# print("Guess the computer's choice to win the prize ")
# a=[1,2,3,4,5,6,7]
# print("select a number from",)








# import random


# options = ["r", "p","s"]
# print("""Select R for rock, P for paper and S FOR scissors.""")
# com_choice = random.choice(options)
# player_choice = input(">").lower
# if player_choice in options:
#     if player_choice == options(0) and 
#     com_choice == options  [2]:
#     print("You Win")
#     print("Computer Choose", com_choice)
#     com_choice == options[1]
#     print("You Win")
#     print("Computer choose",com_choice)
#     elif player_choice == options[2] and 
#     com_choice==options[1]
#          print("You win")
#          print("Computer choose",com_choice)
#     elif player_choice == options{1} and 
#     com_choice==options[0]:
#         print("You win")
#         print("Computer choose", com_choice)
#     elif player_choice==com_choice
#          print("its a tie")     

#     else:
#         print("You lose") 
#         print('Computer choose',com_choice.title())

















# for i in range (10):
#     if i == 5:
#        # break
#         continue
#     print(i)










# a = 0
    
# for i in range (90-120):
#     if i%2==1:
#             a+=1
#             print(i)
# print(" ")
# print(a)
# print(" ")        





# def is_prime(x):
#     list_n = range(2,x)

#     if x <= 1:
#         return False
#     elif x-1>2:
#         for n in range(len(list_n)):
#             list_n[n] = x % list_n[n]
#         for n in list_n:
#             if n == 0:
#                 return False
#         for n in list_n:
#             if n > 0:
#                 return True
#     else:
#         return True





num = int(input("Please enter a number to check if its prime : "))

def primeNumber():
    if (num <= 1):
        return False

    for i in range(2,num):
        if(num % i == 0):
            return False

    return True

if (primeNumber() == True):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")




    