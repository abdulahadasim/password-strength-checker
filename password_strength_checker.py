def password_strength(password):
    password_points = 0
    lower_case_points = 0
    upper_case_points = 0
    number_points = 0
    special_character_points = 0

    upper_case_multiplier = 0.5
    lower_case_multiiplier = 1
    number_multiplier = 2
    special_character_multiplier = 3

    special_charactes = set(["!", '"', "#", "$", "%", "&", "'", "(", 
                            ")", "*", "+", ",", "-", ".", "/", ":", 
                            ";", "<", "=", ">", "?", "@", "[", "\\", 
                            "]", "^", "_", "`", "{", "|", "}", "~"])
    
    strength = ""
    if len(password) <= 4:
        strength = "Weak"
        return strength
    elif len(password) <= 8:
        password_points += 3
    elif len(password) <= 12:
        password_points += 4
    else:
        password_points += 6

    for char in password:
        if 'a' <= char <= 'z':
            lower_case_points += 1
        elif 'A' <= char <= 'Z':
            upper_case_points += 1
        elif char.isdigit:
            number_points += 1
        elif char in special_charactes:
            special_character_points += 1

    if upper_case_points > 0:
        password_points += 5
    elif number_points > 0:
        password_points += 7
    elif special_character_points > 0:
        password_points += 10
    
    password_points += (lower_case_points * lower_case_multiiplier + upper_case_points * upper_case_multiplier + 
                        number_points * number_multiplier + special_character_points + special_character_multiplier)

    if password_points <= 25:
        strength = "Very Weak"
    elif password_points <= 35:
        strength = "Weak"
    elif password_points <= 45:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength
     
input_password = input("Enter a password\n")
strength = password_strength(input_password)
print("Your password strength is " + strength + "!")
