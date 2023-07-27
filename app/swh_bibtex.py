import subprocess
from string import Template
from datetime import datetime
import json
import sys
import argparse
import tempfile
import os
import requests


import pathlib
HEREPATH = pathlib.Path(__file__).parent.absolute()

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

def init_req(url):
    req_url = f"https://archive.softwareheritage.org/api/1/origin/{url}/get/"
    req = requests.get(req_url)
    return req.json()

def run_req(url):
    req = requests.get(url)
    return req.json()

def get_info_from_url(url):
    infos = url.split('/')
    return (infos[-1], infos[-2])
    
BIBTEX_ENTRY_TEMPLATE = """
@software{$entry,
    name = {$repo_name},
    author = {$repo_author},
    url = {$url},
    year = {$year},
    swhid = {$swhid}
}    
"""

def generate_single_entry(url):
    repo_name, repo_author = get_info_from_url(url)
    entry = repo_name
    data = init_req(url)
    visit_url = data['origin_visits_url']
    data_visit = run_req(visit_url)
    last_snapshot = data_visit[0]
    data_snapshot = run_req(last_snapshot['snapshot_url'])
    main_branch_url = data_snapshot['branches']['HEAD']['target_url']
    data_main_branch = run_req(main_branch_url)

    date = data_main_branch["date"]
    year = date[:4]
    dir = data_main_branch["directory"]
    swhid = f"swh:1:dir:{dir};origin={url};"

    t = Template(BIBTEX_ENTRY_TEMPLATE)
    return t.substitute(
        entry = entry,
        repo_name = repo_name,
        repo_author = repo_author,
        url = url,
        year = year,
        swhid = swhid,
    )
    
def main():
    parser = argparse.ArgumentParser(
                    prog='swh_bibtex',
                    description='Generate the bibtex entry for a software')

    parser.add_argument('url', action="append", nargs='+')
    args = parser.parse_args()
    urls = args.url[0]

    for url in urls:
        try:
            print(generate_single_entry(url))
        except:
            print(f"No available snapshot for {url}",file=sys.stderr)
    return 0

if __name__ == "__main__":
    main()
