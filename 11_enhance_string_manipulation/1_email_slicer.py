# WAP to demo for the Email Slicer
def email_slicer(email):
    # check if the email contains '@' or not
    if "@" in email:
        indexing = email.index("@")
        userName = email[:indexing]
        domain = email[(indexing+1):]
        return userName, domain

    else:
        return "Invalid email ", "Invalid Domain"


email = input("Enter your email address: ")
userName, domain = email_slicer(email)
print(f"Username:- {userName}, Domain:- {domain}")
