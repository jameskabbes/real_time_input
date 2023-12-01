import kabbes_client
from .RealTimeInput import RealTimeInput
from . import params


class Client(RealTimeInput):

    _BASE_DICT = {
        'PLATFORM_SYSTEM': params.PLATFORM_SYSTEM,
        'KEY_MAPPING': params.KEY_MAPPING
    }

    def __init__(self, dict={}):

        d = {}
        d.update(Client._BASE_DICT)
        d.update(dict)

        self.Package = kabbes_client.Package(params._Dir, dict=d)
        self.cfg_rti = self.Package.cfg

        RealTimeInput.__init__(self)
