"""
We need to reduce words in the free group F('(', '[', '{', '<') where the inverse of a symbol is it's mirror image through a vertical line. If a word reduces to the empty word, then it is complete and incorrupted. If it does not reduce to the empty word, then look at the reduced word w. If a 'left' delimiter is next to a 'right' delimter and they don't match, then the line is corrupted. We'll score the corruption based on the first incorrect 'right' delimter.
"""


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


def isReduced(word):
    """Checks if word is reduced"""
    for i, symbol in enumerate(word[:-1]):
        if symbol in openingSymbols and word[i + 1] == match(symbol):
            return False
    return True


def reduceWord(word):
    """
    A standard use of stacks. Only slightly more complicated than the usual balanced paren situation.
    """
    stack = []
    for symbol in word:
        if symbol in openingSymbols:
            stack.append(symbol)
        else:
            try:
                last = stack.pop()
                if last in openingSymbols and match(last) == symbol:
                    continue
                else:
                    stack.append(last)
                    stack.append(symbol)
            except IndexError:
                return None
    return "".join(stack)


def firstCorrupt(word):
    """
    A line is corrupt if there is an opening closing pair that don't match. Return first
    problematic closing symbol
    """
    word = reduceWord(word)
    for i, symbol in enumerate(word[:-1]):
        if (symbol in openingSymbols) and (word[i + 1] in closingSymbols):
            if not word[i + 1] == match(symbol):
                return word[i + 1]
    return ""


def scoreSymbol(symbol):
    scoring = {")": 3, "]": 57, "}": 1197, ">": 25137, "": 0}
    return scoring[symbol]


def answer1(lines):
    redWord = [reduceWord(w) for w in lines]
    return sum([scoreSymbol(firstCorrupt(word)) for word in redWord])


def completeLine(word):
    """
    Find the symbols needed to complete the line.
    """
    reduced = reduceWord(word)
    suffix = [match(l) for l in reduced if l in openingSymbols]
    suffix.reverse()
    return "".join(suffix)


closingSymbolScore = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def scoreSuffix(suffix):
    """
    Give score to completing suffix according to scheme in problem.
    """
    score = 0
    for char in suffix:
        score = score * 5 + closingSymbolScore[char]
    return score


def answer2(lines):
    incompleteReduced = [reduceWord(line) for line in lines if firstCorrupt(line) == ""]
    suffixes = [completeLine(line) for line in incompleteReduced]
    scores = sorted([scoreSuffix(suffix) for suffix in suffixes])
    print(scores)
    return scores[len(scores) // 2]


test = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def main():
    infile = get_input("./inputs/ten.txt")
    print(f"Part 1: {answer1(infile)}")
    print(f"Part 2: {answer2(infile)}")


if __name__ == "__main__":
    main()
