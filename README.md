# nest-influxdb
Import stats into InfluxDB from the Nest API

Script was originally created by kremlinekev in `nest_influx <https://github.com/kremlinkev/nest_influx>`_ and adapted to use the new Nest API, using `python-nest <https://github.com/jkoelker/python-nest>`_

## Setup Steps

1. Follow the instructions on `python-nest <https://github.com/jkoelker/python-nest#nest-developer-account>`_ to setup a Nest Developer account.

2. Install requierements from requirements.txt:
```bash
$ pip install -r requirements.txt
```

3. Copy `config.ini.example` to `config.ini` and edit with your information for the Nest account and InfluxDB

4. Make sure the `nest` database exists in your InfluxDB

5. At the first run, you will need to authorize this app through your Developer account.  Follow the link instructions and paste the PIN to activate.
