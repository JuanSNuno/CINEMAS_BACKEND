#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        # Import at runtime using importlib to avoid static analysis errors
        # when Django isn't installed in the analysis environment.
        import importlib
        django_core_mgmt = importlib.import_module('django.core.management')
        execute_from_command_line = getattr(django_core_mgmt, 'execute_from_command_line')
    except Exception as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
