import random, os, sys

price = 75
balance = 1500
count = 0
week = 1
month = 1
TAX = 0.3

def plus():
	chance = random.random()
	factor = random.random()
	global price
	if chance <= 0.4:
		price *= (1+factor)
def minus():
	chance = random.random()
	factor = random.random()
	global price
	if chance >= 0.4:
		price *= factor

while True:
	full_bal = f'''
--- МЕСЯЦ {month} ---
Баланс: {balance:.2f}р.
Цена коина: {price:.2f}р.
—> {count} *{price:.2f} = {count*price:.2f}р.
'''
	print(full_bal)
	print('[1] Купить')
	print('[2] Продать')
	u = input('Как действуем?\n')

	if u == '1':
		try:
			c = int(input(f'Сколько покупаем? (можно: {int(balance/price)})\n'))
		except ValueError:
			print('Введите число!')
			continue
		if c < 0:
			print('Число должно быть положительным!')
			continue
		if balance >= c*price:
			balance -= c*price
			count += c
			plus()
		else:
			print('Недостаточно средств')
			continue

	elif u == '2':
		try:
			c = int(input('Сколько продаем?\n'))
		except ValueError:
			print('Введите число!')
			continue
		if c < 0:
			print('Число должно быть положительным!')
			continue
		if c <= count:
			balance += c*price
			count -= c
			minus()
		else:
			print('Недостаточно коинов')
			continue
	else:
		print('Некорректный выбор')
		continue
	week+=1
	if week == 4:
		week = 1
		month += 1
		if balance>1000:
			print(f'Вы заплатили ежемесячный налог в размере {(balance*TAX):.2f}р.')
			balance -= balance*TAX
	if balance+(count*price) < 1:
		print('Вы банкрот!')
		break
	input('Нажмите Enter, чтобы продолжить...')
	useos = sys.platform
	if useos == 'win32':
		os.system('cls')
	else:
		os.system('clear')
