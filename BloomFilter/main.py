import re
import math


def get_words(file):
    with open(file, 'r') as f:
        text = f.read()
        text = re.findall('[a-zа-яё]+', text, flags=re.IGNORECASE)
        for i in range(len(text)):
            text[i] = text[i].lower()
        return text


def get_hash_values(word, step, m):
    hash_values = []
    for i in range(step):
        ord_sum = 0
        for char in word:
            ord_value = ord(char)
            ord_sum += ord_value
        ord_sum = ord_sum + i * step * step * 256
        hash_value = ord_sum
        hash_values.append(hash_value % m)
    return hash_values


def update_bloom_filter(word, k, m, bloom_filter):
    hash_values = get_hash_values(word, k, m)
    for hash_value in hash_values:
        bloom_filter[hash_value] += 1
    return bloom_filter

def check_word(word, k, m, bloom_filter):
    hash_values = get_hash_values(word, k, m)
    for hash_value in hash_values:
        if bloom_filter[hash_value] == 0:
            return False
    return True


def main():
    # n - количество элементов хранящихся в фильтре-множестве
    # p - желаемая вероятность ложного срабатывания
    # m - оптимальный размер массива
    # k - оптимальное кол-во хеш-функций

    words = list(set(get_words('InputData')))
    n = len(words)
    p = float(input("Введите желаемую вероятность ложного срабатывания: "))
    m = math.ceil((-1 * (n * math.log(p))) / (math.log(2) * math.log(2)))
    k = math.ceil((float(m) / n) * math.log(2))

    print(f"m = {m}")
    print(f"k = {k}")

    bloom_filter = [0] * m

    for word in words:
        bloom_filter = update_bloom_filter(word, k, m, bloom_filter)

    print(bloom_filter)

    while True:
        command = int(input("1 - добавить слово, 2 - проверить на наличие.\nВведите команду: "))
        if command == 1:
            word = input("Введите слово: ")
            bloom_filter = update_bloom_filter(word.lower(), k, m, bloom_filter)
        elif command == 2:
            word = input("Введите слово: ")
            if_could_have_word = check_word(word.lower(), k, m, bloom_filter)
            if if_could_have_word:
                print("Оно может быть в фильтре")
            else:
                print("Его нет в фильтре")
        else:
            pass


if __name__ == '__main__':
    main()
