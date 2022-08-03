# parseInt() reloaded

d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,
  'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16,
  'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50,
  'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90, 'hundred':100, 'million':1000000}

def parse_int(x):
  r = 0
  w = []
  for n in x.split('thousand'):
    s = 0
    for i in n.strip().split():
      if i.find('-') != -1:
        for j in i.split('-'):
          if j in d:
            s += d.get(j)
      else:
        if i in d:
          if i == 'hundred':
            s *= d.get(i)
          elif i == 'million':
            s *= d.get(i)
          else:
            s += d.get(i)
    w.append(s)
  if len(w) > 1:
    r = w[0] * 1000 + w[1]
  elif len(w) == 1:
    r = w[0]
  return r

# тест для локального запуска
test = "two hundred forty-six"
print("Тестовый массив:")
print(test)
print("\nРезультат:")
print(parse_int(test))
print("Правильно:\n246")
input()

# Лучшие решения:
# ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        # 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
        # 'eighteen', 'nineteen']
# TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# def parse_int(string):
    # print(string)
    # numbers = []
    # for token in string.replace('-', ' ').split(' '):
        # if token in ONES:
            # numbers.append(ONES.index(token))
        # elif token in TENS:
            # numbers.append((TENS.index(token) + 2) * 10)
        # elif token == 'hundred':
            # numbers[-1] *= 100
        # elif token == 'thousand':
            # numbers = [x * 1000 for x in numbers]
        # elif token == 'million':
            # numbers = [x * 1000000 for x in numbers]
    # return sum(numbers)