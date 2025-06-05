def lambda_handler(event, context):
    """
    Sample validator Lambda function.
    """
    input_value = event.get("input", "")
    is_valid = isinstance(input_value, str) and len(input_value) > 3

    return {
        "input": input_value,
        "is_valid": is_valid,
        "message": "Valid input" if is_valid else "Invalid input"
    }
