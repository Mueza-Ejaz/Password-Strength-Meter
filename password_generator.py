import random
import string

def generate_strong_password(length=12):
    uppercase = random.choice(string.ascii_uppercase) # ascii => American Standard Code for Information Interchange.
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*")
    
    other_chars = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=length-4))
    
    password = uppercase + lowercase + digit + special + other_chars
    return ''.join(random.sample(password, len(password)))  # Shuffle the characters
