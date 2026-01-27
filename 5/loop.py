import random

student_scores = [156, 89, 134, 67, 198, 45, 123, 78, 167, 92, 145, 56, 189, 34, 112, 87, 176, 23, 134, 98]

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

sum = 0

for number in range(1,101):
    sum += number

print(sum)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', 
           '+', '=', '[', ']', '{', '}', '|', ':', ';', '<', '>', 
           ',', '.', '?', '/']

num_letters = int(input("How many letters?"))

num_numbers = int(input("How many numbers?"))

num_symbols = int(input("How many symbols?"))

# first get the list of letters,num,sym randomly
letter_list = []
for i in range(0, num_letters):
    index = int(random.random() * len(letters))
    letter_list.append(letters[index])   
print(letter_list)

number_list = []
for i in range(0, num_numbers):
    index = int(random.random() * len(numbers))
    number_list.append(numbers[index])   
print(number_list)

symbol_list = []
for i in range(0, num_symbols):
    index = int(random.random() * len(symbols))
    symbol_list.append(symbols[index])   
print(symbol_list)

# combine everything into a list
combined_list = letter_list + number_list + symbol_list
print(combined_list)

# randomly extract information out
generated_list = []

# pick item, add in list, then remove item
for i in range(0,len(combined_list)):
    index = int(random.random() * len(combined_list))
    generated_list.append(combined_list[index])
    combined_list.pop(index)

print(generated_list)

pw_string = ''
for i in range(0,len(generated_list)):
    pw_string += generated_list[i]

print(f"Password is : {pw_string}")