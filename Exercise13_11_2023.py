shopping = ['bread', 'potatoes', 'eggs', 'flour', 'rubber duck', 'pizza', 'milk']
amounts =  ['1',     '10',       '12',    '1',    '2',            '5',     '1']
prices =  [3, 0.5, 1.2, 5.3, 13.7, 16, 1.47]


res = 0
for i in range(len(shopping)):
    s = 'I need to buy ' + amounts[i] + ' ' + shopping[i]
    print(s)
    res = res + (prices[i] * int(amounts[i]))
 
print("the total price is " + str(res))