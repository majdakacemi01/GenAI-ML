import string
import re
class Text:
    def __init__(self, text):
        self.text = text

   
    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else None

    def most_common_word(self):
        words = self.text.lower().split()
        freq = {}

        for w in words:
            freq[w] = freq.get(w, 0) + 1

        most_common = max(freq, key=freq.get)
        return most_common

    def unique_words(self):
        words = self.text.lower().split()
        return list(set(words))


    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return cls(content)


# BONUS : 

class TextModification(Text):

    def remove_punctuation(self):
        translator = str.maketrans("", "", string.punctuation)
        cleaned = self.text.translate(translator)
        return cleaned

    def remove_stop_words(self):
        stop_words = {
            "the", "a", "an", "and", "is", "are", "to", "in", "it", "of", 
            "that", "this", "for", "on", "with", "as", "by", "at", "from"
        }

        words = self.text.lower().split()
        filtered = [w for w in words if w not in stop_words]
        return " ".join(filtered)

    def remove_special_characters(self):
        cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", self.text)
        return cleaned
