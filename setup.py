from setuptools import setup, find_packages

setup(
    name='ep2014tutorial',
    version='0.0.0',
    url='https://github.com/dobe/ep2014tutorial',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    extras_require=dict(
        test=['crate[test]']
    ),
    install_requires = [
        'setuptools',
        ]
)
