def backtrack(state, choices, results):
    # 1. Base case: if solution is complete, save it
    if is_solution(state):
        results.append(state.copy())  # or process it
        return

    # 2. Explore all choices
    for choice in choices:
        if is_valid(choice, state):     # pruning step
            # make choice
            state.append(choice)

            # recurse
            backtrack(state, update_choices(choices, choice), results)

            # undo choice (backtrack)
            state.pop()
