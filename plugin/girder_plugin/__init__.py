from girder import plugin

from girder_plugin.test_rest import TestRest

class Plugin(plugin.GirderPlugin):
    DISPLAY_NAME = "Test"

    def load(self, info):
        info["apiRoot"].test = TestRest() 
