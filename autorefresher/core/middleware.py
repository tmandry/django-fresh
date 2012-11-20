from django.conf import settings

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from bs4 import BeautifulSoup

import sys
import time
import logging

from .models import LastChange


class RefreshEventHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        new_update = LastChange()
        new_update.refreshed = False
        new_update.save()


class AutoRefresher(object):

    def watcher(self):
        observer = Observer()

        path = settings.SITE_ROOT
        event_handler = RefreshEventHandler()
        observer.schedule(event_handler, path, recursive=True)

        observer.start()

    def process_response(self, request, response):
        if settings.DEBUG:
            try:
                soup = BeautifulSoup(response.content)

                # Append refresher
                script_refresher = soup.new_tag('script', src='/static/autorefresher/js/refresher.js')
                soup.head.append(script_refresher)

                response.content = soup.prettify()
            except:
                pass
            return response

    def __init__(self):
        if settings.DEBUG:
            self.watcher()

