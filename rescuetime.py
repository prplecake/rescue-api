import os
import datetime
import requests


class RescueAPI:

    def __init__(self, ):
        self.API_KEY = os.environ['RESCUETIME_API_KEY']

    def read_highlights(self, start_date=None, end_date=None):
        ENDPOINT = "http://www.rescuetime.com/anapi/highlights_feed"
        payload = {}
        payload['key'] = self.API_KEY
        if start_date: payload['start_date'] = start_date
        if end_date: payload['end_date'] = end_date
        r = requests.get(ENDPOINT, params=payload)
        return {'status_code': r.status_code, 'json': r.json()}

    def post_highlight(self, message, highlight_date=None, source=None):
        ENDPOINT = "https://www.rescuetime.com/anapi/highlights_post"
        now = datetime.date.today()
        payload = {}
        payload['key'] = self.API_KEY
        payload['highlight_date'] = highlight_date if highlight_date else now
        payload['description'] = message
        if source: payload['source'] = source
        r = requests.post(ENDPOINT, params=payload)
        return {'status_code': r.status_code, 'json': r.json()}
