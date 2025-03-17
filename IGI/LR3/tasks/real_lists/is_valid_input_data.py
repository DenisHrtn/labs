from tasks.decors.log_function_call import log_function_call


@log_function_call
def is_valid_input_data(input_data: str) -> bool:
    """
    Check if the input value is a valid float number.
    """
    try:
        float(input_data)  # Attempt to convert the value to a float
        return True
    except ValueError:
        return False
