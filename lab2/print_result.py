
def print_result(input_func):

    def output_func(*arg):
        print(input_func.__name__)                                # print(str(input_func)[10:str(input_func).index("a")-1])
        result = input_func(*arg)
        if type(result) == list: print(*result, sep = "\n")       # [ print(i) for i in result ]
        elif type(result) == dict: [print(f"{i} = {result[i]}") for i in result ]
        else: print(result)
        return result
    return output_func
    

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 13}


@print_result
def test_4():
    return [1, 2, 3, 4, 5]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()