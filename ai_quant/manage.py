# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_quant.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()

#!/usr/bin/env python
<<<<<<< HEAD
# Djnago setting
=======
>>>>>>> a6a16126d06c4c176c3af49c5970b2c19a41189f
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
<<<<<<< HEAD
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
=======
=======
>>>>>>> d7e2f3df410f69864dda0f8d231b48f9827ad002
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


    try:
        if sys.argv[2] == 'react':
            project_root = os.getcwd()
            os.chdir(os.path.join(project_root, "frontend"))
            os.system("npm run build")
            os.chdir(project_root)
            sys.argv.pop(2)
    except IndexError:
        execute_from_command_line(sys.argv)
    else:
        execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()