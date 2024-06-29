 import re

def checkpwd(pwd):
    score = 0
    feedbck = []

    if len(pwd) >= 8:
        score += 1
    else:
        feedbck.append("Password must be at least 8 characters long.")

    if re.search(r'[A-Z]', pwd):
        score += 1
    else:
        feedbck.append("Password must contain at least one uppercase letter.")

    if re.search(r'[a-z]', pwd):
        score += 1
    else:
        feedbck.append("Password must contain at least one lowercase letter.")

    if re.search(r'[0-9]', pwd):
        score += 1
    else:
        feedbck.append("Password must contain at least one digit.")

    if re.search(r'[@$!%*?^<>&#]', pwd):
        score += 1
    else:
        feedbck.append("Password must contain at least one special character(@, $, !, %, *, ?, &, #,^,<,>).")

    if score == 5:
        strength = "Very Strong !!!!"
    elif score == 4:
        strength = "Strong !!!"
    elif score == 3:
        strength = "Moderate !!"
    else:
        strength = "Weak "

    return strength, feedbck

if __name__ == "__main__":
    passwd = input("Enter your password: ")
    strength, feedback = checkpwd(passwd)
    print(f"Password Strength: {strength}")
    for msg in feedback:
        print(msg)
   
