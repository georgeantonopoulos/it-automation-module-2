#! /usr/bin/env python3

import os
import requests

# List all txt files under /data/feedback with os.listdir()
# for each make dict {"title":"A", "name": "B", "date":"C", "feedback":"C"}
# x = requests.post(url, data=feedback_dict)
# Abbreviating feedback as fb

fb_dir = "/data/feedback"
url = "http://35.222.145.75/feedback/"

fb_lst = []

for f in os.listdir(fb_dir):

    with open(os.path.join(fb_dir, f)) as fb_txt:
        fb_lst.append(
            {
                "title":fb_txt.readline().rstrip("\n"),
                "name":fb_txt.readline().rstrip("\n"),
                "date":fb_txt.readline().rstrip("\n"),
                "feedback":fb_txt.read().rstrip("\n")
            }
        )

for fb in fb_lst:    
    r = requests.post(url, json=fb)
    if r.status_code != 201:
        raise Exception('POST error status={}'.format(r.status_code))
    print('Created feedback ID: {}'.format(r.json()["id"]))