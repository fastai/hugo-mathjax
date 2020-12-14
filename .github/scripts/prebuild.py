#!/usr/bin/env python

from fastcore.utils import *
from ghapi.all import *

def rel_tag():
    tag = GhApi().repos.get_latest_release('gohugoio', repo='hugo').name
    api = GhApi(owner='fastai', repo='hugo-mathjax', token=github_token())
    try: return api.repos.get_release_by_tag(tag)
    except HTTP404NotFoundError: pass

    rel = api.repos.create_release(tag, name=tag)
    print(f'New release: {tag}')
    actions_output('tag', tag)

rel_tag()
