import os
import datetime
import requests

class RescueAPI():

    def __init__(self, ):
        self.API_KEY = os.environ['RESCUETIME_API_KEY']

    def post_highlight(self, message, highlight_date=None, source=None):
        ENDPOINT = "https://www.rescuetime.com/anapi/highlights_post"
        now = datetime.date.today()
        payload = {}
        payload['key'] = self.API_KEY
        payload['highlight_date'] = highlight_date if highlight_date else now
        payload['description'] = message
        if source: payload['source'] = source
        r = requests.post(ENDPOINT, params=payload)
        return {'status_code': r.status_code,'json': r.json()}
