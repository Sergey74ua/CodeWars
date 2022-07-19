def spin_words(sentence):
	sentence = sentence.split()
	for i in range(len(sentence)):
		if len(sentence[i]) > 4:
			sentence[i] = sentence[i][::-1]
	return " ".join(sentence)


# тест для локального запуска
test = "Hey fellow warriors"
print("Тестовая строка:")
print(test)
print("\nРезультат:")
print(spin_words(test))
print("Правильно:\nHey wollef sroirraw")
input()

# Лучшие решения:
# spin_words = lambda s: ' '.join(w[::-1] if len(w) > 4 else w for w in s.split())
