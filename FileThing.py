'''
This program is meant to analyze a file that has numbers on each line. It will then tell you how many numbers
are in the file, and the lowest and highest number in the file.
'''
# Durango Dodge
# 03/27/2023
# Written in VSCode

# Get the integer from every line and add it to the list of numbers
nums = []
for line in open('Numbers-1.txt'):
    nums.append(int(line))

# Go through the list of numbers and print them out.
print("Printing all numbers in file: ")
for i in nums:
    print(i)

# Sort the list then print the the amount of Numbers in the Array, and the logical highest and lowest numbers.
nums.sort()
print("\nNumber of Numbers: " + str(len(nums)))
print("Lowest Num: " + str(nums[0]))
print("Highest Num: " + str(nums[len(nums)-1]))

'''
By doing this project I learned how to open and use lines in a file.
'''