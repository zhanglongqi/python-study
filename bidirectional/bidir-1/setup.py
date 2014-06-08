from setuptools import setup, find_packages

setup(
    name='bi-directional converter controller',
    version='0.1',
    packages=find_packages(),

    # Declare your packages' dependencies here, for eg:
    install_requires=[
        'PyQt4>=1',
        'bidirUI', ],

    # Fill in these to make your Egg ready for upload to
    # PyPI
    author='longqi',
    author_email='LQZhang@ntu.edu.sg',

    summary='bi-directional converter controller with modbus support',
    url='',
    license='git@github.com:benhuan/python-study.git',
    long_description='Long description of the package',

    # could also include long_description, download_url, classifiers, etc.


)
