import pandas as pd import psycopg2 import matplotlib.pyplot as plt

def generate_report(): conn = psycopg2.connect(host="localhost", database="factory_db", user="admin", password="secret_password")

# Analyze Uptime vs Downtime via SQL
query = "SELECT state, SUM(duration_minutes) as total FROM equipment_performance GROUP BY state"
df = pd.read_sql(query, conn)

# Generate Chart
df.set_index('state').plot(kind='pie', y='total', autopct='%1.1f%%', title="Equipment Uptime Distribution")
plt.savefig('output/uptime_report.png')
print("📊 Report generated: output/uptime_report.png")

conn.close()


if name == "main": generate_report()