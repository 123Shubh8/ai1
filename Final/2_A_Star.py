g = 0

def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()
        if elements[i] == 0:
            print("_", end=" ")
        else:
            print(elements[i], end=" ")
    print()

def solvable(start):
    inv = 0

    for i in range(9):
        if start[i] <= 1:
            continue
        for j in range(i + 1, 9):
            if start[j] == 0:
                continue
            if start[i] > start[j]:
                inv += 1
    if inv % 2 == 0:
        return True
    return False

def heuristic(start, goal):
    global g
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != 0:
                h += (abs(j - i)) // 3 + (abs(j - i)) % 3
    return h + g

def move_left(start, position):
    start[position], start[position - 1] = start[position - 1], start[position]

def move_right(start, position):
    start[position], start[position + 1] = start[position + 1], start[position]

def move_up(start, position):
    start[position], start[position - 3] = start[position - 3], start[position]

def move_down(start, position):
    start[position], start[position + 3] = start[position + 3], start[position]


def move_tile(start, goal):
    empty_at = start.index(0)
    row = empty_at // 3
    col = empty_at % 3
    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]
    f1, f2, f3, f4 = 100, 100, 100, 100

    if col - 1 >= 0:
        move_left(t1, empty_at)
        f1 = heuristic(t1, goal)
    if col + 1 < 3:
        move_right(t2, empty_at)
        f2 = heuristic(t2, goal)
    if row + 1 < 3:
        move_down(t3, empty_at)
        f3 = heuristic(t3, goal)
    if row - 1 >= 0:
        move_up(t4, empty_at)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2, f3, f4)

    if f1 == min_heuristic:
        move_left(start, empty_at)
    elif f2 == min_heuristic:
        move_right(start, empty_at)
    elif f3 == min_heuristic:
        move_down(start, empty_at)
    elif f4 == min_heuristic:
        move_up(start, empty_at)


def solve_eight(start, goal):
    global g
    g += 1
    move_tile(start, goal)
    print_board(start)
    f = heuristic(start, goal)
    if f == g:
        print("Solved in {} moves".format(f))
        return

    solve_eight(start, goal)


def main():
    global g
    start = list()
    goal = list()
    print("Enter the start state:(Enter 0 for empty):")
    for i in range(9):
        start.append(int(input()))

    print("Enter the goal state:(Enter 0 for empty):")
    for i in range(9):
        goal.append(int(input()))

    print_board(start)

    # To check if solvable
    if solvable(start):
        solve_eight(start, goal)
        print("Solved in {} moves".format(g))
    else:
        print("Not possible to solve")


if __name__ == '__main__':
    main()


# Test Cases
# 
# 1
# 2
# 3
# 0
# 4 
# 6
# 7 
# 5 
# 8 

# 1 
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8
# 0