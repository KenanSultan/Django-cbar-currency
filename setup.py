from distutils.core import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = 'cbar_currency',    
  packages = ['cbar_currency'],
  version = '1.0.4',
  license = 'MIT',
  description = 'Getting currencies and differencies from CBAR',
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = 'KENAN SULTAN',
  author_email = 'kenansultan@yahoo.com',
  url = 'https://github.com/KenanSultan/Django-cbar-currency', 
  download_url = 'https://github.com/KenanSultan/Django-cbar-currency/archive/v_1.0.4.tar.gz',
  keywords = ['CBAR', 'CURRENCY'],
  install_requires=['requests'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)