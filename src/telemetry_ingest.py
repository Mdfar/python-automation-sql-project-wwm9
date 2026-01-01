import time import random import psycopg2 from datetime import datetime

Database Connection

DB_CONFIG = { "host": "localhost", "database": "factory_db", "user": "admin", "password": "secret_password" }

def simulate_equipment_data(): """Simulates raw sensor data from an industrial PLC/Tool.""" return { "equipment_id": "CNC-001", "power_draw": random.uniform(5.5, 55.0), "vibration": random.uniform(0.1, 2.5), "status": "RUNNING" if random.random() > 0.1 else "IDLE" }

def ingest_data(): conn = psycopg2.connect(**DB_CONFIG) cur = conn.cursor()

print("🚀 Telemetry ingestion started...")
try:
    while True:
        data = simulate_equipment_data()
        cur.execute(
            "INSERT INTO raw_telemetry (equipment_id, power_draw, vibration, status, timestamp) VALUES (%s, %s, %s, %s, %s)",
            (data['equipment_id'], data['power_draw'], data['vibration'], data['status'], datetime.now())
        )
        conn.commit()
        time.sleep(5) # Poll every 5 seconds
except KeyboardInterrupt:
    cur.close()
    conn.close()


if name == "main": ingest_data()