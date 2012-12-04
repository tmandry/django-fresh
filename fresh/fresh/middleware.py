import sys
import time
import logging
import json

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from bs4 import BeautifulSoup

from django.conf import settings


fresh = False


class Fresh(object):
    class RefreshEventHandler(FileSystemEventHandler):

        def on_any_event(self, event):
            global fresh
            fresh = True

    def watcher(self):
        observer = Observer()

        path = settings.SITE_ROOT
        event_handler = self.RefreshEventHandler()
        observer.schedule(event_handler, path, recursive=True)

        observer.start()

    def process_response(self, request, response):
        if settings.DEBUG:
            mimetype = response._headers['content-type'][1]
            if mimetype == 'application/json':
                items = json.loads(response.content)
                try:
                    global fresh
                    if fresh:
                        items['fresh'] = fresh
                        fresh = False
                        response.content = json.dumps(items)
                        print response.content
                except:
                    pass
            elif mimetype == 'text/html; charset=utf-8':
                try:
                    soup = BeautifulSoup(response.content)

                    # Append refresher
                    script_fresh = soup.new_tag('script', src='/static/fresh/js/refresher.js')
                    soup.head.append(script_fresh)

                    response.content = soup.prettify()
                except:
                    pass
            return response

    def __init__(self):
        if settings.DEBUG:
            self.watcher()

