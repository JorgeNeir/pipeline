import getopt
import sys
import os

from java.util import Properties
from java.io import FileInputStream

# Archivo Propiedades
rutaPropiedades = "/u01/oracle/Domains/aserver/seguridad/dominio.properties"

# Cargar archivo
propiedades = Properties()
propiedades.load(FileInputStream(rutaPropiedades))

print ' # Conectando al dominio WebLogic # '
connect(userConfigFile='/u01/oracle/Domains/aserver/seguridad/userwl.secure', userKeyFile='/u01/oracle/Domains/aserver/seguridad/passwl.secure', url=propiedades.getProperty("urlwl"))
getcommand=sys.argv[1]
print '[INFO] - Comando Ejecutado: ' + getcommand

if getcommand != 'start' and getcommand != 'stop':
  print 'usage: <start|stop> <wls admin username> <wls admin password>'
  exit()

# List of managed instance names this script will control
serverList = cmo.getServers()

# Go to the root of the MBean hierarchy
domainRuntime()

# Start
if getcommand == 'start':
    for server in serverList:
       nombreServidorManejado=server.getName()
       #estadoServidor = getMBean('ServerRuntimes/' + nombreServidorManejado)
       #estadoServidorC = estadoServidor.getState()
       #print '[INFO] - Servidor: ' + nombreServidorManejado + ' esta ' + estadoServidorC
       if nombreServidorManejado != 'AdminServer':
           start(nombreServidorManejado, 'Server', block='false')
           print '[INFO] - Iniciando Server ' + nombreServidorManejado

# Stop
if getcommand == 'stop':
   for server in serverList:
       nombreServidorManejado=server.getName()
       estadoServidor = getMBean('ServerRuntimes/' + nombreServidorManejado)
       estadoServidorC = estadoServidor.getState()
       print '[INFO] - Servidor: ' + nombreServidorManejado + ' esta ' + estadoServidorC
       if nombreServidorManejado != 'AdminServer':
           if estadoServidorC == 'RUNNING' or 'SUSPENDING':
               shutdown(nombreServidorManejado, 'Server', force='true', block='true')
               print '[INFO] - Apagando Server ' + nombreServidorManejado
           else:
               print '[ERROR] - Server ' + nombreServidorManejado + ' es diferente a RUNNING'

print ''
print '[INFO] - IMPORTANTE - Revisa el estado desde la consola administrativa'
disconnect()
exit()
