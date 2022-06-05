from typing import List, Dict

class Translator:
    dictionary: Dict[str, List[str]]

    def __init__(self):
        self.dictionary = {}

    def add(self, eng: str, rus: str) -> None:
        if eng not in self.dictionary:
            self.dictionary[eng] = []

        self.dictionary[eng].append(rus)

    def remove(self, eng: str) -> None:
        self.dictionary.pop(eng)

    def translate(self, eng: str) -> List[str]:
        return self.dictionary[eng]


tr = Translator()

for pair_of_words in ('tree - дерево', 'car - машина', 'car - автомобиль',
                      'leaf - лист', 'river - река', 'go - идти',
                      'go - ехать', 'go - ходить', 'milk - молоко'):
    tr.add(*pair_of_words.split(' - '))

tr.remove('car')
print(*tr.translate('go'))