def all_variants(text: str):
    if isinstance(text, str):
        for i in range(len(text)):
            for j in range(i, len(text)):
                yield text[j - i:j + 1]
    else:
        raise TypeError('Должна быть строка')


a = all_variants("abc")
for i in a:
    print(i)

b = all_variants('Колокол')
for i in b:
    print(i)
try:
    b = all_variants(123)
    for i in b:
        print(i)
except TypeError:
    print('Сказано же, строка!')
