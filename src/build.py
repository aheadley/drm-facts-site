#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Copyright (c) 2013, Alex Headley <aheadley@waysaboutstuff.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
# THIS SOFTWARE.

import os.path

import staticjinja

# TEMPLATE_DIR = os.path.join(
#     os.path.dirname(os.path.abspath(__file__)),
#     'templates')
TEMPLATE_DIR = 'templates'
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'output')

if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option('-t', '--template', dest='searchpath',
        help='Path to template directory', metavar='PATH',
        default=TEMPLATE_DIR)
    parser.add_option('-o', '--output', dest='outpath',
        help='Path to generated output', metavar='PATH',
        default=OUTPUT_DIR)
    opts, args = parser.parse_args()
    print opts
    staticjinja.main(searchpath=opts.searchpath, outpath=opts.outpath)
