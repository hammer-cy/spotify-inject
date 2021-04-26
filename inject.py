#! /bin/python

import requests
import asyncio
import websockets
import json

data = requests.get('http://localhost:9222/json').json()
ws_uri = data[0]['webSocketDebuggerUrl']

script = """
var cssId = 'myCss';  // you could encode the css path itself to generate id..
if (!document.getElementById(cssId))
{
    var head  = document.getElementsByTagName('head')[0];
    var link  = document.createElement('link');
    link.id   = cssId;
    link.rel  = 'stylesheet';
    link.type = 'text/css';
    link.href = 'https://raw.githubusercontent.com/hammer-cy/spotify-inject/main/style.css';
    //link.media = 'all';
    head.appendChild(link);
}
console.log('injected css!');
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
