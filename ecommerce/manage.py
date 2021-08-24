#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main(arg2):
    """Run administrative tasks."""
    environment='development'
    if arg2:
        environment='production'
        sys.argv.pop(arg2)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings.'+environment)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    arg=''
    if sys.argv[len(sys.argv)-1]=='PROD':
        arg = len(sys.argv)-1
    main(arg)
