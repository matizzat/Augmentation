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
1. Descargar e instalar LM Studio

Dirígete al sitio oficial y descarga el instalador adecuado para tu sistema operativo.
LM Studio
[lmstudio.id](https://lmstudio.ai/).

Ejecuta el instalador y sigue el asistente — es un proceso simple e intuitivo.

Asegúrate de que tu equipo cumpla los requisitos mínimos.

2. Descargar y cargar un modelo

Abre LM Studio y ve a la pestaña “Discover” o "Descubrir", (la lupa al lado Izquierdo).

Busca modelos en la biblioteca integrada (por ejemplo, Llama, Mistral 7B, etc.) y descarga la versión compatible (como GGUF, optimizada para ejecución local).

Elige un modelo que sea compatible con tu hardware. LM Studio ofrece indicadores mediante colores:

Verde: tu equipo puede usar GPU si está disponible (óptimo).

Celeste: es parcial, con suerte funcionará bien.

Rojo: probablemente no funcione bien en tu máquina.

Una vez descargado, ve a la pestaña “Chat”, usa Ctrl + L (Windows/Linux) o ⌘ + L (macOS) para abrir el cargador de modelos, selecciona el modelo e inicia su carga en memoria. o en su defecto selecciona en la barra que esta en la parte superior de la pantalla.

3. Probar el modelo

En la pestaña “Chat”, escribe una pregunta (por ejemplo: “¿Qué es LM Studio y para qué sirve?”).
Presiona Enter y observa cómo el modelo genera una respuesta localmente 
Si lo deseas, explora los ajustes como temperatura, longitud máxima de contexto, número de tokens, etc., en la sección de configuración 
