def email_slicer(email_address):
    """Function which takes email and slices it."""
    username = email[:email.index("@")]
    domain_name = email[email.index("@")+1:]

    final_output = f"Username is {username} and domain name is {domain_name}"
    return final_output


email = input("Enter your email address: ").strip()
print(email_slicer(email))
