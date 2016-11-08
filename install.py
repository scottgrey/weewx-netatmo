# $Id: install.py 1484 2016-04-25 16:20:31Z mwall $
# installer for netatmo driver
# Copyright 2015 Matthew Wall

from setup import ExtensionInstaller

def loader():
    return NetatmoInstaller()

class NetatmoInstaller(ExtensionInstaller):
    def __init__(self):
        super(NetatmoInstaller, self).__init__(
            version="0.6",
            name='netatmo',
            description='Driver for netatmo weather stations.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            config={
                'Station': {
                    'station_type': 'netatmo'},
                'netatmo': {
                    'mode': 'cloud',
                    'username': 'INSERT_USERNAME_HERE',
                    'password': 'INSERT_PASSWORD_HERE',
                    'client_id': 'INSERT_CLIENT_ID_HERE',
                    'client_secret': 'INSERT_CLIENT_SECRET_HERE',
                    'driver': 'user.netatmo'}},
            files=[('bin/user', ['bin/user/netatmo.py'])]
            )
