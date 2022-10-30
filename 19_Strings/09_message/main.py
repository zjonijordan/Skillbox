text = input('Сообщение: ')
word = ''
reverse = ''
def check(temp):
    for u in ['.', ',', ';', ':', '!', '&', '?', '-', '"', ' ', '\'']:
        if u == temp:
            return True
    return False
def lenin(w):
    if len(w):
        return w[::-1]
    return ''

for i in text:
    if check(i):
        b = lenin(word)
        if b:
            reverse += b
            word = ''
        reverse += i
    else:
        word += i

reverse += lenin(word)
print('Новое сообщение:', reverse)