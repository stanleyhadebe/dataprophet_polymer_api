def react_polymer(chain: str) -> tuple[str, int]:
    stack = []
    reactions = 0

    for c in chain:
        if stack and abs(ord(stack[-1]) - ord(c)) == 32:
            stack.pop()
            reactions += 1
        else:
            stack.append(c)

    return "".join(stack), reactions
