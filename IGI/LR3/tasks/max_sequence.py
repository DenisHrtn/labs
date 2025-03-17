from tasks.decors.log_function_call import log_function_call


@log_function_call
def find_max_sequence():
    """
    Function to find the maximum number in a sequence of integers in real-time.
    The sequence ends when the user inputs the number 1.
    """
    max_number = None

    print("Enter numbers (input 1 to stop):")
    while True:
        try:
            num = int(input())
            if num == 1:
                break
            if max_number is None or num > max_number:
                max_number = num
            print(f"Current maximum: {max_number}")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"Final maximum number: {max_number}")
    return max_number


if __name__ == "__main__":
    find_max_sequence()