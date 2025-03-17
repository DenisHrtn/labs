from tasks.decors.log_function_call import log_function_call


@log_function_call
def process_list(lst: list) -> tuple:
    """
    Process the list to find odd negative numbers and sum elements before the last zero.
    """
    odd_negative_count = 0
    sum_before_zero = 0
    found_zero = False

    for index, num in enumerate(lst):
        # Count odd negative numbers
        if num < 0 and num % 2 != 0:
            odd_negative_count += 1
        # Sum elements before the last zero
        if num == 0:
            found_zero = True
            break
        if not found_zero:
            sum_before_zero += num

    return odd_negative_count, sum_before_zero


@log_function_call
def print_list(lst: list) -> None:
    """Print the list elements."""
    print("The list you entered is:", lst)
