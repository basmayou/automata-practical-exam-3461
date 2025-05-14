# Write a program that implement function that takes a regular expression as input and converts it into a DFA. Then simulate the DFA on a list of input strings.
# RE -> NFA, NFA -> DFA

from pyformlang.regular_expression import Regex


# Examples of regular expressions and their corresponding strings
Examples = {'a|b': ['a','bb'],
            'a*': ['aaa','b'],
            'b(b*)': ['', 'bb']}

def simulate_DFA(dfa,string):
  """Simulate DFA"""
  return dfa.accepts(string)

for regex, strings in Examples.items():
    print(f"\nRegex: {regex}")
    # RE -> NFA
    regex = Regex(regex)
    nfa = regex.to_epsilon_nfa()
    # NFA -> DFA
    dfa = nfa.to_deterministic().minimize()
    # Simulate DFA
    for string in strings:
        print(f"String: {string.ljust(10)}-> {'Accepted' if simulate_DFA(dfa,string) else 'Rejected'}")