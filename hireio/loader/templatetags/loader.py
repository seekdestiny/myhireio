import simplejson as json

from django import template
from hireio.settings import STATIC_URL, DEBUG

import os
from os.path import join, dirname, abspath

register = template.Library()


def _load_config(app_name):
    with open(join(dirname(__file__), '..', 'config.json')) as f:
        return json.load(f)

def _make_js_ref(file_names):
    ret = ''
    for file_name in file_names:
        dependency = '<script type="text/javascript" src="' + STATIC_URL + file_name + '"></script>'
        ret += dependency
    return ret

def _make_css_ref(file_names):
    ret = ''
    for file_name in file_names:
        dependency = '<link rel="stylesheet" type="text/css" href="' + STATIC_URL + file_name + '" />'
        ret += dependency

    return ret

@register.simple_tag
def load_js_bundle(app_name):
    config_json = _load_config(app_name)

    global_files = config_json['js']['global_js']
    app_dir = app_name.split('/')

    app_files = config_json['js']
    for sub_dir in app_dir:
        app_files = app_files[sub_dir]

    return _make_js_ref(global_files) + _make_js_ref(app_files)

@register.simple_tag
def load_css_bundle(app_name):
    config_json = _load_config(app_name)

    #global_files = config_json['js']['global_js']
    app_dir = app_name.split('/')

    app_files = config_json['css']
    for sub_dir in app_dir:
        app_files = app_files[sub_dir]

    #return _make_js_ref(global_files) + _make_js_ref(app_files)
    return _make_css_ref(app_files)

