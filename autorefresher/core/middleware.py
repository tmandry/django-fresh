import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from django.conf import settings


class AutoRefresher(object):
    def watcher(self):
        logging.basicConfig(level=logging.INFO,
                            format='[%(asctime)s] %(message)s',
                            datefmt='%d/%b/%Y %H:%M:%S')
        path = settings.SITE_ROOT
        event_handler = LoggingEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()

    def process_response(self, request, response):
        return response

    def __init__(self):
        self.watcher()

