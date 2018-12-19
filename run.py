import json
import rescuetime

rt = rescuetime.RescueAPI()

print("""
--------------------------------------------------------------------------------
Testing Highlights Feed
--------------------------------------------------------------------------------
""")
result = rt.read_highlights(start_date="yesterday")
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
