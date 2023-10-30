from decouple import config
ENV = config('ENV', 'local')

if ENV == 'local':
    print(f"{'*' * 10} loading {ENV} evironment settings {'*' * 10}")
    from .local import *
elif ENV == 'dev':
    print(f"{'*' * 10} loading {ENV} evironment settings {'*' * 10}")
    from .dev import *