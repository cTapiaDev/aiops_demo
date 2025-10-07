# Simulación de AIOps y Auto-Remediación con Prometheus

Este proyecto demuestra un flujo completo de monitoreo, alerta y auto-remediación utilizando Docker, Prometheus, Alertmanager y un webhook personalizado en Python. El objetivo es simular el comportamiento de una plataforma AIOps que detecta incidentes, los agrupa y genera acciones automáticas de respuesta.

## 🎯 Conceptos Clave Demostrados

-   **Detección de Incidentes**: Prometheus monitorea activamente los servicios y genera alertas basadas en reglas predefinidas.
-   **Enrutamiento y Agrupación**: Alertmanager recibe las alertas, las de-duplica para evitar "ruido" y las enruta al canal de notificación correcto.
-   **Acción Automática (Auto-Remediación)**: Un webhook en Python recibe la notificación y ejecuta una lógica predefinida (un "runbook"), simulando una acción correctiva.
-   **Reducción de Tiempos (MTTR)**: Se visualiza cómo la automatización disminuye drásticamente el tiempo entre la detección de un problema y la ejecución de una primera acción de respuesta.

## 📂 Estructura del Proyecto

```
.
├── alertmanager/
│   └── alertmanager.yml
├── prometheus/
│   ├── prometheus.yml
│   └── alert.rules.yml                 
├── docker-compose.yml          
├── webhook_server.py        
├── .gitignore       
└── README.md 
```

## 🛠️ Prerrequisitos

Para ejecutar este proyecto, necesitas tener instalado:

-   [Docker](https://www.docker.com/get-started/)
-   [Docker Compose](https://docs.docker.com/compose/install/)
-   [Python 3](https://www.python.org/downloads/)

## ⚙️ Preparación del Entorno

1.  **Clona o descarga este repositorio.**

2.  **Crea un entorno virtual para Python:**
    ```bash
    python -m venv .venv
    ```

3.  **Activa el entorno virtual:**
    -   En Windows:
        ```bash
        .\.venv\Scripts\activate
        ```
    -   En macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

4.  **Instala las dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Asegúrate de tener un archivo `requirements.txt` con el contenido `Flask`)*

## 🚀 Pasos para la Demostración

Para una demostración efectiva, se recomienda tener abiertas 2 ventanas de terminal y 3 pestañas en el navegador.

### Paso 1: Iniciar el Webhook de Remediación

En la **primera terminal**, inicia el servidor Python. Este actuará como nuestro "robot reparador", a la espera de recibir alertas.

```bash
python webhook_server.py
```

### Paso 2: Iniciar la Pila de Monitoreo

En la **segunda terminal**, levanta los servicios de Prometheus y Alertmanager usando Docker Compose.

```bash
docker-compose up -d
```

### Paso 3: Observar el Flujo de AIOps en Acción

Espera aproximadamente 30 segundos para que el sistema detecte la falla simulada (`fake_service`) y observa el flujo:

1.  **Detección (Prometheus):**
    -   Abre en tu navegador: `http://localhost:9091/alerts`
    -   Verás la alerta `FakeServiceDown` en estado **ROJO (FIRING)**.
    -   *Explicación:* El "vigilante" ha detectado la falla y ha sonado la alarma.

2.  **Enrutamiento (Alertmanager):**
    -   Abre en tu navegador: `http://localhost:9093`
    -   Verás la misma alerta recibida y procesada.
    -   *Explicación:* El "director" ha recibido la alarma y la ha enviado al canal correcto: nuestro webhook.

3.  **Acción (Webhook y Log):**
    -   Revisa la **primera terminal**. Verás el mensaje `"¡Alerta recibida de Alertmanager!"`.
    -   Abre el archivo `remediation_log.txt` en tu editor de código. Verás el incidente registrado.
    -   *Explicación:* El "robot reparador" recibió la notificación y ejecutó su tarea, dejando evidencia de la acción.

## 🧹 Limpieza del Entorno

Una vez finalizada la demostración, puedes apagar todo:

1.  **Detén los contenedores de Docker:**
    ```bash
    docker-compose down
    ```

2.  **Detén el servidor Python:**
    -   Ve a la primera terminal y presiona `Ctrl + C`.
