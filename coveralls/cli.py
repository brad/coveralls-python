#!/usr/bin/env python
"""Publish coverage results online via coveralls.io

Puts your coverage results on coveralls.io for everyone to see.
It makes custom report for data generated by coverage.py package and sends it to `json API`_ of coveralls.io service.
All python files in your coverage analysis are posted to this service along with coverage stats,
so please make sure you're not ruining your own security!

Usage:
    coveralls [options]
    coveralls debug  [options]

    Debug mode doesn't send anything, just outputs json to stdout, useful for development.
    It also forces verbose output.

Global options:
    -h --help       Display this help
    -v --verbose    Print extra info, True for debug command

Example:
    $ coveralls
    Submitting coverage to coveralls.io...
    Coverage submitted!
    Job #38.1
    https://coveralls.io/jobs/92059
"""
import logging
from docopt import docopt
from coveralls import Coveralls


log = logging.getLogger('coveralls')


def main(argv=None):
    options = docopt(__doc__, argv=argv)
    if options['debug']:
        options['--verbose'] = True
    level = logging.DEBUG if options['--verbose'] else logging.INFO
    log.addHandler(logging.StreamHandler())
    log.setLevel(level)

    coverallz = Coveralls()
    if not options['debug']:
        log.info("Submitting coverage to coveralls.io...")
        result = coverallz.wear()
        log.info("Coverage submitted!")
        log.info(result['message'])
        log.info(result['url'])
        log.debug(result)
    else:
        log.info("Testing coveralls-python...")
        coverallz.wear(dry_run=True)