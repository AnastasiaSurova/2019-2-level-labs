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
    new_text = ''
    if text is None:
        return frequencies
    if not isinstance(text, str):
        text = str(text)
    for symbol in text:
        if symbol.isalpha() or symbol == ' ':
            new_text += symbol
    new_text = new_text.lower()
    words = new_text.split()
    for key in words:
        key = key.lower()
        if key in frequencies:
            value = frequencies[key]
            frequencies[key] = value + 1
        else:
            frequencies[key] = 1
    return frequencies



def filter_stop_words(frequencies, stop_words):
    """
    Removes all stop words from the given frequencies dictionary
    """
    if frequencies is None:
        frequencies = {}
        return frequencies
    for word in list(frequencies):
        if not isinstance(word, str):
            del frequencies[word]
    if not isinstance(stop_words, tuple):
        return frequencies
    for word in stop_words:
        if not isinstance(word, str):
            continue
        if frequencies.get(word) is not None:
            del frequencies[word]
    return frequencies


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    :param
    """
    if not isinstance(top_n, int):
        frequencies = ()
        return frequencies
    if top_n < 0:
        top_n = 0
    elif top_n > len(frequencies):
        top_n = len(frequencies)
    top_words = sorted(frequencies, key=lambda x: int(frequencies[x]), reverse=True)
    best = tuple(top_words[:top_n])
    return best


def read_from_file(path_to_file: str, lines_limit: int) -> str:
    """
    Read text from file
    """
    file = open(path_to_file)
    counter = 0
    text = ''
    if file is None:
        return text
    for line in file:
        text += line
        counter += 1
        if counter == lines_limit:
            break
    file.close()
    return text


def write_to_file(path_to_file: str, content: tuple):
    """
    Creates new file
    """
    file = open(path_to_file, 'w')
    for i in content:
        file.write(i)
        file.write('\n')
    file.close()
