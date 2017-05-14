#!/usr/bin/env python

unitd = (1024.0 * 1024.0)

import subprocess
import math

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
mem_app = us

f = open('/proc/meminfo', 'r')
mils = f.read()
f.close()

ls = mils.split("\n")
ls.pop()
d = {}
for l in ls:
 vs = l.split()
 d[vs[0]] = vs[1]

ram_total = float(d["MemTotal:"])
ram_free = float(d["MemFree:"])
mem_buffers = float(d["Buffers:"])
mem_cached = float(d["Cached:"])

ram_used = ram_total - ram_free
mem_shared = ram_used - mem_buffers - mem_cached - mem_app

mes = "WTF?"

if (mem_shared <= 0):
 mem_shared = math.fabs(mem_shared)
 mes = "Good"

sp = (mem_shared*100.0)/ram_total

print
print "Linux memory analyser v0.1"
print
print "Usable RAM total:        %.3f GB" % (ram_total/unitd)
print "Used RAM:                %.3f GB" % (ram_used/unitd)
print "Used by bufers+cache:    %.3f GB" % ((mem_buffers + mem_cached)/unitd)
print "Used by *programs*:      %.3f GB (%.2f%%)" % (mem_app/unitd, mps)
print "Shared or *unknown*:     %.3f GB (%.2f%%) (%s)" % ((mem_shared/unitd),sp, mes)
print
