# an inelegant solution from an elegant man

# this was my solution:
def get_first_and_last_digits():
    current_number = ""
    array_of_values = []

    with open('input.txt', 'r') as provided_text:
        for string in provided_text:
            for i in string:
                if i.isdigit():
                    current_number += i
                if len(current_number) > 2:
                    first_char = current_number[0]
                    second_char = current_number[-1]
                    current_number = first_char + second_char
                if len(current_number) == 1:
                    first_char = current_number[0]
                    second_char = current_number[0]
                    current_number = first_char + second_char
            array_of_values.append(current_number)
            current_number = ""

        return array_of_values
    
def calc_sum(data_array):
    int_values = [int(value) for value in data_array]
    return sum(int_values)
    
number_list = get_first_and_last_digits()
result = calc_sum(number_list)

print(result)


# I asked chat GPT to improve the solution:
def get_first_and_last_digits(filename='input.txt'):
    array_of_values = []

    with open(filename, 'r') as provided_text:
        for line in provided_text:
            current_number = ""
            for char in line:
                if char.isdigit():
                    current_number += char

                # Check if current_number has at least 2 digits
                if len(current_number) > 1:
                    # Extract the first and last digits
                    first_char = current_number[0]
                    second_char = current_number[-1]
                    current_number = first_char + second_char

            # If there's only one digit, duplicate it
            if len(current_number) == 1:
                current_number *= 2

            array_of_values.append(current_number)

    return array_of_values

def calc_sum(data_array):
    int_values = [int(value) for value in data_array]
    return sum(int_values)

# Use default filename or provide a specific one if needed
number_list = get_first_and_last_digits()
result = calc_sum(number_list)

print(result)
