from setuptools import setup
from codecs import open
import re



with open('tpfd/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open('tpfd/__init__.py', 'r') as fd:
    license = re.search(r'^__license__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

CLASSIFIERS = (
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy')


setup(name='tpfd',
      version=version,
      description='Text Parsing Function Dispatcher',
      long_description=readme,
      url='https://github.com/erinxocon/tpfd',
      author="Erin O'Connell",
      author_email='erinocon5@gmail.com',
      license=license,
      packages=['tpfd'],
      zip_safe=False,
      classifiers=CLASSIFIERS,
      install_requires=['parse'],
      data_files=['test/Test1.txt'])
