from setuptools import setup

setup(
    name='taskwarrior-focus',
    version='0.1.6',
    description='Taskwarrior wrapper for manual ordering of a focus list',
    url='http://github.com/babadoo/taskwarrior-focus',
    author='babadoo',
    author_email='babadoo@doonx.org',
    keywords = ["taskwarrior", "task", "sort", "order", "focus", "manual"],
    packages=['taskwarrior-focus'],
    scripts=['scripts/tw'],
    install_requires=['tasklib'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description="""\
tw - Taskwarrior wrapper for manual ordering of a focus list
-------------------------------------

Features
 - focus list report
 - user defined attribute (UDA) 'focus'
 - manual sorting of tasks by
 - move tasks up and down the focus list
 - move tasks to top and bottom of focus list
 - move tasks before or after a specified task

This version requires Python 3 or later.
"""
)
