"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
lines_limit = 5
path_to_file = 'The Cactus.txt'


def read_from_file(path_to_file: str, lines_limit: int) -> str:
    opened_text = open(path_to_file, 'r')
    text_read = ''
    for number in range(lines_limit):
        text_read += opened_text.readline()
    opened_text.close()
    return text_read


text = """The most notable thing about Time is that it is so purely relative. A large amount of reminiscence is, by common consent, conceded to the drowning man; and it is not past belief that one may review an entire courtship while removing one's gloves.

The Cactus Enthusiast, Carl Spitzweg, 1850. That is what Trysdale was doing, standing by a table in his bachelor apartments. On the table stood a singular-looking green plant in a red earthen jar. The plant was one of the species of cacti, and was provided with long, tentacular leaves that perpetually swayed with the slightest breeze with a peculiar beckoning motion.
The most notable thing about Time is that it is so purely relative. A large amount of reminiscence is, by common consent, conceded to the drowning man; and it is not past belief that one may review an entire courtship while removing one's gloves.
Trysdale's friend, the brother of the bride, stood at a sideboard complaining at being allowed to drink alone. Both men were in evening dress. White favors like stars upon their coats shone through the gloom of the apartment.
The Cactus Enthusiast, Carl Spitzweg, 1850. That is what Trysdale was doing, standing by a table in his bachelor apartments. On the table stood a singular-looking green plant in a red earthen jar. The plant was one of the species of cacti, and was provided with long, tentacular leaves that perpetually swayed with the slightest breeze with a peculiar beckoning motion.
As he slowly unbuttoned his gloves, there passed through Trysdale's mind a swift, scarifying retrospect of the last few hours. It seemed that in his nostrils was still the scent of the flowers that had been banked in odorous masses about the church, and in his ears the lowpitched hum of a thousand well-bred voices, the rustle of crisp garments, and, most insistently recurring, the drawling words of the minister irrevocably binding her to another."""


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    frequencies = {}
    if str == type(text):
        text = text.lower()
        text_splitted = text.replace("'", " ").split()
        new_text = []
        punct_marks = ["@", "$", "%", "*", "&", "^%$", "—", '"', "'", ".",
                       ":", ";", ",", "/", "\n", "!", "?", "(", ")", "-"]
        for word in text_splitted:
            if not word.isdigit() and word not in punct_marks:
                new_word = ''
                for element in word:
                    if element.isalpha():
                        new_word += element
                if new_word is not '':
                    new_text.append(new_word)
        for new_word in new_text:
            number_of_word = new_text.count(new_word)
            frequencies[new_word] = number_of_word
    if text is None:
        frequencies = {}
    return frequencies


frequencies = calculate_frequences(text)

stop_words = ('a', 'hers', 'm', 'am', 'but', 'did', 'there', 'about', 'me', 'by', 'i', 'don', 'he',
              'once', '', 'during', 'out', 'very', 'if', 'with', 'they', 'own', 'an', 'be', 'all',
              'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'and',
              't', 'off', 'is', 's', 'so', 'or', 'my', 'as', 'his', 'him', 'each', 'the', 'at',
              'are', 'we', 'these', 'your', 'her', 'to', 'up', 'gonna', 'too', 'yes', 'you', 'on',
              'had', 'that', 'it', 'was', 'in', 'from', 'she', 'been', 'how', 'now', 'no', 'upon',
              'one', 'last', 'have', 'when', 'could', 'before', 'any', 'here', 'this', 'not')


def filter_stop_words(frequencies, stop_words):
    """
    Removes all stop words from the given frequencies dictionary
    """
    if frequencies is not None:
        clear_freq = frequencies.copy()
        if stop_words is not None:
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


path_to_file = 'report.txt'
content = get_top_n(frequencies, top_n)


def write_to_file(path_to_file: str, content: tuple):
    file_opened = open(path_to_file, 'w')
    for element in content:
        file_opened.writelines(element)
        file_opened.writelines('\n')
    file_opened.close()
