#!/usr/bin/env python
from setuptools import setup, find_packages
import os

README = file(os.path.join(
    os.path.dirname(__file__),
    'README.md')).read()

setup(name='authentic2-idp-freshdesk',
        version='0.1',
        license='AGPLv3',
        description='Freshdesk simple SSO support for Authentic2',
        long_description=README,
        author="Jocelyn Delalande",
        author_email="jdelalande@oasiswork.fr",
        packages=find_packages('src'),
        package_dir={
            '': 'src',
        },
        install_requires=[
        ],
        entry_points={
            'authentic2.plugin': [
                'authentic2-idp-freshdesk= authentic2_idp_freshdesk:Plugin',
            ],
        },
)
