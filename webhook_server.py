from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_receiver():

    print("¡Alerta recibida de Alertmanager!")
    data = request.json
    
    # Imprime la alerta completa para depuración
    print(json.dumps(data, indent=2))
    
    # Simulación de la acción de auto-remediación
    # En un caso real, aquí iría un comando como 'kubectl rollout restart'
    # o la llamada a un script de Ansible.
    
    # Nuestra acción simple será registrar la alerta en un archivo.
    with open("remediation_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"--- INCIDENTE RECIBIDO a las {timestamp} ---\n")
        for alert in data.get('alerts', []):
            summary = alert.get('annotations', {}).get('summary', 'Sin resumen')
            log_file.write(f"Alerta: {alert.get('labels', {}).get('alertname')}\n")
            log_file.write(f"Resumen: {summary}\n")
            log_file.write(f"Estado: {alert.get('status')}\n\n")
            
    print("Acción de remediación simulada: Se ha escrito en remediation_log.txt")
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)