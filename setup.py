from setuptools import find_packages, setup

setup(
    name='pyglicko2',
    packages=find_packages(include=['pyglicko2'),
    version='0.1.0',
    description='An implementation of Glicko 2 in Python 3',
    author='Brandon Harrison',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
