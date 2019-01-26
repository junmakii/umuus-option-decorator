
umuus-option-decorator
======================

Installation
------------

    $ pip install git+https://github.com/junmakii/umuus-option-decorator.git

Example
-------

    $ umuus_option_decorator

    >>> import umuus_option_decorator

    @umuus_option_decorator.option_decorator()
    def run(x, options):
        assert x == options.x

----

    In [2]: @umuus_option_decorator.decorator() 
       ...: def f(x): print(x)

    In [3]: f(1)
    1

    In [4]: f(x=1)
    1

    In [5]: f(options=dict(x=1))
    1

    In [6]: @umuus_option_decorator.decorator() 
       ...: def f(x, options): print(x, options)

    In [7]: f(options=dict(x=1))
    1 {'x': 1}

    In [8]: f(1)
    1 {}

Authors
-------

- Jun Makii <junmakii@gmail.com>

License
-------

GPLv3 <https://www.gnu.org/licenses/>