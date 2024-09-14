hat_list = [1, 2, 3, 4, 5]

user_input = int(input("Input Number: "))
middle_number = user_input
hat_list[2] = middle_number

del hat_list[4]

print("\nList's length:", len(hat_list))
print(hat_list)
