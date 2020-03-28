#from distutils.core import setup
from setuptools import setup
setup(
  name = 'nmc_bins_python',         # How you named your package folder (MyLib)
  packages = ['nmc_bins_python'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Provides API Access to NMC BINS web service',   # Give a short description about your library
  author = 'NMC Corp',                   # Type in your name
  author_email = 'bins_dev@nmcomputing.com',      # Type in your E-Mail
  url = 'https://github.com/nmcbins/nmc_bins_python',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/nmcbins/nmc_bins_python/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Bot', 'Language', 'Normalization'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
		'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
	'Programming Language :: Python :: 2', 
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)