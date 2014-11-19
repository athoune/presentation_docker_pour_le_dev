#!/usr/bin/env python
from contextlib import closing
import requests

from statsd.defaults.env import statsd

url = 'http://cdimage.debian.org/debian-cd/7.7.0/amd64/iso-cd/debian-7.7.0-amd64-netinst.iso'
with closing(requests.get(url, stream=True)) as r:
    with open('debian.iso', 'w') as f:
        for bloc in r.iter_content(chunk_size=2048):
            f.write(bloc)
            statsd.incr('debian', len(bloc))
