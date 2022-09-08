# - Descripción del código.
En esta introducción se llevara a cabo una breve explicación de cómo opera o trabaja el código 
que se mostrara más adelante,  a continuación el siguiente código tiene como misión o trabajo 
mandar un tipo de dato "json" en la cual estarán todos los datos del TATC, pero para ello primero debe haber una autenticación con las credenciales que se darán más abajo.


- url = "https://navisq.puertoangamos.cl/APIWsPortAngTatc/Auth/authenticate"

Ya con esto procederá a llamar al método **"POST"** para luego obtener el token de autorización. Luego se reutiliza la variable **"Url"** e inicia con el endpoint: **EnviarTatc**.

Para ir terminando se reutiliza el objeto para llenar los datos del TATC como se puede ver en 
el ejemplo de más abajo.

```python
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
```
Se envía nuevamente la petición mediante el **"POST"** a la nueva url y se imprime la respuesta por la consola, como penúltimo paso se genera un archivo del log de la siguiente manera: *logging.basicConfig(filename = 'logs/logTATC-{}.log'.format(get_time_instance()), level = logging.INFO). 

Por ultimo se ingresa la respuesta dada por el servidor que bien podría ser por un código **"400"** o por el contrario la petición.