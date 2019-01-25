import json
import rescuetime

rt = rescuetime.RescueAPI()

print("""
--------------------------------------------------------------------------------
Testing Alerts Feed
--------------------------------------------------------------------------------
""")
result = rt.list_alerts()
print(result['status_code'])
payload = json.dumps(result['json'], indent=2)
print(payload)

print("""
--------------------------------------------------------------------------------
Testing Alerts Status
--------------------------------------------------------------------------------
""")
result = rt.alert_status()
print(result['status_code'])
payload = json.dumps(result['json'], indent=2)
print(payload)

print("""
--------------------------------------------------------------------------------
Testing Highlights Feed
--------------------------------------------------------------------------------
""")
result = rt.read_highlights(end_date="2019-01-23")
print(result['status_code'])
payload = json.dumps(result['json'], indent=2)
print(payload)

print("""
--------------------------------------------------------------------------------
Testing Highlights POST
--------------------------------------------------------------------------------
""")
result = rt.post_highlight("Test")
payload = result['json']
if result['status_code'] == 200:
    print('Success!')
    print(payload)
elif result['status_code'] == 400:
    print('Fail!')
    print(payload)
