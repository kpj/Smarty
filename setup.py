from setuptools import setup, find_packages

def readme():
	with open('README.rst') as f:
		return f.read()

setup(
	name='smarty',
	version='0.3.3',
	description='Smart playlist creation for mpd',
	long_description=readme(),
	url='https://github.com/kpj/Smarty',
	author='kpj',
	author_email='kpjkpjkpjkpjkpjkpj@gmail.com',
	license='Apache2',
	packages=find_packages(),
	zip_safe=True,
	scripts=['bin/smarty'],
	install_requires=['python-mpd2']
)
