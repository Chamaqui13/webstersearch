from setuptools import setup, find_packages

setup(name='webstersearch',
    version='0.1',
    description='Small function to query the merriam-webster API dictionary',
    author='Octavio Gomez',
    author_email='chamaquin13@gmail.com',
    packages=find_packages(),
    scripts=['src/main.py'],
    zip_safe=False)
