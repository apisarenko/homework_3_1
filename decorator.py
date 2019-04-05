import datetime


def path_out(path):
    def decorator(old_func):
        def new_func(*args, **kwargs):
            start = datetime.datetime.now()
            out_in = old_func(*args, **kwargs)
            out = out_in * 32
            output_line = 'Время вызова: ' + str(start) + '\n' + \
                          'Имя функции: ' + (f'{old_func.__name__}') + '\n' + \
                          'Аргумент вызова: ' + str(args) + '\n' + \
                          'Возвращаемое значение: ' + str(out)
            with open(path, 'w', encoding='utf8') as file:
                file.write(str(output_line))
            return out
        return new_func
    return decorator


@path_out('out.txt')
def foo(x, y):
    return x**y
foo(4, 5)
