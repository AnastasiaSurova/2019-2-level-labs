"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    matrix = []
    if isinstance(num_cols, int) and isinstance(num_rows, int):
        mtrx_cols = [0] * num_cols
        for numb in range(num_rows):
            matrix.append(mtrx_cols)
    return matrix


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if isinstance(edit_matrix, tuple):
        M = list(edit_matrix)
        if M and M.count([]) == 0 and isinstance(add_weight, int) and isinstance(remove_weight, int):
            for i in range(1, len(M)):
                M[i][0] = M[i - 1][0] + remove_weight
            for j in range(1, len(M[0])):
                M[0][j] = M[0][j - 1] + add_weight
        return M


def minimum_value(numbers: tuple) -> int:
    return min(numbers)


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    M = list(edit_matrix)
    if (M and M.count([]) == 0 and isinstance(original_word, str) and isinstance(target_word, str)
        and target_word and original_word):
        if isinstance(add_weight, int) and isinstance(remove_weight, int) and isinstance(substitute_weight, int):
            for i in range(1, len(M)):
                for j in range(1, len(M[0])):
                    val_remove = M[i - 1][j] + remove_weight
                    val_add = M[i][j - 1] + add_weight
                    if original_word[i - 1] != target_word[j - 1]:
                        val_subst = M[i - 1][j - 1] + substitute_weight
                    else:
                        val_subst = M[i - 1][j - 1]
                    numbers = val_add, val_remove, val_subst
                    M[i][j] = minimum_value(numbers)
    return M


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if (isinstance(original_word, str) and isinstance(target_word, str) and isinstance(add_weight, int)
        and isinstance(remove_weight, int) and isinstance(substitute_weight, int)):
        num_rows, num_cols = len(original_word) + 1, len(target_word) + 1
        mtrix = tuple(generate_edit_matrix(num_rows, num_cols))
        edit_matrix = tuple(initialize_edit_matrix(mtrix, add_weight, remove_weight))
        M = fill_edit_matrix(edit_matrix, add_weight, remove_weight, substitute_weight, original_word, target_word)
        distance = M[-1][-1]
    else:
        distance = -1
    return distance



