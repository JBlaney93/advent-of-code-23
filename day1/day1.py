# an inelegant solution from an elegant man

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