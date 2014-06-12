from setuptools import setup
from discover_slowest_tests_runner import __version__

setup(
    name='django-slowtests',
    version=__version__,
    description="Locate your slowest tests.",
    long_description=open('README.md').read(),
    author='Michael Herman',
    author_email='michael@realpython.com',
    url='https://github.com/realpython/django-discover-slowest-tests-runner',
    license='MIT',
    packages=['django-slowtests'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
