from pymystem3 import Mystem
from string import punctuation

input_text = '25.5 миллиона двести тысяч пятьдесят пять рублей'
# text = 'Мне нравится когда моя машина, стоимостью сотку штук баксов, мелькает по телевизору'

mystem = Mystem()

numbers_dict = {
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900,
    'тысяча': 1000,
    'миллион': 1000000
}

jargon_numbers_dict = {
    'чирик': 10,
    'червонец': 10,
    'двадцон': 20,
    'полтинник': 50,
    'сотка': 100,
    'сотыга': 100,
    'сотен': 100,
    'сотня': 100,
    'пятихат': 500,
    'пятихатка': 500,
    'косарь': 1000,
    'тыща': 1000,
    'штука': 1000,
    'мульт': 1000000,
    'мультец': 1000000,
    'лям': 1000000,
    'лямов': 1000000,
    'лимон': 1000000
}


def text_to_lemma_words(text):
    """Возвращает текст, слова которого преобразованы в их Леммы"""
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens
              if token != " " and token.strip() not in punctuation]
    return tokens


def is_numeral(word):
    """Проверяет слово на число.
    Возвращает True, если число.
    Возвращает False, если строка"""
    try:
        float(word)
    except ValueError:
        return False
    return True


def get_index_of_max(num_list):
    x = 0
    index = 0
    for idx, num in enumerate(num_list):
        if num > x:
            x = num
            index = idx
    return index


def calculate(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        max_index = get_index_of_max(num_list)
        total = num_list[max_index]
        # голова - слева
        head = num_list[:max_index]
        # хвост - справа
        tail = num_list[max_index + 1:]
    if head:
        total *= sum(head)
    if tail:
        return total + calculate(tail)
    else:
        return total


def main(text):
    lemma_text = text_to_lemma_words(text)

    num_list = []
    for word in lemma_text:
        if is_numeral(word):
            num_list.append(float(word))
        elif word in numbers_dict:
            num_list.append(numbers_dict[word])
        elif word in jargon_numbers_dict:
            num_list.append(jargon_numbers_dict[word])

    return calculate(num_list)


if __name__ == '__main__':
    print(main(input_text))
