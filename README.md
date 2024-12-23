# CODTECH_T1
# Password Strength Checker

## Author

- **Devarsh Mehta**

## Overview

A Python-based tool to evaluate password strength using various criteria like length, complexity, and the presence of special characters. It also checks against common default passwords and provides actionable feedback to enhance password security.

## Features

- Evaluates password length (minimum 12 characters for strong passwords).
- Checks for digits, uppercase, and lowercase letters.
- Verifies the inclusion of special characters.
- Warns if the password matches common defaults.
- Provides feedback to improve password strength.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DEVARSHMEHTA/CODTECH_T1.git
   cd CODTECH_T1
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Tool**:
   ```bash
   python3 Pass.py
   ```

## Usage

1. Run the script and input your password.
2. Receive an evaluation of its strength and suggestions for improvement.
3. Type 'exit' to quit.

## Example Output
(https://github.com/user-attachments/assets/0e48f6e7-3258-4d10-8497-0c6770709fbc)


### Strong Password Example
```plaintext
Enter your password (or 'exit' to quit): My$ecureP@ssw0rd
Feedback: Strong Password - Great job!
```

### Default Password Warning
```plaintext
Enter your password (or 'exit' to quit): admin123
This is a Default password. It is easily crackable. Use a high-security password. Thank you.
```

### Weak Password Feedback
```plaintext
Enter your password (or 'exit' to quit): pass
Feedback: Weak Password - Use a longer password with uppercase, lowercase, digits, and special characters.
```

## License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## Acknowledgments

- [pyfiglet](https://github.com/pwaller/pyfiglet): ASCII art generation
- [termcolor](https://pypi.org/project/termcolor/): Colored terminal text

