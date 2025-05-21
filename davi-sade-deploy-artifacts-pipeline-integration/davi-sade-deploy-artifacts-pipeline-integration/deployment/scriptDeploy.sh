#!/bin/bash

# Autor: Infraestructura Capa Media
# Descripción: Script automatización despliegues WebLogic 

# VARIABLES GLOBALES
DOMAIN_HOME=/u01/oracle/Domains/aserver/CO_DAV_SADE
. ${DOMAIN_HOME}/bin/setDomainEnv.sh

SCRIPT_PATH=~/scripts/deployment
JAVA_HOME=/u01/oracle/java/jdk

# Inicializar Programa
echo "
	--> INICIANDO SCRIPT DEPLOYMENT APPS <--
" 

cd ~/scripts/deployment/

java -Dweblogic.security.SSL.ignoreHostnameVerification=true -Dweblogic.security.allowCryptoJDefaultJCEVerification=true -Dweblogic.security.allowCryptoJDefaultPRNG=true -Dweblogic.security.CustomTrustKeystoreType=jks -Dweblogic.security.TrustKeyStore=CustomTrust -Dweblogic.security.CustomTrustKeyStorePassPhrase=changeit -Dweblogic.security.CustomTrustKeyStoreFileName=${JAVA_HOME}/lib/security/cacerts weblogic.WLST ${SCRIPT_PATH}/scriptDeploy.py ${SCRIPT_PATH}/ ${DOMAIN_HOME}/servers/AdminServer/upload/
