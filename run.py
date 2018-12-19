import json
import rescuetime

rt = rescuetime.RescueAPI()
result = rt.post_highlight("Test")
json = json.dumps(result['json'], indent=2)
if result['status_code'] == 200:
    print('Success!')
    print(json)
elif result['status_code'] == 400:
    print('Fail!')
    print(json)
