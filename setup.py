from setuptools import setup, find_packages

setup(
  name = 'routing_transformer',
  packages = find_packages(exclude=['examples']),
  version = '0.0.3',
  license='MIT',
  description = 'Routing Transformer (Pytorch)',
  author = 'Phil Wang, Aran Komatsuzaki',
  author_email = 'lucidrains@gmail.com, aran1234321@gmail.com',
  url = 'https://github.com/lucidrains/routing-transformer',
  keywords = ['transformers', 'attention', 'artificial intelligence'],
  install_requires=[
      'torch'
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)