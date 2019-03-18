try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Automated Testing',
	'author': "Zhoubin Yu",
	'url': 'URL to get it at',
	'download_url': 'Where to download it.',
	'author_email': 'vamyu0202@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'automated testing'
}

setup(**config)
