from setuptools import setup, find_packages

setup(
    name='ep2014tutorial',
    version='0.0.0',
    url='https://github.com/dobe/ep2014tutorial',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'paste.app_factory': [
            'main=ep2014tutorial.server:app_factory',
            ],
        'console_scripts': [
            'app=pyramid.scripts.pserve:main',
            ],
          },
    extras_require=dict(
        test=['crate[test]',
              'webtest'
        ]
    ),
    install_requires = [
        'setuptools',
        'crate[sqlalchemy]',
        'pyramid',
        'waitress',
        ]
)
