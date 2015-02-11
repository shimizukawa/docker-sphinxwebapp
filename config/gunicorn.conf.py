import os
import multiprocessing

workers = os.environ.get(
    'SPHINXWEB_WORKERS',
    multiprocessing.cpu_count() * 2 + 1)
bind = '0.0.0.0:' + os.environ.get('SPHINXWEB_PORT', '5000')

accesslog = '-'
errorlog = '-'
loglevel = 'info'

