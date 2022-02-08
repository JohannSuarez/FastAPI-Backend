#! /usr/bin/bash

gunicorn -b 127.0.0.1:8000 -w 4 -k uvicorn.workers.UvicornWorker blog.main:app --name blogfolio_api --chdir /root/Documents/blogfolio/ --access-logfile /root/.config/blogfolio/logs/access.log --error-logfile /root/.config/blogfolio/logs/error.log --user root


