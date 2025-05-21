#!/bin/bash

# Autor: Infraestructura Capa Media
# Descripción: Script stop start MS WebLogic

# VARIABLES GLOBALES
JAVA_HOME=/u01/oracle/java/jdk
DOMAIN_HOME=/u01/oracle/Domains/aserver/CO_DAV_SADE
. ${DOMAIN_HOME}/bin/setDomainEnv.sh
SCRIPT_PATH=~/scripts/startStopAllMS

# Inicializar Programa
echo "
        --> INICIANDO SCRIPT START ALL MS WEBLOGIC <--
"

cd ${SCRIPT_PATH}

java -Dweblogic.security.SSL.ignoreHostnameVerification=true -Dweblogic.security.allowCryptoJDefaultJCEVerification=true -Dweblogic.security.allowCryptoJDefaultPRNG=true -Dweblogic.security.CustomTrustKeystoreType=jks -Dweblogic.security.TrustKeyStore=CustomTrust -Dweblogic.security.CustomTrustKeyStorePassPhrase=changeit -Dweblogic.security.CustomTrustKeyStoreFileName=${JAVA_HOME}/lib/security/cacerts weblogic.WLST ${SCRIPT_PATH}/startStopAllMS.py start
