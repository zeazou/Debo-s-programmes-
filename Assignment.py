# #question1 - Mean

# numbers_list = [1, 2, 3,4,5]

# mean = sum(numbers_list) / len(numbers_list)


# print(mean)



# question 2 - Median 

# n_num = [1, 2, 3, 4, 5]
# n = len(n_num)
# n_num.sort()
  
# if n % 2 == 0:
#     median1 = n_num[n//2]
#     median2 = n_num[n//2 - 1]
#     median = (median1 + median2)/2
# else:
#     median = n_num[n//2]
# print("Median is: " + str(median))


#Question 3 - Variance 

# def variance(data):
#   n = len(data)
#   mean = sum(data) / n
#   deviations = [(x - mean) ** 2 for x in data]
#   variance = sum(deviations) / n
#   return variance


#question 4 - standard deviation 

# def get_std_dev(data):
#     n = len(data)
#     mean = sum(data) / n
#     var = sum((x - mean)**2 for x in data) / n
#     std_dev = var ** 0.5
#     return std_dev


#question 5 - Skewness

 