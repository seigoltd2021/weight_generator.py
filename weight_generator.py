import random

weights = []

for i in range(10):
    weight = random.randint(1, 100)
    weights.append(weight)

print("Сгенерированные веса:", weights)
