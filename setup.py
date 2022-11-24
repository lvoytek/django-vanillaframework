"""Setup.py file."""
from setuptools import setup
from vanillaframework import __version__

setup(
    name='django-vanillaframework',
    version=__version__,
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
