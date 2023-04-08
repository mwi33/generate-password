from setuptools import setup, find_packages

setup(
    name='generate-password',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=['click'],
    entry_points="""
        [console_scripts]
        generate-password=pkg:cli
    """
)