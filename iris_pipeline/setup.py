from setuptools import find_packages, setup

entry_point = 'iris_pipeline = iris_pipeline.__main__:main'

setup(
    name='iris_pipeline',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            entry_point
        ]
    },
)
