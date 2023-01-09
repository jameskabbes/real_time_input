import real_time_input
import kabbes_user_client
import py_starter as ps

class Client( real_time_input.RealTimeInput ):

    BASE_CONFIG_DICT = {
        "_Dir": real_time_input._Dir,
        "PLATFORM_SYSTEM": real_time_input.PLATFORM_SYSTEM,
        'KEY_MAPPING': real_time_input.KEY_MAPPING
    }

    def __init__( self, dict={}, **kwargs ):

        dict = ps.merge_dicts( Client.BASE_CONFIG_DICT, dict )
        self.cfg_rti = kabbes_user_client.Client( dict=dict, **kwargs ).cfg
        real_time_input.RealTimeInput.__init__( self )
