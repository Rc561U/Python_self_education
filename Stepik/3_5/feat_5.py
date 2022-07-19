import re
from functools import total_ordering


@total_ordering
class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __str__(self):
        return ' '.join(self.lst_words)

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

pattern = re.compile(r"[–?!,.;]")
lst_text = [StringText(el.split()) for el in map(lambda s: pattern.sub('', s), stich)]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [*map(str, lst_text_sorted)]