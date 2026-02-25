
def password_check():
    while True:
        password = input("Enter the password to check:")

        if len(password) < 8:
            print("length must be > 8")
            continue

        has_digit = False
        has_upper = False

        for ch in password:
            if ch.isdigit():
                has_digit = True
            if ch.isupper():
                has_upper = True

        if not has_digit:
            print("Password must contain at least one digit")   
            continue 

        if not has_upper:
            print("Password must contain at least one uppercase letter")
            continue

        print("Password is strong ✅")
        break

password_check()