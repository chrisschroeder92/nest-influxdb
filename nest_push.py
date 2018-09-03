import sys
import nest

from configobj import ConfigObj
from influxdb import InfluxDBClient

config = ConfigObj(sys.path[0] + '/config.ini')
CLIENT_ID = config['nest']['client_id']
CLIENT_SECRET = config['nest']['client_secret']
ACCESS_TOKEN_CACHE_FILE = config['nest']['access_token_cache_file']
IFLX_HOST = config['influx']['host']
IFLX_PORT = config['influx']['port']
IFLX_USER = config['influx']['user']
IFLX_PASS = config['influx']['pass']
IFLX_DB = config['influx']['database']


# Metrics to loop
metrics = ['mode',
           'hvac_state',
           'fan',
           'fan_timer',
           'temperature',
           'humidity',
           'target',
           'has_leaf',
           'is_using_emergency_heat',
           'online']
    
def send_to_influx(metrics):
    client = InfluxDBClient(IFLX_HOST, IFLX_PORT, IFLX_USER, IFLX_PASS, IFLX_DB)
    print(metrics)
    client.write_points(metrics)


def gather_nest():
    napi = nest.Nest(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token_cache_file=ACCESS_TOKEN_CACHE_FILE)
    if napi.authorization_required:
        print('Go to ' + napi.authorize_url + ' to authorize, then enter PIN below')
        if sys.version_info[0] < 3:
            pin = raw_input("PIN: ")
        else:
            pin = input("PIN: ")
        napi.request_token(pin)


    data = []
    for structure in napi.structures:
        struct_name = structure.name
        for device in structure.thermostats:
            for m in metrics:
                print(m + ": " + str(getattr(device, m)))
                data.append({'measurement': m,
                             'tags': {'structure': struct_name,
                                      'device': device.name},
                             'fields': {'value': getattr(device, m)}})

    return data

if __name__ == '__main__':
    data = gather_nest()
    send_to_influx(data)
