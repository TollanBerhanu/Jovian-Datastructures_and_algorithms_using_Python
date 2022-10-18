from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases

str = 'Hello ' + 'I am' + '{}' + ' years old'
if not None:
    print('Hello')
print(str.format(12))
parity = 'odd' if 2%2 != 0 else 'even'
print('Parity ' + parity)
a_number = 6
if a_number % 2 == 0:
    pass
elif a_number % 3 == 0:
    print('{} is divisible by 3 but not divisible by 2'.format(a_number))

tests = []
# query occurs in the middle
tests.append({
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
})
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})
# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})
# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})
# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})
# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})
# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})
# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})
# query occurs multiple times upto the first element
tests.append({
    'input': {
        'cards': [5, 5, 5, 5, 5, 5, 3, 2, 2, 2, 0, 0, 0],
        'query': 5
    },
    'output': 0
})

# Assume cards is in descending order
def locate_card(cards, query):
    start, end = 0, len(cards) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_num = cards[mid]

        if mid_num == query:
            while mid-1 >= 0 and cards[mid-1] == mid_num:
                mid -= 1
            return mid
        elif mid_num < query:
            end = mid - 1
        elif mid_num > query:
            start = mid + 1
        
    return -1

evaluate_test_cases(locate_card, tests)