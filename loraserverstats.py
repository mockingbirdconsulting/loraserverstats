#!/usr/bin/env python
import requests
import certifi
import json
import yaml

cfg_file = "lsstats.yml"
cfg = {}
with open(cfg_file, "r") as ymlfile:
    cfg = yaml.load(ymlfile)

auth_request = requests.post(
        cfg['server']['uri']+"/api/internal/login",
        json = cfg['server']['auth']
        )

auth_tok = auth_request.json()

jwt = auth_tok['jwt']

#print(jwt)

auth_header = {"Grpc-Metadata-Authorization": jwt}

stats = {}
for qtype in ['organizations','applications','gateways', 'devices']:
    stats[qtype] = requests.get(
            cfg['server']['uri']+"/api/%s" % qtype,
            headers = auth_header
            ).json()['totalCount']


print(stats)
