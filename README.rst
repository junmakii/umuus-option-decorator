
umuus-option-decorator
======================

Installation
------------

    $ pip install git+https://github.com/junmakii/umuus-option-decorator.git

Example
-------

    $ umuus_option_decorator

    >>> import umuus_option_decorator

    >>> @umuus_option_decorator.decorator() 
    ... def f(x, options): print(x, options)

    >>> f(1)
    1 {'x': 1}

    >>> f(x=1)
    1 {'x': 1}

    >>> f(options=dict(x=1))
    1 {'x': 1}

    >>> f(options={'x': 1})
    1 {'x': 1}

Authors
-------

- Jun Makii <junmakii@gmail.com>

License
-------

GPLv3 <https://www.gnu.org/licenses/>