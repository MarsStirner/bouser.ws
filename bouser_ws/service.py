# -*- coding: utf-8 -*-
from .factory import WsFactory
from .resource import WsResource
from bouser.helpers.plugin_helpers import BouserPlugin, Dependency

__author__ = 'viruzzz-kun'


class WsService(BouserPlugin):
    signal_name = 'bouser.ws'
    web = Dependency('bouser.web')
    cas = Dependency('bouser.castiel')

    def __init__(self, config):
        self.config = config

    @web.on
    def web_boot(self, web):
        factory = WsFactory(self)
        resource = WsResource(factory)
        web.root_resource.putChild('ws', resource)
