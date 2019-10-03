"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
lines_limit = 5
path_to_file = 'The Cactus.txt'
def read_from_file(path_to_file: str, lines_limit: int) -> str:
    opened_text = open(path_to_file, 'r')  # открывает файл с текстом для чтения, текстовый файл находится в папке с файлом с кодом
    text_read = ''
    for number in range(lines_limit):
        text_read += opened_text.readline()
    #text_read = opened_text.readlines()[:lines_limit + 1]
    opened_text.close()
    return text_read

text = read_from_file(path_to_file, lines_limit)

def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    frequencies = {}
    if type(text) == str:
        text = text.lower()  # меняет регистр текста на нижний
        text_splitted = text.replace("'", " ").split()  # делим  строку на элемены по пробелам
        new_text = []
        punct_marks = [ '@', '$', '%','*', '&', '^%$' , "—", '"', "'", ".", ":", ";", ",", "/", "\n", "!", "?", "(", ")", "-"]  # список пунктуационных знаков
        for word in text_splitted:  # проходим по каждому элементу в списке
            if not word.isdigit() and word not in punct_marks:  # если элемент не цифра и элемент не находится в списке пунктуационных знаков
                new_word = ''  # создали пустую строку
                for element in word:  # проходим по каждому элементу в слове
                    if element.isalpha():  # если элемент буква
                        new_word += element  # создаем новое слово, добавляем в пустую строку элементы
                if new_word is not '':
                    new_text.append(new_word)
        for new_word in new_text:
            number_of_word = new_text.count(new_word)
            frequencies[new_word] = number_of_word
    if text == None:
        frequencies = {}
    return frequencies


print(calculate_frequences(text))

frequencies = calculate_frequences(text)

stop_words = ('a', 'hers', 'm', 'am', 'but', 'did', 'there', 'about', 'me', 'by', 'i', 'don', 'he',
              'once', '', 'during', 'out', 'very', 'if', 'with', 'they', 'own', 'an', 'be', 'all',
              'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'and',
              't', 'off', 'is', 's', 'so', 'or', 'my', 'as', 'his', 'him', 'each', 'the', 'at', 'not',
              'are', 'we', 'these', 'your', 'her', 'to', 'up', 'gonna', 'too', 'yes', 'you', 'on',
              'had', 'that', 'it', 'was', 'in', 'from', 'she', 'been', 'how', 'now', 'no', 'upon', 'this',
              'one', 'last', 'have', 'when', 'could', 'before', 'any', 'here')


def filter_stop_words(frequencies, stop_words):
    """
    Removes all stop words from the given frequencies dictionary
    """
    if frequencies != None:
        clear_freq = frequencies.copy()
        if stop_words != None:
            stop_words_list = list(stop_words)
            for key in clear_freq.keys():
                if type(key) != str:
                    stop_words_list.append(key)
            for stop in stop_words_list:
                if stop in clear_freq.keys():
                    del clear_freq[stop]
        return clear_freq
    else:
        frequencies = {}
        return frequencies



print(filter_stop_words(frequencies, stop_words))

frequencies = filter_stop_words(frequencies, stop_words)
top_n = 10
def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    if top_n > 0:
        words = list(frequencies.items())
        words.sort(key=lambda elmnt_val: elmnt_val[1], reverse=True)
        top_words = []
        for element in words:
            element_first = element[0]
            top_words.append(element_first)
        tuple_top_words = tuple(top_words[:top_n])
    else:
        tuple_top_words = ()
    return tuple_top_words


print(get_top_n(frequencies, top_n))
