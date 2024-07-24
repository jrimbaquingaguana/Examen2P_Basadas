# Evaluación U2 Cantuña - Imbaquinga
## Pasos para la Ejecución del Despliegue del Modelo

### Requisitos Previos
Antes de comenzar, asegúrate de tener lo siguiente:
- Python instalado (preferentemente versión 3.7 o superior).
- Git instalado en tu máquina.
- Un editor de código, como Visual Studio Code (VSCode).

### Pasos a Seguir

#### 1. Clonar el Repositorio
Primero, clona el repositorio desde GitHub a tu máquina local. Abre una terminal y ejecuta:

```bash
git clone https://github.com/jrimbaquingaguana/Examen2P_Basadas.git
```
#### 2. Abrir el Proyecto en Visual Studio Code
Una vez completado el proceso de clonación, abre la carpeta del proyecto con Visual Studio Code (VSCode).

#### 3. Activar el Entorno Virtual
Abre una terminal dentro de la raíz del proyecto y ejecuta el siguiente comando para activar el entorno virtual de Python:
```bash
myenv\Scripts\activate
```
#### 4. Instalar las Dependencias
Una vez iniciado el entorno virtual, instala las dependencias necesarias para el proyecto con el siguiente comando:
```bash
pip install flask scikit-learn numpy joblib
```

#### 5. Iniciar el Servidor
Después de completar la instalación, inicia el servidor ejecutando el siguiente comando:
```bash
python app.py
```
Esto iniciará el servidor y abrirá una pestaña en el navegador para poder utilizar el modelo.

### Aspectos a Tener en Cuenta
- Versiones de las Dependencias: Asegúrate de que las versiones de las dependencias sean compatibles con tu versión de Python.
- Configuración del Entorno Virtual: Si myenv\Scripts\activate no funciona, asegúrate de que myenv es el nombre correcto de tu entorno virtual y que estás en la carpeta correcta.
- Permisos de Red: Si estás utilizando un firewall, asegúrate de permitir las conexiones al puerto en el que Flask está ejecutando el servidor.


