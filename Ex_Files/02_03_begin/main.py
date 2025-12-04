NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2] # from start to index 2 (not inclusive)
GEORGE_RINGO = NAMES[2:] # from index 2 to the end
REVERSE = NAMES[::-3] # reverse order of names with step of 3
EVERY_OTHER = NAMES[::3] # every third name

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(f"initial list: {NAMES}")
print(f"from start to index 2 (not inclusive): {JOHN_PAUL}")
print(f'from index 2 to the end: {GEORGE_RINGO}')
print(f'reverse order of names with step of 3: {REVERSE}')
print(f'every third name: {EVERY_OTHER}')