# coding=utf-8
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='pubplot',
    version='0.1',
    description='Generate plots to use in a LaTeX publication using matplotlib',
    long_description=readme,
    packages=find_packages(),
    url='',
    download_url='',
    license='GPLv3',
    author='Hugo Sadok',
    author_email='hugo@sadok.com.br',
    keywords=['matplotlib', 'latex', 'pgf'],
    include_package_data=True,
    install_requires=[
        'matplotlib',
        'pylatex'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
)
