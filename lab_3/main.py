"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        identificator = 0
        if isinstance(word, str) and word not in self.storage:
            self.storage[word] = identificator
        return identificator

    def get_id_of(self, word: str) -> int:
        ident = self.storage.get(word, -1)
        return ident

    def get_original_by(self, id: int) -> str:
        if isinstance(id, int):
            for key, value in self.storage.items():
                if id == value:
                    return key
        return "UNK"

    def from_corpus(self, corpus: tuple):
        if isinstance(corpus, tuple):
            count = 0
            for word in corpus:
                self.storage[word] = count
                count += 1


class NGramTrie:
    def __init__(self, number):
        self.size = number
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
        self.code = []
        self.next_sentence = []

    def fill_from_sentence(self, sentence: tuple) -> str:
        if self.size == 2:
            if isinstance(sentence, tuple):
                sentence = list(sentence)
                for index, element in enumerate(sentence):
                    if index != len(sentence) - 1:
                        bi_gram = element, sentence[index + 1]
                        self.code.append(bi_gram)
                for bi_gram in self.code:
                    numb_of_bigram = self.code.count(bi_gram)
                    self.gram_frequencies[bi_gram] = numb_of_bigram
                return "OK"
        return "ERROR"

    def calculate_log_probabilities(self):
        for bi_gram, frequency in self.gram_frequencies.items():
            sum_frequencies = 0
            for key in list(self.gram_frequencies.keys()):
                if bi_gram[0] == key[0]:
                    sum_frequencies += self.gram_frequencies.get(key)
                    probability = frequency / sum_frequencies
                    log_probability = math.log(probability)
                    self.gram_log_probabilities[bi_gram] = log_probability

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not prefix or not isinstance(prefix, tuple) or len(prefix) != self.size - 1:
            return self.next_sentence

        prefix_l = list(prefix)
        print(prefix_l)

        keys_first_elem = [list(keys)[0] for keys in self.gram_log_probabilities.keys()]
        if prefix_l[0] not in keys_first_elem:
            return prefix_l

        prediction = []
        probability = []
        for gram in self.gram_log_probabilities.keys():
            if prefix_l[0] == list(gram)[0]:
                probability.append(self.gram_log_probabilities.get(gram))
        probability_sort = sorted(probability, reverse=True)
        print(probability)
        for key in self.gram_log_probabilities:
            if probability_sort[0] == self.gram_log_probabilities.get(key):
                key_lst = list(key)
                print(key_lst)
                prediction.append(prefix_l[0])
                print(prediction)
                prediction.append(key_lst[-1])
                print(prediction)
        for p in prediction:
            if p not in self.next_sentence:
                self.next_sentence.append(p)
        print('next_sentence = ', self.next_sentence)
        prefix = (prediction[-1],)
        print(prefix)
        if list(prefix)[0] not in keys_first_elem:
            return self.next_sentence
        return self.predict_next_sentence(prefix)


def encode(storage_instance, corpus) -> list:
    for sentence in corpus:
        for index, word in enumerate(sentence):
            for keyword, ident in storage_instance.items():
                if word == keyword:
                    sentence[index] = ident
    return corpus


def split_by_sentence(text: str) -> list:
    if not text:
        return []
    if not isinstance(text, str):
        text = str(text)
    text = text.replace("\n", "")
    new_text = ""
    for symbol in text:
        if symbol.isalpha() or symbol == " ":
            new_text += symbol
    sep_sentence = []
    if new_text != "":
        for index, element in enumerate(new_text):
            if element == " " and new_text[index + 1].isupper():
                new_text = new_text[:index] + "." + new_text[index + 1:]
        if "." in new_text:
            new_text = new_text.lower()
            sentences_lst = new_text.split(".")
            for element in sentences_lst:
                sentence = element.split()
                sentence.insert(0, "<s>")
                sentence.insert(len(sentence), "</s>")
                sep_sentence.append(sentence)
    return sep_sentence
