# NeuroSym

# Instalación

Sigan los siguientes pasos para instalar todas las herramientas que requiere el curso. 

1. El primer paso es instalar **Miniconda**, una distribución de Python minimalista que viene equipado con el gestor de ambientes y paquetes *conda*. Para instalar Miniconda hay que seguir el siguiente [tutorial](https://www.anaconda.com/docs/getting-started/miniconda/main). 

2. Descarguen este proyecto en su computadora, ya sea con Git o descargando el proyecto como un .zip.

3. Abran una terminal y ejecuten el comando de abajo. Esto creará un nuevo ambiente virtual donde instalar los paquetes que requiere el curso.
   ```bash
   conda create -n cursoIEEE
   ``` 

4. Desde la terminal naveguen hacia el directorio donde descargaron el proyecto y ejecuten en secuencia los siguientes comando
   ```bash
   conda activate cursoIEEE
   conda install pip
   pip install -r requisitos.txt
   ```

## Tutorial LMStudio
