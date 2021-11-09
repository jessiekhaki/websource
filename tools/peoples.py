#!/usr/bin/env python
from __future__ import print_function
import yaml
import sys

import os.path
import os
from collections import defaultdict

def get_meta(personfile):
    text = open(personfile).read()
    ts = text.split("---")
    ts = "---\n"+ ts[1]
    meta = yaml.load(ts)
    meta = defaultdict(lambda: "", meta)

    return meta

    

def main(people_folder, output_csv):
    people = os.listdir(people_folder)
    print("webid, name, position, orcid, link, newbio, newpersonal")
    for person in people:
        page = os.path.join(people_folder, person)
        if not page.endswith(".html"):
            continue
        if page.endswith("index.html"):
            continue
        if page.endswith("former.html"):
            continue
        meta = get_meta(page)
        if meta['status'] == "former":
            continue
        link = "http://chicas.lancaster-university.uk/people/"+person
        s = "%s, %s, %s, %s, %s, %s, %s" % (meta['username'], meta['title'], meta['status'],meta['orcid'],link,"","")
        print(s)
    
if __name__=="__main__":
    main(sys.argv[1], sys.argv[2])

                        
    
