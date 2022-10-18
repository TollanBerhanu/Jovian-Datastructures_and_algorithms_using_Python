line = '*'
max_length = 10

while len(line) < max_length:
    print(line)
    line += "*"
    
while len(line) > 0:
    print(line)
    line = line[:-1]

my_list = [1, 2, 'a', 'b', [1,'a']]
my_list.append('c')
my_tuple = tuple(my_list)
for i in my_tuple:
    print(i)

my_dict = {'key1': 'value1', 'key2': 'value2'}
for k in my_dict:
    print(k + '= ' + my_dict[k])
for v in my_dict.values():
    print(v)
for kv in my_dict.items():
    print(kv)

for char in 'abc':
    print(char)
for i in range(3): # same as range(0, 3) --- 0,1,2
    print('Item: ' + str(i))
for i in range(0, 6, 2): # third argument is step --- 0,2,4
    print(i)

print('Lengths of data structures: ' + str(len(my_list)) + ' ' + str(len(my_dict)))