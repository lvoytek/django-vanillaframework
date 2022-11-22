"""Setup.py file."""
from setuptools import setup

setup(
    name='django-vanillaframework',
    version='0.1.0',
    packages=["vanillaframework"],
    url='https://github.com/lvoytek/django-vanillaframework',
    license='LGPL v3',
    author='Lena Voytek',
    author_email='lena@voytek.dev',
    description='Vanilla Framework frontend for Django',
    install_requires=[
        'django'
    ]
)
