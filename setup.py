from setuptools import find_packages, setup


from dijkstar import __version__


with open('README.md') as fp:
    long_description = fp.read()


setup(
    name='Dijkstar',
    version=__version__,
    description='Dijkstra/A*',
    long_description=long_description,
    license='MIT',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    keywords='Dijkstra A* algorithms',
    url='https://github.com/wylee/Dijkstar',
    packages=find_packages(),
    extras_require={
        'dev': [
            'coverage',
            'flake8',
            'runcommands',
            'tox',
        ],
    },
    entry_points={
        'console_scripts': {
            'dijkstar=dijkstar.__main__:main',
        },
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
