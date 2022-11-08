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

# while(True):
#     line = input("type something: ")
#     if(line.lower() == 'q'):
#         break
#     print(f"you typed {line}")

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number * 3)

# total = 0
# for number in numbers:
#     total = total + number
# print(total)

# chickens = ['Margaret', "Hetty", "Henrietta", "Audrey", "Mabel"]
# for chicken in chickens:
#     print(chicken)

chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]

for chicken in chickens:
    print(f'{chicken["name"]} is {chicken["age"]}')