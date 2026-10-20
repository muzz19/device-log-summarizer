# PROMPT_LOG.md — AI Usage Record

This log documents the AI assistance used for the assignment. Section 1 was completed without AI assistance, as required by the assessment instructions.

## Section 2 — Device telemetry processing

**Initial prompt:**
> Write a Python CLI script to read `device_telemetry.csv` with `device_id`, `status`, and `temperature` columns. Group rows by device, calculate total records, mean temperature, and ERROR count, exclude devices with average temperature above 80.0, export the remaining results to JSON, and print a readable terminal summary. Include basic error handling for missing files and invalid CSV data.

**Review / changes:** Reviewed the aggregation and filtering logic, checked required CSV columns, and verified that the summary JSON matched the sample input. The sample status values were aligned with the assessment's specified values (`ACTIVE`, `WARNING`, and `ERROR`).

## Section 3 — Charting

**Initial prompt:**
> Write a Python script that loads `device_summary.json` and uses Matplotlib to create a bar chart comparing average temperature per device. Include a descriptive title, axis labels, and save the chart as a PNG.

**Issue identified during review:** In the initial chart layout, device labels were horizontal, which could overlap and make the chart harder to read when device IDs are longer or more numerous.

**Follow-up prompt:**
> Improve the chart readability by rotating the device labels and right-aligning them. Add value labels above the bars, a light y-axis grid, use `tight_layout()`, and save the image with `bbox_inches='tight'`. Handle missing/invalid JSON and empty data gracefully.

**Review / validation:** Reviewed the final chart script and ran it against the generated JSON summary. The chart includes a title, axis labels, values above bars, rotated device labels, and spacing adjustments.

## Files and outputs

- `sensor_readings.py` contains the Section 1 cleaning function and simple test cases; Section 1 was completed without AI assistance.
- `device_log_summarizer.py` processes the CSV and writes `device_summary.json`.
- `device_temperature_chart.py` reads the JSON and writes `device_temperature_chart.png`.
- `sample_output.txt` records example console output from the scripts.

AI was used as an assistant for the data-processing and visualization work. The code and outputs were reviewed and run before packaging.
