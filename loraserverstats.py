#!/usr/bin/env python
import requests
import certifi
import json
import yaml

cfg_file = "lsstats.yml"
cfg = {}
with open(cfg_file, "r") as ymlfile:
    cfg = yaml.load(ymlfile)

auth_data = {
        "username": cfg['server']['auth']['username'],
        "password": cfg['server']['auth']['password']
        }

auth_request = requests.post(
        cfg['server']['uri']+"/api/internal/login",
        json = auth_data,
        verify = False
        )

auth_tok = auth_request.json()

print(json.dumps(auth_tok))
