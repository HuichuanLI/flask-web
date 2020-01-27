# -*- coding: utf-8 -*-
#使用装饰器极大地复用了代码，但是他有一个缺点就是原函数的元信息不见了， 比如函数的docstring、—name—、参数列表
import functools


def use_logging(level="debug"):
    def decorator(func):
        # 可以使用
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("[%s] %s is running" % (level, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


def bar():
    print('i am bar')


def bar2():
    print('i am bar2')


f = use_logging(level="info")(bar)
f()
print(f.__name__)
print(f.__doc__)
