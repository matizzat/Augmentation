# Instalación

Sigan los siguientes pasos para instalar todas las herramientas que requiere el curso. 

## Miniconda y paquetes
Miniconda es una distribución de Python minimalista que viene equipado con el gestor de ambientes y paquetes *conda*. Para instalar esta herramienta y los paquetes que requiere el curso sigan los siguientes pasos: 

1. Descargar Miniconda siguiendo este [tutorial](https://www.anaconda.com/docs/getting-started/miniconda/main). 
2. Descargar este proyecto  con Git o como un `.zip`.
3. Desde una terminal ejecutar el siguiente comando: 
   ```bash
   conda create -n cursoIEEE
   ``` 
4. Desde una terminal navegar hacia el directorio donde se descargó el proyecto y ejecutar en secuencia los siguientes comandos
   ```bash
   conda activate cursoIEEE
   conda install pip
   pip install -r requisitos.txt
   ```

## LMStudio
