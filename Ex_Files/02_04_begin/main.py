NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1 # increment index by 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(name, age)

for name in reversed(NAMES):
    print(name)

for i in range(10):
    print(i)

# enumerate
for i, name in enumerate(NAMES):
    print(f"{i} : {name}")
    

for i, name in enumerate(NAMES):
    print(str(i) +" : "+ str(name))
          