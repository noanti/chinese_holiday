from setuptools import setup

setup(
    name='chinese_holiday',
    author_email='noanti001@gmail.com',
    version='2022.0.0',
    packages=['chinese_holiday'],
    package_data={'chinese_holiday': ['festival_arrangements.yaml']},
    install_requires=[
        'pyyaml'
    ],
)
