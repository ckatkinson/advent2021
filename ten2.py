from collections import deque

def get_input(file):
    with open(file) as f:
        return [line[:-1] for line in f]


openingSymbols = ["(", "[", "{", "<"]
closingSymbols = [")", "]", "}", ">"]


def match(s):
    if s == "(":
        return ")"
    elif s == "[":
        return "]"
    elif s == "{":
        return "}"
    elif s == "<":
        return ">"
    else:
        raise RuntimeError(f"Input {s} is not one of the accepted symbols")

def reduce(word):
    stack = []
    for symbol in word:
        if symbol in openingSymbols:
            stack.append(symbol)
        else: 
            try:
                last = stack.pop()
                if match(last) == symbol:
                    continue
                else:
                    stack.append(last)
                    stack.append(symbol)
            except IndexError:
                return None
    return ''.join(stack)

