import re


def is_valid_email(email: str) -> bool:
    if not email or " " in email:
        return False

    # Basic length check
    if len(email) > 254:
        return False

    # Regex covering most real-world rules
    pattern = r"""
        ^[a-zA-Z0-9]+            # start with alphanumeric
        ([._%+-]?[a-zA-Z0-9]+)*  # allowed special chars
        @
        [a-zA-Z0-9]+             # domain start
        (-?[a-zA-Z0-9]+)*        # optional hyphens
        (\.[a-zA-Z]{2,})+$       # top-level domain
    """

    return re.match(pattern, email, re.VERBOSE) is not None


email_id = input("Enter the mail id:- ")
print(is_valid_email(email_id))
