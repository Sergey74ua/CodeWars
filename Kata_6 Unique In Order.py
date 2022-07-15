# Unique In Order

def solution(n):
	arr = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
	s = ''
	for i in sorted(arr.keys(),reverse=True):
		while n >= i:
			s += arr[i]
			n -= i
	return s

# Тест для локального запуска
test = 984
print('Тестируем: ', test)
print('Результат: ', solution(test))
print('Правильно: ', "CMLXXXIV")
input()

# Другой вариант:
# units = " I II III IV V VI VII VIII IX".split(" ")
# tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
# hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
# thousands = " M MM MMM".split(" ")
# def solution(n):
#    return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]
