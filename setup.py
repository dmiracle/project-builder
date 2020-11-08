from setuptools import setup

setup(
    name="HelloWorld",
    version='0.0.1',
    py_modules='hello',
    entry_points='''
        [console_scripts]
        hello=hello:cli
    '''
)