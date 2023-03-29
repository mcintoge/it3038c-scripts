import json
import requests

response = requests.get('http://localhost:3000/')


if response.status_code == 200:
    widget_data = response.json()
    
    widgets = [(widget['name'], widget['color']) for widget in widget_data]
    
    
    for widget in widgets:
        print(f'{widget[0]} is {widget[1]}.')
else:
    print(f'Error: {response.status_code}')

