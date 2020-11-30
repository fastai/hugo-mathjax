#!/usr/bin/env python

from fastcore.utils import *
from ghapi import *
import tarfile

def rel_tag():
    api = GhApi(owner='fastai', repo='hugo-mathjax', token=os.environ['GITHUB_TOKEN'])
    tag = GhApi().repos.get_latest_release('gohugoio', repo='hugo').name
    try: return api.repos.get_release_by_tag(tag)
    except HTTP404NotFoundError: pass

    rel = api.repos.create_release(tag, name=tag)
    actions_output('tag', tag)

rel_tag()
