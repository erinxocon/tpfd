from setuptools import setup

setup(name='tpfd',
      version='0.0.2',
      description='Text Parsing Function Dispatcher',
      url='https://github.com/erinxocon/tpfd',
      author="Erin O'Connell",
      author_email='erinocon5@gmail.com',
      license='MIT',
      packages=['tpfd'],
      zip_safe=False,
      classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy'
      ),
       install_requires=['parse'])
