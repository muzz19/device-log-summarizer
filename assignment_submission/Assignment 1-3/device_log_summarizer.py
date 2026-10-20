import csv
import json
from collections import defaultdict


def process_device_telemetry(input_file, output_file):
    """Aggregate telemetry by device and export eligible device summaries."""
    devices = defaultdict(lambda: {
        "total_records": 0,
        "total_temperature": 0.0,
        "error_count": 0
    })

    with open(input_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required = {"device_id", "status", "temperature"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("CSV must contain device_id, status, and temperature columns.")

        for line_number, row in enumerate(reader, start=2):
            try:
                device_id = row["device_id"].strip()
                status = row["status"].strip().upper()
                temperature = float(row["temperature"])
            except (AttributeError, TypeError, ValueError) as error:
                raise ValueError(f"Invalid data on CSV line {line_number}: {error}") from error

            if not device_id:
                raise ValueError(f"Missing device_id on CSV line {line_number}.")

            devices[device_id]["total_records"] += 1
            devices[device_id]["total_temperature"] += temperature
            if status == "ERROR":
                devices[device_id]["error_count"] += 1

    results = []
    for device_id, data in devices.items():
        average_temperature = data["total_temperature"] / data["total_records"]
        if average_temperature <= 80.0:
            results.append({
                "device_id": device_id,
                "total_records": data["total_records"],
                "average_temperature": round(average_temperature, 2),
                "error_count": data["error_count"]
            })

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print("\nDevice Telemetry Summary")
    print("-" * 68)
    print(f"{'Device ID':<15}{'Total Records':<18}{'Average Temp':<18}{'Error Count':<15}")
    print("-" * 68)
    for device in results:
        print(
            f"{device['device_id']:<15}{device['total_records']:<18}"
            f"{device['average_temperature']:<18.2f}{device['error_count']:<15}"
        )
    print("-" * 68)
    print(f"Results exported to {output_file}")


if __name__ == "__main__":
    try:
        process_device_telemetry("device_telemetry.csv", "device_summary.json")
    except FileNotFoundError:
        print("Error: device_telemetry.csv was not found.")
    except (ValueError, KeyError) as error:
        print(f"Error: Invalid CSV data - {error}")
