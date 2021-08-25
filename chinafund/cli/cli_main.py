#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys
import os
sys.path.append(os.getcwd())

import configparser

from ..version import __version__
from ..utils import parse_params_options, dict_from_config_items

def cli_main_help():
    syntax_tips = '''Syntax:
    __argv0__ <command>
    __argv0__ <module> <action> [options]

Global Commands:
    help ................... Get help for a command

    list ................... List all funds

Options:
    -v, --version .......... print out the version
    -d, --verbose .......... debug mode produces verbose log output

Example:
    __argv0__ list
'''.replace('__argv0__',os.path.basename(sys.argv[0]))

    print(syntax_tips)

def cli_main_params_options(params, options):
    # parse command line arguments
    cli_tools = {
    }

    if ('-v' in options) or ('--version' in options):
        print( __version__ )
        return

    if len(params) == 0:
        cli_main_help()
        return

    command = params[0]

    if command == 'help':
        if (len(params) > 1) and (params[1] in cli_tools):
                func = cli_tools[ params[1] ]
                func(['help'], options)
        else:
            cli_main_help()

    elif command in cli_tools:
        func = cli_tools[ command ]
        func(params[1:], options)
    else:
        cli_main_help()

def cli_main():
    params, options = parse_params_options(sys.argv)
    cli_main_params_options(params, options)

if __name__ == "__main__":
    cli_main()
