"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequencies():
    """
    Calculates number of times each word appears in the text
    """
    opened_text = open('The cats.txt', 'r')  # открывает файл с текстом для чтения, текстовый файл находится в папке с файлом с кодом
    text = opened_text.read()
    text = text.lower()  # меняет регистр текста на нижний
    text_splitted = text.split()  # делим  строку на элемены по пробелам
    new_text = []
    punct_marks = ["“", "—", "”", "’", "'", ".", ":", ";", ",", "/", "\n", "!", "?", "(", ")", "-"]  # список пунктуационных знаков
    for word in text_splitted:  # проходим по каждому элементу в списке
        if not word.isdigit() and word not in punct_marks:  #если элемент буква и элемент не находится в списке пунктуационных знаков
            new_word = ''  # создали пустую строку
            for element in word:  # проходим по каждому элементу в слове
                if element not in punct_marks:  # если элемент не входит
                    new_word += element  # создаем новое слово, добавляем в пустую строку элементы
            if new_word is not '':
                new_text.append(new_word)
    frequencies = {}
    for new_word in new_text:
        number_of_word = new_text.count(new_word)
        frequencies[new_word] = number_of_word
    opened_text.close()
    return frequencies

print(calculate_frequencies())


def filter_stop_words(frequencies):
    """
    Removes all stop words from the given frequencies dictionary
    """
    stop_words = ('in', 'the', 'a', 'theres','with', 'as', 'more', 'is', 'theyre',
                  'on', 'or', 'that', 'to', 'even', 'than', 'did', 'its', 'unlike',
                  'one', 'out', 'all', 'still', 'will', 'does', 'was', 'who', 'those',
                  'over', 'and', 'other', 'maybe', 'not', 'to', 'often', 'our', 'an',
                  'i', 'lot', 'me', 'at', 'this', 'dr', 'up', 'into', 'her', 'how',
                  'isnt', 'my', 'do', 'once', 'some', 'might', 'toward', 'were', 'much'
                  )
    clear_freq = dict(frequencies)
    for word in sorted(clear_freq):
        for s_word in stop_words:
            if word == s_word:
                deleted_word = clear_freq.pop(word)
    return clear_freq

filter_stop_words(calculate_frequencies())

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    #for val in clear_freq.values():
        #for i in range(16):
