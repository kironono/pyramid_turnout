# config: utf-8

import os

from pyramid.response import Response
from pyramid.renderers import render
from pyramid.settings import asbool


def turnout_tween_factory(handler, registry):

    settings = registry.settings
    enabled = asbool(settings.get("turnout.enabled"))
    if not enabled:
        return handler
    template = settings.get("turnout.template")
    settings_file = settings.get("turnout.settings_file")

    def turnout_tween(request):
        show_turnout = os.path.exists(settings_file)
        if show_turnout:
            with open(settings_file, "r", encoding="utf-8") as f:
                message = f.read()
            return Response(render(template, dict(message=message), request),
                            status=503)
        return handler(request)

    return turnout_tween


def includeme(config):
    config.add_tween('pyramid_turnout.turnout_tween_factory')
