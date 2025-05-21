# -*- coding: utf-8 -*-
#Modificado por: Manuel Alejandro Murcia
#Fecha: 15-02-2024
#Descripcion: Se conecta con dominio WLS y ejecuta despliegue segun lo configurado en el archivo deployment.properties

from java.io import FileInputStream
from java.io import FileOutputStream
import sys

print serverName
print version

#Lee el archivo de configuracion
scriptPath = sys.argv[1]

propInputStream = FileInputStream(scriptPath + 'deployment.properties')
configProps = Properties()
configProps.load(propInputStream)

#Propiedades de reverso de la instalacion
undeployProps = Properties()

#Enviar el log de resultado a un archivo
redirect(scriptPath + 'scriptDeploy.log', 'true')

ruta_despliegue=sys.argv[2]

#CARGAR PARAMETROS DE ARCHIVO .properties
props = Properties()
archivo_propiedades = "/u01/oracle/Domains/aserver/seguridad/dominio.properties"
propsInputStream = FileInputStream(archivo_propiedades)
props.load(propsInputStream)

#Inicia una sesión el servidor
connect(userConfigFile='/u01/oracle/Domains/aserver/seguridad/userwl.secure', userKeyFile='/u01/oracle/Domains/aserver/seguridad/passwl.secure', url=props.getProperty("urlwl"))

#Obtiene la lista de las librerias que actualmente estan instaladas
serverLibs =cmo.getLibraries()
serverLibsDict = dict()
for i in range(len(serverLibs)):
    nameParts = serverLibs[i].getName().split('#')
    if (len(nameParts) == 1):
        nameParts = serverLibs[i].getName()
    nameSubParts=nameParts[1].split('@')
    if (len(nameSubParts) == 1):
        nameSubParts = nameParts
    serverLibsDict[serverLibs[i].getName()]=nameSubParts

#Obtiene la lista de las aplicaciones que actualmente estan instaladas
serverApps =cmo.getAppDeployments()
serverAppsDict = dict()
for i in range(len(serverApps)):
    serverAppsDict[serverApps[i].getName()]="EXISTE"

#Obtiene el destino (servidor o cluster) en el que se instalaran las aplicaciones
deployDestino=configProps.get("deploy.target")

#Instala las aplicaciones
cantidadApps=int(configProps.get("deploy.cantidad"))+1
try:
    for i in range(1, cantidadApps):
        deployNombre=configProps.get('deploy.'+str(i)+'.nombre')
        deploySpecVersion=configProps.get('deploy.'+str(i)+'.spec.version')
        deployNameConsole=configProps.get('deploy.'+str(i)+'.nameConsole')

        deployTipo=configProps.get('deploy.'+str(i)+'.tipo')

        deployNombreCompleto=deployNombre
        esLibreria='false'
        nombreArchivo = ''
        if(deployTipo=='lib'):
            esLibreria='true'
            deployNombreCompleto+='#'+deploySpecVersion+'@'+deployImplVersion

        if (deployTipo == 'lib') & (deployNombreCompleto in serverLibsDict):
            print 'LIBRERIA ' + deployNombre + ' YA ESTA INSTALADA'

        elif deployNombreCompleto in serverAppsDict:
            print 'APLICACION: ' + deployNombre + ' YA ESTA INSTALADA'

        else:
            if esLibreria=='true':
                nombreArchivo = deployNombre + '.jar'
                print 'SE INSTALARA LIBRERIA: ' + deployNombre + ', VERSION: ' + deployImplVersion
            else:
                nombreArchivo = deployNombre
                print 'SE INSTALARA APLICACION: '+ nombreArchivo

            try:
                edit()
                startEdit()
                deploy(deployNameConsole, ruta_despliegue + nombreArchivo, targets=deployDestino, libraryModule=esLibreria)
                save()
                activate(block="true")
                progress=startApplication(deployNameConsole)
                print 'Se instalo correctamente : '+deployNombre+' esLibreria='+esLibreria
            except:
                print >> sys.stderr, 'NO FUE POSIBLE DESPLEGAR EL COMPONENTE: ' + deployNombre
                print >> sys.stderr, 'LA INSTALACION SE DETUVO'
                undo(defaultAnswer='y', unactivatedChanges='true')
                stopEdit('y')

except:
        print >> sys.stderr, 'NO FUE POSIBLE DESPLEGAR EL COMPONENTE: ' + nombreArchivo
        print >> sys.stderr, 'LA INSTALACION SE DETUVO'
        undo(defaultAnswer='y', unactivatedChanges='true')
        stopEdit('y')

disconnect()

print 'INSTALACION TERMINADA'

#Detiene la escritura en el archivo de log
stopRedirect()
exit()