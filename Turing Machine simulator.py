# Turing machine shoud have tape, head, states, and transition function
# L = {0^n 1^n 0^n 1^n} ∈ {0, 1}*

import unittest  # For testing

Examples = ['0101', '1010', '1100', '00110011', '00110101', '000111000111', '00011110001111', '0000111100001111']


def move_right(head):
    """Move head to ritht of tape"""
    return head + 1


def move_left(head):
    """Move head to left of tape"""
    return head - 1


def print_tape(tape):
    """Print the tape content"""
    print('\tTape:', end=' ')
    for symbol in tape:
        print(symbol, end=' ')
    print()


def turing_machine(string):
    """ Check if string is in the language or not"""
    tape = list(string)  # Tape contains the string
    tape.append('B')  # Append blank symbol to the end of the tape
    head = 0  # Head start from first index of tabe

    if len(string) % 4 != 0:  # Length of string should be multiple of 4
        return False

    if not all(letter in ['0', '1'] for letter in string):  # String should be in {0, 1}
        return False

    # Transition function
    while (tape[head] != 'B'):
        # Read first 0 and write X
        if tape[head] == '0':
            tape[head] = 'X'
            head = move_right(head)
        else:
            return False
        # Skip 1's & Y's
        while tape[head] == '0' or tape[head] == 'Y':
            tape[head] = tape[head]
            head = move_right(head)
        # Read first 1 and write Y
        if tape[head] == '1':
            tape[head] = 'Y'
            head = move_right(head)
        else:
            return False
        # Skip 1's & Z's
        while tape[head] == '1' or tape[head] == 'Z':
            tape[head] = tape[head]
            head = move_right(head)
        # Read second 0 and write Z
        if tape[head] == '0':
            tape[head] = 'Z'
            head = move_right(head)
        else:
            return False
        # Skip 0's & M's
        while tape[head] == '0' or tape[head] == 'M':
            tape[head] = tape[head]
            head = move_right(head)
        # Read second 1 and write M
        if tape[head] == '1':
            tape[head] = 'M'
            head = move_left(head)
        else:
            return False
        # Skip 0's 1's Y's M's & Z's
        while tape[head] == '0' or tape[head] == '1' or tape[head] == 'Y' or tape[head] == 'Z' or tape[head] == 'M':
            tape[head] = tape[head]
            head = move_left(head)
        # Skip X
        if tape[head] == 'X':
            tape[head] = 'X'
            head = move_right(head)

        if tape[head] == '1':
            continue
        elif tape[head] == 'Y':
            while tape[head] != 'B':
                tape[head] = tape[head]
                head = move_right(head)
        # Check if head is at the end of the tape
        if tape[head] == 'B':
            return True
    return False


def turing_machine_with_steps(string):
    """ Check if string is in the language or not with steps"""
    tape = list(string)  # Tape contains the string
    tape.append('B')  # Append blank symbol to the end of the tape
    head = 0  # Head start from first index of tabe

    print_tape(tape)
    if len(string) % 4 != 0:  # Length of string should be multiple of 4
        return False

    if not all(letter in ['0', '1'] for letter in string):  # String should be in {0, 1}
        return False

    # Transition function
    while (tape[head] != 'B'):
        # Read first 0 and write X
        if tape[head] == '0':
            tape[head] = 'X'
            head = move_right(head)
            print_tape(tape)
        else:
            return False
        # Skip 1's & Y's
        while tape[head] == '0' or tape[head] == 'Y':
            tape[head] = tape[head]
            head = move_right(head)
        # Read first 1 and write Y
        if tape[head] == '1':
            tape[head] = 'Y'
            head = move_right(head)
            print_tape(tape)
        else:
            return False
        # Skip 1's & Z's
        while tape[head] == '1' or tape[head] == 'Z':
            tape[head] = tape[head]
            head = move_right(head)
        # Read second 0 and write Z
        if tape[head] == '0':
            tape[head] = 'Z'
            head = move_right(head)
            print_tape(tape)
        else:
            return False
        # Skip 0's & M's
        while tape[head] == '0' or tape[head] == 'M':
            tape[head] = tape[head]
            head = move_right(head)
        # Read second 1 and write M
        if tape[head] == '1':
            tape[head] = 'M'
            head = move_left(head)
            print_tape(tape)
        else:
            return False
        # Skip 0's 1's Y's M's & Z's
        while tape[head] == '0' or tape[head] == '1' or tape[head] == 'Y' or tape[head] == 'Z' or tape[head] == 'M':
            tape[head] = tape[head]
            head = move_left(head)
        # Skip X
        if tape[head] == 'X':
            tape[head] = 'X'
            head = move_right(head)

        if tape[head] == '1':
            continue
        elif tape[head] == 'Y':
            while tape[head] != 'B':
                tape[head] = tape[head]
                head = move_right(head)
        # Check if head is at the end of the tape
        if tape[head] == 'B':
            return True
    return False


def handle_input(string):
    """ Handle input and return the status of the string"""
    print(f"\n\tString: {string}\n\n\tTuring machine steps:")
    status = turing_machine_with_steps(string)
    # Get the status of the string
    if status:
        status = "Accepted"
    else:
        status = "Rejected"
    return f"\n\t{string} -> {status}"


class TestTuringMachine(unittest.TestCase):
    def test_valid_strings(self):
        """ Test valid strings"""
        valid_strings = [
            "0101",
            "00110011",
            "0000111100001111",
            "000111000111",
        ]
        # Check if all valid strings are accepted
        for string in valid_strings:
            self.assertTrue(turing_machine(string), f"{string} Expected: Accepted")

    def test_invalid_strings(self):
        """ Test valid strings """
        invalid_strings = [
            "1010",
            "00110101",
            "00011110001111"
            "101010101"
        ]
        # Check if all invalid strings are rejected
        for string in invalid_strings:
            self.assertFalse(turing_machine(string), f"{string} Expected: Rejected")


print("\n\t---------- Turing Machine simulator for {0^n 1^n 0^n 1^n} ----------")
# Get user choice
choice = input("\n\tEnter 1 to see some examples or 2 to enter your own string or 3 to see test casses: ")
# Handle user choice
if choice == '1':
    print("\n\tExamples:\n")
    for i in range(len(Examples)):
        print(f"\t{handle_input(Examples[i])}\n")
        print("\t----------\n")
elif choice == '2':
    input_string = input("\n\tEnter your string: ")
    print(f"\n\t{handle_input(input_string)}")
elif choice == '3':
    unittest.main()
else:
    print("\n\tInvalid choice!")