#!/usr/bin/env python
from setuptools import setup, find_packages, Command

class test_example_app(Command):
    """Runs all tests under the sympy/ folder
    """

    description = "Run tests in example_feedback application"
    user_options = []  # distutils complains if this is not here.

    def initialize_options(self):  # distutils wants this
        pass

    def finalize_options(self):    # this too
        pass

    def run(self):
        import os
        import subprocess
        os.chdir('example_feedback')
        subprocess.call(['./manage.py', 'test'])

METADATA = dict(
    name='django-simple-feedback',
    version='0.2.6',

    author='Nicolas Patry',
    author_email='nicolas.patry@student.ecp.fr',

    description="""Django application that allows you to easily get user
feedbacks. Users need to be registrated via django.contrib.auth.""",
    long_description=open('README.rst').read(),

    url='http://github.com/Narsil/django-simple-feedback',
    download_url='http://github.com/Narsil/django-simple-feedback',

    include_package_data = True,

    packages=find_packages(),

    keywords='django feedback bugs suggestions',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public \
License (LGPL)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    cmdclass = {
        'test': test_example_app
    }
)


if __name__ == '__main__':
    setup(**METADATA)

