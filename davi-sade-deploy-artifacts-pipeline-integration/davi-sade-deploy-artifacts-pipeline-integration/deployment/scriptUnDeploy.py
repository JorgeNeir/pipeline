#!/usr/bin/python
# -*- coding: utf-8 -*-

from java.io import FileInputStream
from java.io import FileOutputStream
import sys

import os
import re
from java.io import FileInputStream

print serverName
print version

#Lee el archivo de configuracion
scriptPath = sys.argv[1]
print scriptPath
propInputStream = FileInputStream(scriptPath + "deployment.properties")
configProps = Properties()
configProps.load(propInputStream)

#Enviar el log de resultado a un archivo
redirect(scriptPath + 'scriptUnDeploy.log', 'true')
#CARGAR PARAMETROS DE ARCHIVO .properties
props = Properties()
archivo_propiedades = "/u01/oracle/Domains/aserver/seguridad/dominio.properties"
propsInputStream = FileInputStream(archivo_propiedades)
props.load(propsInputStream)

#Inicia una sesión en el servidor
connect(userConfigFile='/u01/oracle/Domains/aserver/seguridad/userwl.secure', userKeyFile='/u01/oracle/Domains/aserver/seguridad/passwl.secure', url=props.getProperty("urlwl"))


dName=cmo.getName()
print 'Conectado al dominio: ' + dName

apps=cmo.getAppDeployments()

#Instala las aplicaciones y librerias
cantidadApps=int(configProps.get("undeploy.cantidad"))
i = cantidadApps
while i > 0:
        #deployNombreFile=configProps.get('undeploy.'+str(i)+'.nombre')
        deployNombreConsole=configProps.get('undeploy.'+str(i)+'.nameConsole')
        for app in apps:
            appName=app.getName()
            if appName == deployNombreConsole:
                redirect(scriptPath + 'scriptUnDeploy.log', 'true')
                print appName
                cd('/AppDeployments/'+ appName)
                rutaDespliegue=cmo.getAbsoluteSourcePath()
                appType= cmo.getModuleType()
                print '++ Realizando copia artefacto: ' + appName + '.' + appType
                print ''
                os.system('cp ' + rutaDespliegue + ' ' + rutaDespliegue + '-`date +%Y%m%d-%H:%M`')
                edit()
                startEdit()
                print '++ Desinstalando app: ' + appName
                print ''
                undeploy(appName)
                print ''
                save()
                activate()
        i=i-1
print '++ Script ejecutado ++'

#Detiene la escritura en el archivo de log
stopRedirect()
exit()