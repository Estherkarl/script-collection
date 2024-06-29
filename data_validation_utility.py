# Function to validate an email address
def validate_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

# Function to validate a phone number
def validate_phone_number(phone_number):
    if phone_number.isdigit() and len(phone_number) == 10:
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    # Validate email address
    email = 'example@email.com'
    if validate_email(email):
        print(f"Email '{email}' is valid.")
    else:
        print(f"Email '{email}' is not valid.")

    # Validate phone number
    phone_number = '1234567890'
    if validate_phone_number(phone_number):
        print(f"Phone number '{phone_number}' is valid.")
    else:
        print(f"Phone number '{phone_number}' is not valid.")
