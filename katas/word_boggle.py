from collections import defaultdict


def word_boggle(board, words):
    tiles = {(i, j) for i in range(len(board)) for j in range(len(board[0]))}
    reachables = {(i, j): reachable_from(board, (i, j)) for i, j in tiles}
    char_locs = build_char_locs(board)
    bogglable_words = [word for word in words if bogglable(word, board, reachables, char_locs)]
    return sorted(bogglable_words)


def reachable_from(board, loc):
    i, j = loc
    all_neighbors = {(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                     (i, j - 1), (i, j + 1),
                     (i + 1, j - 1), (i + 1, j), (i + 1, j + 1), }
    return {(i, j) for (i, j) in all_neighbors if (0 <= i < len(board) and 0 <= j < len(board[0]))}


def build_char_locs(board):
    char_locs = defaultdict(list)
    for i in range(len(board)):
        for j in range(len(board[0])):
            char_locs[board[i][j]].append((i, j))

    return char_locs


def bogglable(word, board, reachables, char_locs):
    if len(word) == 0:
        return True
    first_char = word[0]
    if first_char not in char_locs:
        return False

    start_positions = char_locs[first_char]
    return any(bogglable_req([pos], word[1:], board, reachables, char_locs) for pos in start_positions)


def bogglable_req(visited, word, board, reachables, char_locs):
    if len(word) == 0:
        return True
    first_char = word[0]
    if first_char not in char_locs:
        return False
    relevant_neighbors = [(i, j) for (i, j) in reachables[visited[-1]]
                          if board[i][j] == first_char]
    relevant_neighbors = [(i, j) for (i, j) in relevant_neighbors
                          if (i, j) not in visited]
    return any(bogglable_req(visited + [neighbor], word[1:], board, reachables, char_locs)
               for neighbor in relevant_neighbors)


board = [["N", "L", "L", "I"],
         ["T", "J", "A", "B"],
         ["L", "E", "T", "S"]]
words = ["STALL",
         "NOTHING",
         "ABSTRACTEDNESSES",
         "VITA",
         "SAIL",
         "ACTA",
         "STEAL",
         "JAIL"]
assert word_boggle(board, words) == ["JAIL",
                                     "SAIL",
                                     "STALL",
                                     "STEAL"]
