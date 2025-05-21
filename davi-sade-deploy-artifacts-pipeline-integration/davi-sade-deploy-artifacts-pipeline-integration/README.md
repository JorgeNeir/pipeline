# davi-sade-deploy-artifacts-pipeline

## Pipeline de Implementación de Artefactos en WebLogic
Este repositorio tiene el objetivo de automatizar el proceso de implementación de artefactos en un entorno de WebLogic y base de datos postgresql en las ramas que gestionan los ambientes de desarrollo, laboratorio y producción. Se utiliza GitHub Actions para recuperar los artefactos desde un servidor de artefactos JFrog y luego desplegarlos en el entorno adecuado para cada ambiente.

A continuacion se describe de manera general el funcionamiento del pipeline, esperando sea de utilidad para los procesos de despliegue futuros.

## Configuraciones
- **`permissions`:** Define los permisos necesarios para acceder a los recursos de GitHub.
- **Variables de Entorno (`env`):** Establece variables de entorno que son utilizadas en el pipeline para identificar los nombres de los artefactos, rutas de almacenamiento, entre otros.

## Trabajos (Jobs)

### `retrieve-artifact`
Este trabajo recupera los artefactos desde un servidor de artefactos JFrog. Realiza los siguientes pasos:

1. **`Leyendo variables del archivo de propiedades`:** Lee las variables de configuración desde el archivo deploy.properties y las almacena como variables de entorno.

2. **`⬇️ Checkout Retrive Action`:** Descarga del Action reutilizable empleado para recuperar artefactos desde JFrog.

3. **`📥 download artifacts from jfrog`:** Descarga los artefactos desde JFrog basándose en las variables de configuración proporcionadas.

4. **`📥 download artifact SQL from jfrog`:** Descarga los artefactos SQL desde JFrog basándose en las variables de configuración proporcionadas.

5. **`🚀📤 Upload EAR artifact`:** Sube los artefactos EAR a GitHub Actions como artefactos del Action.

6. **`🚀📤 Upload SQL artifact`:** Sube los artefactos SQL a GitHub Actions como artefactos del Action


### `deployment`
Este trabajo implementa los artefactos en el entorno de integración de WebLogic. Utiliza un flujo de trabajo de implementación no reutilizable proporcionado por Davivienda Colombia.

Para obtener más detalles sobre la documentación y cambios en el pipeline, consulta el [Archivo de información esencial del proyecto (README)](https://github.com/davivienda-colombia/davi-sade-deploy-artifacts-pipeline/blob/main/README.md).

## Personalización

Puedes personalizar este pipeline ajustando las siguientes configuraciones:

- Modificar las variables de entorno para reflejar tus nombres de artefactos, rutas de almacenamiento y otras configuraciones específicas de tu proyecto.
- Ajustar los pasos del trabajo `retrieve-artifact` para adaptarse a tu servidor de artefactos o repositorio de artefactos.
- Personalizar los pasos del trabajo `deployment` para adaptarse a tus necesidades de implementación específicas para el entorno de WebLogic.
- Si se envían valores para WebLogic (nombre de artefacto y tipo de paquete), se procederá a desplegar la versión especificada en el entorno de WebLogic. Si no se envían valores para WebLogic, no se realizará ningún despliegue en este entorno.
- Si se envían valores para SQL (nombre de artefacto y tipo de paquete), se ejecutará el script SQL especificado en la base de datos. Si no se envían valores para SQL, no se ejecutará ningún script SQL.


## Configuraciones de Despliegue para WebLogic y BD postgresql

En el archivo deploy.properties se pueden modificar las configuraciones de ejecución según las necesidades específicas del despliegue.

### deploy.properties

En este archivo se detallan las configuraciones necesarias para el despliegue de artefactos en un entorno de WebLogic, así como la ejecución de scripts en una base de datos asociada (postgresql).

#### Tipo de Despliegue

La variable `$deploy_deploy_type_ear` especifica el tipo de despliegue para los artefactos de WebLogic. Los tipos disponibles son:

- `cash4u`
- `transportadora`
- `web-services`
- `migrador`

Cada tipo representa un contexto específico para el despliegue de los artefactos.

#### Tipo de Paquete

La variable `$deploy_package_type_ear` indica el tipo de paquete que puede ser desplegado en WebLogic. Los tipos disponibles son:

- `ear`: Enterprise Archive
- `sql`: Scripts SQL

Dependiendo del tipo de paquete seleccionado, el proceso de despliegue variará.

#### Versión a Remover WebLogic

La variable `$undeploy_artifact_ear_name_file` especifica la versión del artefacto que se eliminará del entorno de WebLogic antes de realizar un nuevo despliegue. Si este valor está vacío, no se eliminará ninguna versión.

#### Versión Despliegue WebLogic

Las variables `$deploy_artifact_ear_name_file`, `$deploy_package_type_ear` y `$deploy_deploy_type_ear` definen la versión del artefacto que será desplegada en el entorno de WebLogic, junto con su tipo de paquete y tipo de despliegue.

#### Versión Despliegue Base de Datos (postgresql)

Las variables `$execute_artifact_sql_name_file`, `$execute_package_type_sql` y `$execute_deploy_type_sql` especifican la versión del artefacto que será ejecutada en la base de datos, junto con su tipo de paquete y tipo de despliegue. Si se proporcionan valores en esta sección, se ejecutará el script SQL correspondiente en la base de datos.


Este README proporciona una descripción general del pipeline y las configuraciones básicas. Para obtener más detalles sobre el funcionamiento específico de cada paso y cómo personalizarlo para tu caso de uso, consulta la documentación adicional proporcionada por Davivienda Colombia.
