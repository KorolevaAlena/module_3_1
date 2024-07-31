calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(name):
    count_calls()
    return (len(name), name.upper(), name.lower())
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [any.upper() for any in list_to_search]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Apple'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('coconut', ['apple', 'peach', 'mango']))
print(is_contains('WorLd', ['peace', 'world', 'ocean']))
print(calls)
