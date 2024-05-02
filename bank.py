def get_user_choice(choices, prompt="Please enter your choice: "):
    """
    Presents a list of choices to the user and validates their input.

    Args:
        choices (list): A list of valid choices the user can select.
        prompt (str, optional): The prompt to display to the user. Defaults to "Please enter your choice: ".

    Returns:
        str: The valid choice selected by the user.
    """

    while True:
        user_input = input(prompt).lower().strip()  # Get sanitized input

        if user_input in choices:
            return user_input
        else:
            print(f"Invalid choice. Please select one of the following: {', '.join(choices)}")

# Example usage

choices = ["apple", "banana", "orange"]
print(choices)
user_choice = get_user_choice(choices, "What fruit do you prefer? ")
print(f"You selected: {user_choice}")
