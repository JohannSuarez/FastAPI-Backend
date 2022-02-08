#! /bin/bash

gunicorn -b 127.0.0.1:8000 -w 4 -k uvicorn.workers.UvicornWorker blog.main:app --name blog_api --timeout 120 --chdir /root/Documents/blogfolio/ --user root
