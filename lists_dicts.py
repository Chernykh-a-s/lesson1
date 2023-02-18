lst = [3, 5, 7, 9, 10.5]
print(lst)
lst.append('Python')
print(len(lst))


print(lst[0])
print(lst[-1])
print(lst[1:4])  
lst.remove('Python')


dict1 = {
    'city': 'Москва',
    'temperature': '20',
}
print(dict1['city'])
dict1['temperature'] = 15
print(dict1)


print(dict1.get('country'))
print(dict1.get('country', 'Россия'))
dict1['date'] = '27.05.2019'
print(len(dict1))
