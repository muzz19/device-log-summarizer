# Device Telemetry Assignment

## Files
- `sensor_readings.py` — cleans and normalizes sensor values.
- `device_log_summarizer.py` — reads the sample CSV, aggregates per-device telemetry, filters devices with average temperature above 80°C, and writes `device_summary.json`.
- `device_temperature_chart.py` — creates `device_temperature_chart.png` from the JSON summary.
- `device_telemetry.csv` — sample input data.
- `device_summary.json` — generated sample output.
- `device_temperature_chart.png` — generated chart output.
- `PROMPT_LOG.md` — AI usage log.

## Requirements
Python 3.9+ and Matplotlib.

Install dependency:
```bash
python -m pip install matplotlib
```

## Run
Run these commands from this folder:
```bash
python sensor_readings.py
python device_log_summarizer.py
python device_temperature_chart.py
```

The telemetry and chart scripts expect `device_telemetry.csv` and `device_summary.json` in the current folder respectively. The included sample files were generated from the included sample CSV. The CSV uses the status values `ACTIVE` and `ERROR` listed in the assessment. Devices with mean temperatures above 80.0°C are excluded from the JSON and chart.
