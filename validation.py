import bcrypt
import re
GENERATEDSALT=b'$2b$12$h2ZRuEWUl7VvwiCOFxLHc.zaBE0XbNpEda/xqtbiZDamuWYJtPMs6'

##validate the name
def validate_name(name):
    pattern = r"^[A-Za-z\s.'-]+$"
    return bool(re.match(pattern, name))


##validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

##validate contact numbers
def validate_contact_number(number):
    pattern = r'^(0|\+)[0-9]+$'
    return bool(re.match(pattern, number))


##validate postal code
def validate_postal_code(postal_code):
    # Postal code format: XXXXX or XXXX
    pattern = r'^\d{4,5}$'
    return bool(re.match(pattern, postal_code))

##validate the password
def validate_password(password):
    # Password must be at least 6 characters long
    # Must contain at least one uppercase letter, one lowercase letter, one digit, and one special character
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
    return bool(re.match(pattern, password))



##encrypt password 
def encrypt_password(password):
    # Hash a password  with a randomly-generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),GENERATEDSALT)
    return hashed_password



def matchPassword(password,confirmPassword):
    return password==confirmPassword
        
    
    
def encrypt(password):
    encryptedpassword=encrypt_password(password)
    return encryptedpassword
