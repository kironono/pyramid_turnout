# coding: utf-8

import os
import sys

from pyramid.paster import get_appsettings


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def start_turnout(argv=sys.argv):
    if len(argv) < 3:
        usage(argv)
    config_uri = argv[1]
    message = argv[2]
    settings = get_appsettings(config_uri)

    settings_file = settings.get("turnout.settings_file")
    if not os.path.exists(settings_file):
        with open(settings_file, "w", encoding="utf-8") as f:
            f.write(message)


def stop_turnout(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    settings = get_appsettings(config_uri)

    settings_file = settings.get("turnout.settings_file")
    if os.path.exists(settings_file):
        os.unlink(settings_file)
