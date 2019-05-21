# -*- coding: utf-8 -*-

import argparse
import asyncio

from e3dump.main import main


def get_parser():
    parser = argparse.ArgumentParser(prog='e3dump', description='NCTU e3 dump')
    parser.add_argument('--username', type=str,
                        help='NCTU e3 username', required=True)
    parser.add_argument('--password', type=str,
                        help='NCTU e3 password', required=True)
    parser.add_argument(
        '--path', type=str, default='.',
        help='Dump to this path, default is current pwd')

    return parser


def run():
    args = get_parser().parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args.username, args.password, args.path))
