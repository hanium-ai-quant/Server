#!/usr/bin/env python
<<<<<<< HEAD
# Djnago setting
=======
>>>>>>> a6a16126d06c4c176c3af49c5970b2c19a41189f
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_quant.settings')
>>>>>>> a6a16126d06c4c176c3af49c5970b2c19a41189f
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
    main()
