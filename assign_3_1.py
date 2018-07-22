token = 'aabb$'

productionRules = {
    '1':['S','AA'],
    '2':['A','aA'],
    '3':['A','b']
}

parseTable = {
    '0':{'a':'s3','b':'s4','$':'','S':'1','A':'2'},
    '1':{'a':'','b':'','$':'a','S':'','A':''},
    '2':{'a':'s3','b':'s4','$':'','S':'','A':'5'},
    '3':{'a':'s3','b':'s4','$':'','S':'','A':'6'},
    '4':{'a':'r3','b':'r3','$':'r3','S':'','A':''},
    '5':{'a':'r1','b':'r1','$':'r1','S':'','A':''},
    '6':{'a':'r2','b':'r2','$':'r2','S':'','A':''}
}

stack = ['0']

result = 0

while True:
    action = parseTable[stack[-1]][token[0]]

    if action[0] == 's':
        stack.append(token[0])
        stack.append(action[1])
        token = token[1:]
        print('shift')
    elif action[0] == 'r':
        for x in range(len(productionRules[action[1]][1]) * 2):
            stack.pop()
        stack.append(productionRules[action[1]][0])
        temp = parseTable[stack[-2]][productionRules[action[1]][0]]
        stack.append(temp)
        print('reduce')
    elif action[0] == 'a':
        print('token accepted')
        break
    else:
        print('invalid token')
        break
