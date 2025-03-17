from tasks.decors.log_function_call import log_function_call
from tasks.real_lists.user_input import get_user_input
from tasks.real_lists.process_list import print_list, process_list


@log_function_call
def main() -> None:
    """Main function to run the program."""
    try:
        lst = get_user_input()
        print_list(lst)

        odd_negative_count, sum_before_zero = process_list(lst)

        print(f"Number of odd negative elements: {odd_negative_count}")
        print(f"Sum of elements before the last zero: {sum_before_zero}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()