#!/usr/bin/env python

import subprocess

o = subprocess.check_output("ps aux --sort -rss", shell=True)

ls = o.split("\n")
ls.pop(0)
ls.pop()

mps = 0.0
us = 0.0

for l in ls:
  vs = l.split()
  mp = vs[3]
  mrss = vs[5]
  mps += float(mp)
  us += float(mrss)


print "usage percent %d %%" % mps

u = 16431416 * (mps / 100.0)

print "usage manual  %d kb" % u


print "usage RSS  %d kb" % us


