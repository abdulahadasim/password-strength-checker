# Password Strength Checker

This program checks how strong a given password is by checking factors like its length and if there are uppercase and lowercase letters, digits, and special characters. It then gives a score to the password and sorts it into one of four strength categories: **Very Weak**, **Weak**, **Strong**, or **Very Strong**.

## What this program does:

- **Assesses password strength** based on character types and it's length.
- **Classifies** the password into one of four categories: "Very Weak", "Weak", "Strong", or "Very Strong".
- **Outputs the Strength** of the password based on its characteristics.

## How to run the program:

1. **Prerequisites:**

   - This program is written in **Python 3**.
   - No extra libraries are needed to run it.

2. **Steps to run the program:**

   - Have **Python 3** installed on your machine.
   - Open a terminal or command prompt.
   - Go to the directory where you saved the script.
   - Run the program with the command below:

     ```
     python password_strength_checker.py
     ```

3. **Input:**
   - You’ll be asked to enter a password.
   - After you enter it, the program will check the password and show you its strength category.

## Dependencies:

- The only requirement is **Python 3**. No external libraries are used.

## Limitations:

- **Password Evaluation:** This program only evaluates password strength based on a very small set of rules. While it can give you a general idea of how strong your password is, it doesn't guarantee security. It doesn’t check if the password has been exposed in something like a data breach, for instance.
- **False Sense of Security:** The program is designed for educational purposes, so it shouldn't be used as a reliable tool to check how secure a password is.
- **Limited Evaluation Criteria:** It focuses on password length and character types (uppercase, lowercase, numbers, and special characters) but doesn't assess other important factors like password randomness or resistance to attacks like brute force or dictionary attacks.

## Ethical Considerations & Responsible Use:

1. **Educational Purpose:** The tool is meant to help users understand what makes a password strong. It’s not a comprehensive security measure, so don’t rely on it alone to check how secure the password is.
2. **Misuse Potential:**

   - **False Confidence:** The tool might give users a false sense of security. For example, a password labeled "Strong" by the program could still be weak because the tool doesn’t account for vulnerabilities like common password patterns or previously exposed passwords.

3. **Data Privacy:** The program doesn’t store or share any data. However, always avoid entering sensitive or real passwords into non-secure tools or platforms as good practice.

4. **Avoid Overreliance on Simple Criteria:** While this program checks basic password strength based on length and character variety, it doesn’t account for more advanced techniques like brute force or rainbow table attacks. For better protection, combine strong passwords with multi-factor authentication (MFA).

## License:

This project is licensed under The Unlicense. See the [UNLICENSE](UNLICENSE) file for details.
