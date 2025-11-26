def react_polymer(polymer: str):
    stack = []
    reaction_count = 0

    for c in polymer:
        if stack:
            top = stack[-1]
            if top != c and top.upper() == c.upper():
                stack.pop()
                reaction_count += 1
                continue
        stack.append(c)

    return "".join(stack), reaction_count
