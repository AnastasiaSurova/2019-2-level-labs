"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('text.txt', 'r') as f:
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

    def get_original_by(self, ident: int) -> str:
        if isinstance(id, int):
            for key, value in self.storage.items():
                if ident == value:
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
        self.next_sentence = []

    def fill_from_sentence(self, sentence: tuple) -> str:
        if isinstance(sentence, tuple):
            for index, element in enumerate(sentence):
                n_gram = sentence[index:index + self.size]
                if len(n_gram) == self.size:
                    if n_gram in self.gram_frequencies:
                        self.gram_frequencies[n_gram] += 1
                    else:
                        self.gram_frequencies[n_gram] = 1
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

        keys_first_elem = [keys[:self.size - 1] for keys in self.gram_log_probabilities]
        if prefix not in keys_first_elem:
            return list(prefix)

        predictions = []
        probability = []
        for gram in self.gram_log_probabilities.keys():
            if prefix == gram[:self.size - 1]:
                probability.append(self.gram_log_probabilities.get(gram))
        probability_sort = sorted(probability, reverse=True)

        for key in self.gram_log_probabilities:
            if probability_sort[0] == self.gram_log_probabilities.get(key):
                for element in prefix:
                    predictions.append(element)
                predictions.append(key[-1])
        for predicted in predictions:
            if predicted not in self.next_sentence:
                self.next_sentence.append(predicted)
        prefix = tuple(predictions[1:])
        if prefix not in keys_first_elem:
            return self.next_sentence
        return self.predict_next_sentence(prefix)


def encode(storage_instance, corpus) -> list:
    for sentence in corpus:
        for index, word in enumerate(sentence):
            for keyword, ident in storage_instance.storage.items():
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


def prediction(ref_text, prefix):
    gram = NGramTrie(2)
    storage_instance = WordStorage()
    sentences = split_by_sentence(ref_text)
    for sentence in sentences:
        storage_instance.from_corpus(tuple(sentence))
    corpus = encode(storage_instance, sentences)
    gram.fill_from_sentence(tuple(corpus))
    gram.calculate_log_probabilities()
    predict = gram.predict_next_sentence(prefix)
    print(predict)
    predicted_sentence = ""
    for number in predict:
        predicted_sentence += storage_instance.get_original_by(number)
        predicted_sentence += " "
    print(predicted_sentence)
