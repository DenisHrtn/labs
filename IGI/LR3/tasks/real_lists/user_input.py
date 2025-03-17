from tasks.decors.log_function_call import log_function_call
from tasks.real_lists.is_valid_input_data import is_valid_input_data


@log_function_call
def get_user_input() -> list:
    """
    Get a list of numbers from the user.
    """
    user_input = input("Enter the list elements separated by spaces: ")
    input_list = user_input.split()
    float_list = []

    for value in input_list:
        if is_valid_input_data(value):
            float_list.append(float(value))
        else:
            raise KeyboardInterrupt(f"'{value}' is not a valid number.")

    return float_list
