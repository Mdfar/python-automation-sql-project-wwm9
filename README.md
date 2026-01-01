Industrial Uptime Automation
Project Overview

This project demonstrates an end-to-end pipeline:

Data Collection: telemetry_ingest.py mimics live PLC data.

Analysis: SQL Views handle the heavy lifting of state-duration calculations.

Automation: insights_generator.py produces visual reports on demand.

Quick Start

Ensure PostgreSQL is running.

Execute sql/schema_and_analysis.sql.

Run python src/telemetry_ingest.py to begin data flow.

Run python src/insights_generator.py to view efficiency charts.