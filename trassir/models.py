from django.db import models
import json, requests
import logging

# Logging configuration
py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.DEBUG)
py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
py_handler.setFormatter(py_formatter)
py_logger.addHandler(py_handler)


# Create your models here.

class NVR(models.Model):
    ip = models.CharField(max_length=100, unique=True)
    port = models.IntegerField(default=80)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    sdk_password = models.CharField(max_length=100)
    name = models.CharField(max_length=200, editable=False)

    def __str__(self):
        return self.name

    @staticmethod
    def make_request(command, username=None, password=None, sdk_password=None, session_id=None, ip='127.0.0.1',
                     port='8080'):
        request_string = f'https://{ip}:{port}/{command}'
        if session_id:
            request_string += '?sid=' + session_id
        elif sdk_password:
            request_string += '?password=' + sdk_password
        elif username and password:
            request_string += '?username=' + username + '&password=' + password
        else:
            raise Exception('please provide session')
        py_logger.debug('Trying request: ' + request_string)

        try:
            r = requests.get(request_string, verify=False, timeout=3)
            py_logger.debug('Response status_code = ' + str(r.status_code))
            py_logger.debug(r.text)

            if r.status_code == 200:
                return json.loads(r.text)

        except (ConnectionError, requests.exceptions.ReadTimeout):
            py_logger.warning('Connection Error, ip=' + ip)
            # raise Exception('ConnectionError')
            return 'error'
        except(requests.exceptions.ConnectTimeout):
            py_logger.warning('Connection Error, ip=' + ip)
            # raise Exception('ConnectionError')
            return 'error'
        except (requests.exceptions.SSLError):
            py_logger.warning('SSL error, ip=' + ip)
            # raise Exception('ConnectionError')
            return 'error'

    def get_health(self):
        health = NVR.make_request(command='health', username=self.username,
                                  password=self.password,
                                  sdk_password=self.sdk_password,
                                  ip=str(self.ip))

        return health
