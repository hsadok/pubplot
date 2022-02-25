# coding=utf-8
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='pubplot',
    version='0.2.5',
    description='Seamless LaTeX and Matplotlib integration for publication plots',
    long_description=readme,
    packages=find_packages(),
    url='',
    download_url='https://github.com/hsadok/pubplot',
    license='ISC',
    author='Hugo Sadok',
    author_email='hugo@sadok.com.br',
    keywords=['matplotlib', 'latex', 'pgf'],
    include_package_data=True,
    package_data= {
        '': ['*.json']
    },
    install_requires=[
        'matplotlib',
        'pylatex',
        'numpy'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)
