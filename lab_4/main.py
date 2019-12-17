import math


def clean_tokenize_corpus(texts: list) -> list:
    result = []
    if not isinstance(texts, list):
        return result

    for text in texts:
        try:
            text = text.lower()
            text = text.replace('\n', ' ')

            while '<br />' in text:
                text = text.replace('<br />', ' ')

            clean_text = ''
            for element in text:
                if element.isalpha() or element == ' ':
                    clean_text += element

            while '  ' in clean_text:
                clean_text = clean_text.replace('  ', ' ')

            tokenized_text = clean_text.split(' ')
            result.append(tokenized_text)
        except AttributeError:
            pass
    return result


class TfIdfCalculator:
    def __init__(self, corpus):
        self.tf_values = []
        self.corpus = corpus
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        try:
            for text in self.corpus:
                if text:
                    tf_val_dictionary = {}

                    all_words_freq = 0
                    for word in text:
                        if isinstance(word, str):
                            all_words_freq += 1

                    for word in text:
                        if isinstance(word, str):
                            word_freq = text.count(word)
                            word_tf_value = word_freq / all_words_freq
                            tf_val_dictionary[word] = word_tf_value

                    self.tf_values.append(tf_val_dictionary)
        except TypeError:
            pass

    def calculate_idf(self):
        try:
            len_corpus = len(self.corpus)
            new_corpus = []
            for text in self.corpus:
                if text:
                    new_text = []
                    for word in text:
                        if word and word not in new_text:
                            new_text.append(word)
                    if new_text:
                        new_corpus.append(new_text)
                else:
                    len_corpus -= 1

            words_in_corpus = {}
            for line in new_corpus:
                for word in line:
                    freq_in_one_text = 1
                    if word not in words_in_corpus.keys():
                        words_in_corpus[word] = freq_in_one_text
                    else:
                        words_in_corpus[word] += freq_in_one_text

            for word in words_in_corpus:
                freq_in_corpus = words_in_corpus.get(word)
                idf_value = math.log(len_corpus / freq_in_corpus)
                self.idf_values[word] = idf_value
        except TypeError:
            pass

    def calculate(self):
        try:
            for element in self.tf_values:
                tf_idf_text = {}
                for word, value in element.items():
                    if word not in tf_idf_text:
                        tf_idf_text[word] = value * self.idf_values.get(word)
                self.tf_idf_values.append(tf_idf_text)
        except TypeError:
            pass

    def report_on(self, given_word, document_index):
        try:
            if document_index < len(self.tf_idf_values):
                text = self.tf_idf_values[document_index]
                new_text = sorted(text, key=lambda word: text[word], reverse=True)
                if given_word in new_text:
                    report = text.get(given_word, None)
                    ind_word = new_text.index(given_word)
                    result = (report, ind_word)
                    return result
            return ()
        except TypeError:
            return ()

    def dump_report_csv(self) -> None:
        with open('Report.csv', 'w') as file_csv:
            tf_line = ""
            tf_idf_line = ""
            for name in self.file_names:
                tf_line += "tf_" + name + ","
                tf_idf_line += "tf_idf_" + name
                if name != self.file_names[-1]:
                    tf_idf_line += ","
            headline = "word" + "," + tf_line + "idf" + "," + tf_idf_line
            file_csv.write(headline)
            file_csv.write("\n")
            lines = []
            for word in self.idf_values:
                word_lst = []
                for document in self.tf_values:
                    if word not in word_lst:
                        word_lst.append(word)
                    word_lst.append(str(document.get(word, 0)))

                word_lst.append(str(self.idf_values.get(word, 0)))
                for element in self.tf_idf_values:
                    word_lst.append(str(element.get(word, 0)))
                lines.append(word_lst)
            for word_info in lines:
                one_line = ",".join(word_info)
                file_csv.write(one_line)
                if word_info != lines[-1]:
                    file_csv.write("\n")


REFERENCE_TEXTS = []


if __name__ == '__main__':
    GIVEN_TEXTS = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for given_text in GIVEN_TEXTS:
        with open(given_text, 'r') as file:
            REFERENCE_TEXTS.append(file.read())
