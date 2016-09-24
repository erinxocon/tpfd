from setuptools import setup
from tpfd import __version__, __license__, __copyright__

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
      version=__version__,
      description='Text Parsing Function Dispatcher',
      url='https://github.com/erinxocon/tpfd',
      author="Erin O'Connell",
      author_email='erinocon5@gmail.com',
      license=__license__,
      packages=['tpfd'],
      zip_safe=False,
      classifiers=CLASSIFIERS,
      install_requires=['parse'],
      data_files=['test/Test1.txt'])
