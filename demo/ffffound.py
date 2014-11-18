#!/usr/bin/env python
import gevent

import gevent.monkey
gevent.monkey.patch_all()

import urllib2
import feedparser

from statsd import StatsClient

statsd = StatsClient()

@statsd.timer('slurp')
def slurp(entry):
    path = entry.media_content[0]['url']
    name= path.split('/')[-1]
    d = urllib2.urlopen(path)
    with open(name, 'w') as f:
        f.write(d.read())
        statsd.incr('image')

ffffound = feedparser.parse('http://feeds.feedburner.com/ffffound/everyone')
s = []
for entry in ffffound.entries:
    s.append(gevent.spawn(slurp, entry))

gevent.wait(s)
