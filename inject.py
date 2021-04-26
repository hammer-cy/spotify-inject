#! /bin/python

import requests
import asyncio
import websockets
import json

data = requests.get('http://localhost:9222/json').json()
ws_uri = data[0]['webSocketDebuggerUrl']

with open('style.css', 'r') as file:
    stylesheet = file.read()

print(stylesheet)

script = f"""
var style  = document.createElement('style');
style.textContent = `{stylesheet}`;
document.head.append(style);
console.log('css injected!');
"""

payload = {
    'id': 69420,
    'method': 'Runtime.evaluate',
    'params': {'expression': script}}

async def inject(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(payload))
        await websocket.recv()

asyncio.get_event_loop().run_until_complete(
    inject(ws_uri))
