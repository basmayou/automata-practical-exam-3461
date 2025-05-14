# Automata Theory Simulators 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Automata](https://img.shields.io/badge/Contains-Turing%20Machine%20%7C%20PDA%20%7C%20DFA-FF6F00)
 
**Student**: Basma Aiman Roshdy  
**Section**: 2 

**-----------**

Three Python implementations of formal language automata:
1. **Turing Machine** for **L** = {0ⁿ1ⁿ0ⁿ1ⁿ | n ≥ 1}
2. **Pushdown Automaton (PDA)** for odd-length palindromes
3. **Regex-to-DFA Converter** (RE → NFA → Minimized DFA)

## Features

### Turing Machine Simulator
- Simulates a deterministic Turing Machine
- Visualizes tape operations step-by-step
- Handles:
  - Tape operations (read/write/move)
  - State transitions
  - Acceptance/rejection
- Interactive menu system
- Comprehensive test cases

## Turing Machine Simulator
Simulates a TM for language L = {0ⁿ1ⁿ0ⁿ1ⁿ | n ≥ 1}

#### How to Run
1. Run the Python script
2. Choose an option:
   - `1` for pre-defined examples
   - `2` to enter your own string
   - `3` to run test cases

#### Testing
- The script includes unittest test cases
- To run tests: Select option `3` or run directly with:
  ```bash
  python -m unittest script_name.py




## PDA Simulator
- Simulates a stack-based PDA
- Implements odd-length palindrome recognition
- Features:
  - Stack operations (push/pop)
  - State transitions
  - Acceptance by empty stack
- Interactive menu system
- Comprehensive test cases

#### How to Run
1. Run the Python script
2. Choose an option:
   - `1` for pre-defined examples
   - `2` to enter your own string
   - `3` to run test cases

#### Testing
- The script includes unittest test cases
- To run tests: Select option `3` or run directly with:
  ```bash
  python -m unittest script_name.py

## Regex-to-DFA Converter
- Converts regular expressions to minimized DFAs
- Implements complete conversion pipeline:
  - Regular Expression → ε-NFA
  - ε-NFA → DFA
  - DFA minimization
- Includes example patterns:
  - Union
  - Kleene star
  - Concatenation
- String acceptance testing

#### How to Run
1. Run the Python script

#### Prerequisites
```bash
pip install pyformlang
