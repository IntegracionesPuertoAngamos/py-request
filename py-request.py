import os, requests, logging
from datetime import datetime

# Función de ayuda para obtener una instancia del tiempo en formato YYYY-MM-DD HH:MM:SS
def get_time_instance():
  now = datetime.now()
  format = "%Y-%m-%d %H:%M:%S"
  return now.strftime(format)

# Declaramos la url de autenticación y el objeto usuario
url = "https://navisq.puertoangamos.cl/APIWsPortAngTatc/Auth/authenticate"
# Las credenciales se encuentran en la Guía de Integración
obj = {'username': 'username', 'password': 'password'}

# Enviamos la peticion mediante el método POST
response = requests.post(url, json = obj)

# Obtenemos el token de autorización
token = response.json()['token']

# Reutilizamos la variable Url e inicializamos con el enpdoint EnviarTatc
url = "https://navisq.puertoangamos.cl/APIWsPortAngTatc/PortAngTatc/EnviarTatc"
obj = {}

# Reutilizamos el objeto para llenar con datos del TATC
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

# Enviamos nuevamente la petición mediante el método POST a la nueva url e imprimimos la respuesta por consola
response = requests.post(url, json = obj, headers = {"Authorization": "Bearer " + token})
print(response.text)

# Generamos un archivo de log
os.mkdir('logs')
logging.basicConfig(filename = 'logs/logTATC-{}.log'.format(get_time_instance()), level = logging.INFO)

# Ingresamos la respuesta dada por el servidor
if response.status_code == 400 or response.text.__contains__("E"):
  logging.error(response.text)
else:
  logging.info(response.text)

# Reutilizamos la variable Url e inicializamos con el enpdoint AnularTatc
url = "https://navisq.puertoangamos.cl/APIWsPortAngTatc/PortAngTatc/AnularTatc"
obj = {}

# Reutilizamos el objeto para llenar con datos del TATC
obj = {
  'dcNumeroTatc':             '100001127',
  'dcOperadorTatc':           'C20',
}

# Enviamos nuevamente la petición mediante el método POST a la nueva url e imprimimos la respuesta por consola
response = requests.post(url, json = obj, headers = {"Authorization": "Bearer " + token})
print(response.text)

# Ingresamos la respuesta dada por el servidor
if response.status_code == 400 or response.text.__contains__("E"):
  logging.error(response.text)
else:
  logging.info(response.text)