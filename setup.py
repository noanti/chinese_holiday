from setuptools import setup

setup(
    name='chinese_holiday',
    author_email='noanti001@gmail.com',
    version='2021.1.1',
    packages=['chinese_holiday'],
    package_data={'chinese_holiday': ['festival_arrangements.yaml']},
    install_requires=[
        'pyyaml'
    ],
)
