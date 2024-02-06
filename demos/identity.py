def valid_illinois_domain(user_email, raise_exc=False):
    valid_domains = ['uillinois.edu', 'illinois.edu', 'uic.edu', 'uis.edu']
    user_domain = user_email.split('@')[1]
    
    result = user_domain in valid_domains
    
    if raise_exc:
        if result == False:
            raise ValueError(f"Email '{user_email}' has an invalid domain.")
    
    return result


def register(first_name, last_name, email):
    if valid_illinois_domain(email):
        # Code to register new user...
        
        return f"registered new user: {first_name} {last_name}, email: {email}."
    else:
        return "registration failed"