#!/usr/bin/env python3

import random
import requests
import sys
import time

with open(sys.argv[1], 'r') as domainfile:
    domains = domainfile.readlines()

while True:
    d = random.choice(domains).strip()
    t = random.randint(0, 300)
    print(d, t)
    try:
        r = requests.get("https://{}".format(d), timeout=2)
        print(r.status_code)
    except (requests.exceptions.ConnectionError, requests.exceptions.SSLError):
        try:
            r = requests.get("http://{}".format(d), timeout=2)
            print(r.status_code)
        except:
            pass
    except:
        pass

    time.sleep(t)

