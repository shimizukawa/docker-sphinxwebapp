# Docker Sphinx WebSupport Application

Docker image with:

- [sphinx](http://sphinx-doc.org/)
- [sphinx-demo-webapp](https://bitbucket.org/shimizukawa/sphinx-demo-webapp)

which execute building a sphinx documentatio you specified, and start Sphinx WebSupport application that provides a comment feature and a search feature.


# Simple usage

`docker run -d -v /path/to/doc:/doc/source -v /path/to/build:/doc/build -v /path/to/db:/var/sphinxweb shimizukawa/sphinxwebapp:latest`


# settings

PATH

- `/app/bin/start`: sphinx webapp bootstrapping bash script
- `/app/config/`: directory contains `sphinxweb.cfg` and `gunicorn.conf.py`
- `/doc/source/`: documentation source directory that contains conf.py for the documentation.
- `/doc/build/`: build output directory that should be permanent.
- `/var/sphinxweb/`: database directory that should be permanent.

ENVIRONMENT

- `SPHINXWEB_SETTINGS`: path to sphinxweb.cfg.
- `SPHINXWEB_PORT`: port number for web server. default is 5000.
- `SPHINXWEB_WORKERS`: number of workers. default is number of cpu core.


Configulation files

- [sphinxweb.cfg](https://github.com/shimizukawa/docker-sphinxwebapp/blob/master/config/sphinxweb.cfg)
- [gunicorn.conf.py](https://github.com/shimizukawa/docker-sphinxwebapp/blob/master/config/gunicorn.conf.py)

