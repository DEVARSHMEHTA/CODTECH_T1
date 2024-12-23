import re
import pyfiglet
from termcolor import colored

def create_banner(style="slant"):
    # Create the banner text
    banner_text = "Password Strength Checker"
    # Use pyfiglet to create the banner with the chosen style
    banner = pyfiglet.figlet_format(banner_text, font=style)
    
    # Print the banner with dark blue color.
    print(colored(banner, "blue"))
    print(colored("****By Devarsh Mehta****", "blue"))

# Call the function to create the banner with the chosen style
create_banner("slant")  # Example style: "slant"

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 12
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^?.]', password))
    
    # Score Calculation
    score = 0
    if length_criteria:
        score += 2
    if lowercase_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 2
    
    # Feedback on password strength
    if score >= 7:
        return "strong", "Strong Password - Great job!"
    elif 5 <= score < 7:
        return "moderate", "Moderate Password - Consider adding more special characters or numbers."
    else:
        return "weak", "Weak Password - Use a longer password with uppercase, lowercase, digits, and special characters."

if __name__ == "__main__":
    default_passwords = ["hacker", "admin", "admin123", "admin@123", "admin.123"]

    while True:
        password = input("Enter your password (or 'exit' to quit): ")
        if password.lower() == 'exit':
            break

        if password in default_passwords:
            print(colored("This is a Default password. It is easily crackable. Use a high security password. Thank you.", "red"))
        else:
            strength, feedback = check_password_strength(password)
            if strength == "strong":
                print(colored("Feedback: " + feedback, "yellow"))
            elif strength == "moderate":
                print(colored("Feedback: " + feedback, "green"))
            else:
                print(colored("Feedback: " + feedback, "red"))
