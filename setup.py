
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def run_tests(self):
        import sys
        import shlex
        import pytest
        errno = pytest.main(['--doctest-modules'])
        if errno != 0:
            raise Exception('An error occured during installution.')
        install.run(self)


setup(
    packages=setuptools.find_packages('.'),
    version='0.1',
    url='https://github.com/junmakii/umuus-option-decorator',
    author='Jun Makii',
    author_email='junmakii@gmail.com',
    keywords=[],
    license='GPLv3',
    scripts=[],
    install_requires=['toolz>=0.9.0', 'addict>=2.2.0'],
    dependency_links=[],
    classifiers=[],
    entry_points={},
    project_urls={},
    setup_requires=[],
    test_suite='',
    tests_require=[],
    extras_require={},
    package_data={},
    python_requires='',
    include_package_data=True,
    zip_safe=True,
    name='umuus-option-decorator',
    description='Utilities, tools, and scripts for Python.',
    long_description=('Utilities, tools, and scripts for Python.\n'
 '\n'
 'umuus-option-decorator\n'
 '======================\n'
 '\n'
 'Installation\n'
 '------------\n'
 '\n'
 '    $ pip install '
 'git+https://github.com/junmakii/umuus-option-decorator.git\n'
 '\n'
 'Example\n'
 '-------\n'
 '\n'
 '    $ umuus_option_decorator\n'
 '\n'
 '    >>> import umuus_option_decorator\n'
 '\n'
 '    @umuus_option_decorator.option_decorator()\n'
 '    def run(x, options):\n'
 '        assert x == options.x\n'
 '\n'
 '----\n'
 '\n'
 '    In [2]: @umuus_option_decorator.decorator() \n'
 '       ...: def f(x): print(x)\n'
 '\n'
 '    In [3]: f(1)\n'
 '    1\n'
 '\n'
 '    In [4]: f(x=1)\n'
 '    1\n'
 '\n'
 '    In [5]: f(options=dict(x=1))\n'
 '    1\n'
 '\n'
 '    In [6]: @umuus_option_decorator.decorator() \n'
 '       ...: def f(x, options): print(x, options)\n'
 '\n'
 '    In [7]: f(options=dict(x=1))\n'
 "    1 {'x': 1}\n"
 '\n'
 '    In [8]: f(1)\n'
 '    1 {}\n'
 '\n'
 'Authors\n'
 '-------\n'
 '\n'
 '- Jun Makii <junmakii@gmail.com>\n'
 '\n'
 'License\n'
 '-------\n'
 '\n'
 'GPLv3 <https://www.gnu.org/licenses/>'),
    cmdclass={"pytest": PyTest},
)
