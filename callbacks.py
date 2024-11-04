#!/usr/bin/python

import argparse
import json
import logging
import os
from sys import argv

script_dir = os.path.dirname(os.path.abspath(argv[0]))
logging.basicConfig(
    filename=script_dir + "/callbacks.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s",
)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", required=False)
parser.add_argument("-l", "--list", action="store_true")
parser.add_argument("-d", "--data")
args = parser.parse_args()

if args.list:
    # Tell the plugin that we should be registered for media
    print("media,playlist")

if args.type and args.data:
    data = json.loads(args.data)
    # logging.debug(data)

    logging.debug("------------------------------")
    logging.debug(args.type)
    logging.debug("------------------------------")
    logging.debug(data)
    logging.debug("==============================")
