#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        sentence_delimiters = ['.', '?', '!']
        sentence_count = 0
        current_index = 0

        while current_index < len(self._value):
            if self._value[current_index] in sentence_delimiters:
                sentence_count += 1
                while current_index < len(self._value) and self._value[current_index] in sentence_delimiters:
                    current_index += 1
            else:
                current_index += 1

        return sentence_count
