site = {'html': {'head': {'title': 'Мой сайт'},'body': {'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'}}}

enter = input('enter: ')
level = int(input("level(1-3): "))
def search(web, count, deep, key):
	if level == count:
		print(web.get(key))
	for i in web.values():
		if type(i) == dict:
			search(i, count + 1, deep, key)

search(site, 1, level, enter)
