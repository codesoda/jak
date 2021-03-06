.. _support_detailed:


Support
=======

Python Support
--------------

jak is explicitly tested on Pythons:

- 2.7.7 (It is probably safe to assume jak works for 2.7.7 - 2.7.13)
- 3.3
- 3.4
- 3.5
- 3.6
- `PyPy <http://pypy.org/>`_

Planned but not tested yet, but hopefully work:

- PyPy3

jak follows the `Python end of support dates <https://docs.python.org/devguide/index.html#branchstatus>`_, which in practice means that support ends on the following dates:

- 3.3 (PEP 398) support ends 2017-09-29
- 3.4 (PEP 429) support ends 2019-03-16
- 2.7 (PEP 373) support ends 2020-01-01
- 3.5 (PEP 478) support ends 2020-09-13
- 3.6 (PEP 494) support ends 2021-12-23

For all you Python 2.7 lunatics out there that means when `this clock reaches zero <https://pythonclock.org/>`_ we drop 2.7 in the name of `courage <http://www.theverge.com/2016/9/7/12838024/apple-iphone-7-plus-headphone-jack-removal-courage>`_, progress and maintaining a clean codebase. It is my understanding that dropping 2.7 may implicitly mean dropping PyPy as well, which may sway this decision, since jak is a sucker for scrappy whippersnappers.

It is however likely that even without explicitly testing for it the 3.X versions will continue to work just fine even after we officially stop supporting them.


OS Support
----------

We believe jak should work well on most `*nix <https://en.wikipedia.org/wiki/Unix-like>`_ systems. But is mainly developed on Ubuntu and tested on Ubuntu and macOS.
