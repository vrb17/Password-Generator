# Password-Generator
This is a random password generator which will take an integer parameter for the desired length of the password.
The generated password will be returned to the user and will consist of numbers,
special characters and both uppercase and lowercase letters depending on the length of the password.

Defining Character Sets:
- Two lists, alpha_lower and alpha_upper, are created to store lowercase and uppercase letters of the alphabet, respectively.
- The spec_chars list contains a set of special characters.

User Input:
- The code prompts the user to enter the desired length of the password.
- The input is stored in the len_pass variable and stripped of any leading or trailing whitespace.

Assigning Characters to the Password:
- Based on the value of the variable four, the code determines which character set to choose from:
    - If four is 1, a lowercase letter is selected randomly from alpha_lower 
    - If four is 2, an uppercase letter is selected randomly from alpha_upper
    - If four is 3, a random digit (0-9) is added
    - If four is 4, a special character is selected randomly from spec_chars 

