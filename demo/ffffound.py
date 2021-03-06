#!/usr/bin/env python
import gevent

import gevent.monkey
gevent.monkey.patch_all()

import urllib2
import feedparser

from statsd.defaults.env import statsd

def wget(url):
    d = urllib2.urlopen(url)
    with open(name, 'w') as f:
        f.write(d.read())

@statsd.timer('slurp')
def slurp(entry):
    statsd.incr('workers')
    for url in [entry.media_content[0]['url'], entry.ffffound_source['url']]:
        try:
            wget(url)
        except :
            statsd.incr('error')
    statsd.incr('image')
    statsd.decr('workers')

ffffound = feedparser.parse('http://feeds.feedburner.com/ffffound/everyone')
s = [gevent.spawn(slurp, entry) for entry in ffffound.entries]
gevent.wait(s)
