import requests
import json

instructions = {
  'parts': [
    {
      'html': 'index.html'
    }
  ]
}

response = requests.request(
  'POST',
  'https://api.pspdfkit.com/build',
  headers = {
    'Authorization': 'Bearer pdf_live_NRi5xYZBbfO164cNb37fTTG7d4IY10CeCo15Qc2J5K3'
  },
  files = {
    'index.html': open('index.html', 'rb')
  },
  data = {
    'instructions': json.dumps(instructions)
  },
  stream = True
)

if response.ok:
  with open('result.pdf', 'wb') as fd:
    for chunk in response.iter_content(chunk_size=8096):
      fd.write(chunk)
else:
  print(response.text)
  exit()
