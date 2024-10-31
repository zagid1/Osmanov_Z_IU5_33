
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': 'Пылесос', 'color': 'yellow'},
    {'title': 'Телевизор', 'price': 34000}
]
#print(*goods, sep = ',')
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
args = ['title','color']

def field(items, *args):
    assert len(args) > 0
    #print(type(*args))
    if len(args) == 1:
        print(', '.join( [ str(element.get(args[0])) for element in items if (element.get(args[0]) != None) ] ) )
    else:
        for element in items:
            arr = {}
            for key in args:
                if element.get(key) != None:
                    arr[key] = element[key]
            print(arr, sep = ',')
field(goods, *args)