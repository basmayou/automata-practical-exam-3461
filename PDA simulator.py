# Write a program that simulates a PDA to check if a string is accepted by a given context-free language (Palindrome (Odd Length))
# WaW^R | WbW^R -> W ∈ {a, b}*

import unittest  # For testing

# Examples of strings to test
Examples = ['b', 'aba', 'abaa', 'abba', 'abaabaaba', 'abababababa', 'aaabaaa']


def odd_length_palindrome(string):
    """ Check if string is an odd length palindrome"""
    if len(string) % 2 == 0:  # Even length is rejected
        return False

    if not all(letter in ['a', 'b'] for letter in string):
        return False

    stack = []  # Stack for PDA operations
    middle_index = len(string) // 2  # Middle index of the string
    temp_string = string  # Temporary string to manuipulate

    # Push $ to the stack, marking the start of stack
    stack.append('$')

    # Read first half of the string and push it to the stack
    for letter in temp_string[:middle_index]:
        stack.append(letter)

    # Read second half of the string and pop it from stack
    for letter in temp_string[middle_index + 1:]:
        if stack.pop() != letter:
            return False

    if stack.pop() != '$':
        return False

    return True


def handle_input(string):
    """ Handle input and return the status of the string"""
    status = odd_length_palindrome(string)
    if status:
        status = "Accepted"
    else:
        status = "Rejected"
    return f"{string} -> {status}"


class TestPDA(unittest.TestCase):

    def test_valid_strings(self):
        """ Test valid strings"""
        valid_strings = [
            "b",
            "aba",
            "abaabaaba",
            "abababababa",
            "aaabaaa",
        ]
        # Check if all valid strings are accepted
        for string in valid_strings:
            self.assertTrue(odd_length_palindrome(string),
                            f"{string} Expected: Accepted")

    def test_invalid_strings(self):
        """ Test valid strings """
        invalid_strings = [
            "abaa",
            "abba",
            "ab",
            "baa",
        ]
        # Check if all invalid strings are rejected
        for string in invalid_strings:
            self.assertFalse(odd_length_palindrome(string),
                             f"{string} Expected: Rejected")


print("\n\t---------- PDA simulator for odd length palindrome ----------")
# Get user choice
choice = input(
    "\n\tEnter 1 to see some examples or 2 to enter your own string or 3 to see test casses: "
)
# Handle user choice
if choice == '1':
    print("\n\tExamples:\n")
    for i in range(len(Examples)):
        print(f"\t{i+1}. {handle_input(Examples[i])}")
elif choice == '2':
    input_string = input("\n\tEnter your string: ")
    print(f"\n\t{handle_input(input_string)}")
elif choice == '3':
    unittest.main()
else:
    print("\n\tInvalid choice!")