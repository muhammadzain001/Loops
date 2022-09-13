# While loops

counter=1
while counter <3:
    print("yahhhhhhhhhh")
    counter += 1

num = 10
while num != 0:
    print(num)
    num -= 1


pos_int = int(input("Please enter a positive integer."))
int_init = pos_int
summed = 0
while pos_int > 0:
    summed += pos_int
    pos_int -= 1
print(int_init)
print(summed)

print("-------------------------------------------------------------------------------------")
# For Loops
# For performing a fixed number of iterations the for loop is particularly useful because it is a type
# of loop that is controlled by the length of the ignorable piece of data that it is being used on rather
# than a condition.

word = "muhammad zain asad"
for letter in word:
    print(letter)

word1 = "hello world"
for letter in word1:
    print(letter)
# --------------------------------------------------------------------------------------
user_str = input("Please enter a string.")
count = 0
for char in user_str:
    count += 1
print(user_str)
print(count)
print("------------------------------------------------------------------------------ ")
# Range
input_one = range(5)
for num in input_one:
    print(num)