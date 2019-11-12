"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    matrix = []
    if isinstance(num_cols, int) and isinstance(num_rows, int):
        for _ in range(num_rows):
            matrix.append([0] * num_cols)
    return matrix


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if isinstance(edit_matrix, tuple):
        matrix = list(edit_matrix)
        if matrix and matrix.count([]) == 0 and isinstance(add_weight, int) and isinstance(remove_weight, int):
            for i in range(1, len(matrix)):
                matrix[i][0] = matrix[i - 1][0] + remove_weight
            for j in range(1, len(matrix[0])):
                matrix[0][j] = matrix[0][j - 1] + add_weight
    return matrix


def minimum_value(numbers: tuple) -> int:
    return min(numbers)


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    matrix = list(edit_matrix)
    if matrix and matrix.count([]) == 0 and isinstance(original_word, str) and isinstance(target_word, str):
        if (isinstance(add_weight, int) and isinstance(remove_weight, int) and isinstance(substitute_weight, int)
                and target_word and original_word):
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    val_remove = matrix[i - 1][j] + remove_weight
                    val_add = matrix[i][j - 1] + add_weight
                    val_subst = matrix[i - 1][j - 1]
                    if original_word[i - 1] != target_word[j - 1]:
                        val_subst += substitute_weight
                    values = val_add, val_remove, val_subst
                    matrix[i][j] = minimum_value(values)
    return matrix


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if (isinstance(original_word, str) and isinstance(target_word, str) and isinstance(add_weight, int)
            and isinstance(remove_weight, int) and isinstance(substitute_weight, int)):
        num_rows, num_cols = len(original_word) + 1, len(target_word) + 1
        first_matrix = tuple(generate_edit_matrix(num_rows, num_cols))
        matrix = tuple(initialize_edit_matrix(first_matrix, add_weight, remove_weight))
        new_matrix = fill_edit_matrix(matrix, add_weight, remove_weight, substitute_weight, original_word, target_word)
        return new_matrix[-1][-1]
    return -1


def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    with open(path_to_file, 'w') as file_save:
        for line in edit_matrix:
            new = [str(elem) for elem in line]
            row = ','.join(new)
            file_save.write(row)
            file_save.write('\n')
    return None


def load_from_csv(path_to_file: str) -> list:
    matrix = []
    with open(path_to_file, 'r') as file_load:
        for line in file_load:
            row = []
            for elem in line.split(','):
                row.append(int(elem))
            matrix.append(row)
    return matrix
