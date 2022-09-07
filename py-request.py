import requests, logging
from datetime import datetime

def get_time_instance():
  now = datetime.now()
  format = "%Y-%m-%d %H:%M:%S"
  return now.strftime(format)

url = "https://navisq.puertoangamos.cl/APIWsPortAngTatc/Auth/authenticate"
# Las credenciales se encuentran en la Guía de Integración
obj = {'username': 'username', 'password': 'password'}

response = requests.post(url, json = obj)
token = response.json()['token']

url = "https://navisq.puertoangamos.cl/APIWsPortAngTatc/PortAngTatc/EnviarTatc"
obj = {}

obj = {
  'dcNumeroTatc':             '100001127',
  'dcOperadorTatc':           'C20',
  'dgOperadorTatc':           'Operador Prueba',
  'dcCodigoAduana':           'ADU01',
  'dgCodigoAduana':           'Nombre Prueba Aduana',
  'dcIdCtr':                  'MRKU000000-1',
  'dcPuerto':                 'CLPAG',
  'dcIsocode':                '2210',
  'dcNumeroBl':               'SH1KJ6480400',
  'dcRutOperadorContenedor':  '96653890-2',
  'dgOperadorContenedor':     'HLC',
  'dcRutDeposito':            '96789280-7',
  'dgNombreDeposito':         'Deposito PANG',
  'dcNumeroLloyd':            '9198575',
  'dgViaje':                  '138E',
  'dgNave':                   'NAVE TEST',
  'dcRutAgenteAduana':        '15679146-6',
  'dgNombreAgenteAduana':     'Agencia Aduana Prueba',
  'dcRutCliente':             '15679146-6',
  'dgNombreCliente':          'Cliente Prueba',
  'dgobservacion':            'Datos de Prueba',
  'dgEmisorBl':               'Navis',
  'dfLiberacion':             '2022-02-01 08:00:00'
}

response = requests.post(url, json = obj, headers = {"Authorization": "Bearer " + token})
print(response.text)

logging.basicConfig(filename = 'logs/logTATC-{}.log'.format(get_time_instance()), level = logging.INFO)

if response.status_code == 400 or response.text.__contains__("E"):
  logging.error(response.text)
else:
  logging.info(response.text)