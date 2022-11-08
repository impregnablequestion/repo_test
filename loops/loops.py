# While Loop

# counter = 0
# my_number = 5

# while(counter <= my_number):
#     print(f'counter is {counter}')
#     counter += 1 
    # or counter = counter + 1

# my_number = 5
# value = int(input("What number am I thinking of? "))

# while(value) != my_number:
#     value = int(input("Tough luck, try again "))

# print("yeah well done!")

while(True):
    line = input("type something: ")
    if(line.lower() == 'q'):
        break
    print(f"you typed {line}")

