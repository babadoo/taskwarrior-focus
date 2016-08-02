=================
taskwarrior-focus
=================

Taskwarrior wrapper for manual ordering of a focus list
=======================================================

:Website: https://github.com/babadoo/taskwarrior-focus
:Source: https://github.com/babadoo/taskwarrior-focus
:Documentation: https://github.com/babadoo/taskwarrior-focus/README.rst
:License: BSD License

Features
========

* focus list report
* user defined attribute (UDA) 'focus'
* manual sorting of tasks by focus attribute
* move tasks up and down the focus list
* move tasks to top and bottom of focus list
* move tasks before or after a specified task

Current Release
===============

The current alpha version of taskwarrior-focus is 0.1, released 2016-08-02.

Installation
============

pip install taskwarrior-focus
task config uda.focus.type numeric
task config uda.focus.label Focus
task config uda.focus.default 0
task config report.focus.description 'List of tasks to focus on'
task config report.focus.columns 'id,priority,project,description,urgency,focus'
task config report.focus.filter 'status:pending and focus.not:0'
task config report.focus.sort 'focus+'
tw init

Usage
=====

Call task with tw wrapper without arguments::

    tw


Pass arguments to task as usual::

    tw list
    tw 5 mod pri:H


Set task 3 on top of focus list::

    tw top 3


Set task 7 on bottom of focus list::

    tw bottom 7


Insert task 5 after task 3 in focus list::

    tw after 5 3


Insert task 8 before task 5 in focus list::

    tw before 8 5


Move task 7 up in the focus list::

    tw up 7


Move task 7 down in the focus list::

    tw down 7


