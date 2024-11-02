
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': 'Пылесос', 'color': 'yellow'},
    {'title': 'Телевизор', 'price': 34000}
]

args = ['color']

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1: print(', '.join( [ str(element.get(args[0])) for element in items if (element.get(args[0]) != None) ] ) )
    else: print(*[ {key: element.get(key) for key in args if element.get(key) != None} for element in items  ], sep = ', \n', )
field(goods, *args)