import json
import matplotlib.pyplot as plt


def generate_temperature_chart(json_file="device_summary.json",
                               output_file="device_temperature_chart.png"):
    """Load device summary data and plot average temperature per device."""
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            devices = json.load(file)
    except FileNotFoundError:
        print(f"Error: {json_file} was not found. Run Section 2 first.")
        return
    except json.JSONDecodeError:
        print(f"Error: {json_file} does not contain valid JSON.")
        return

    if not devices:
        print("No device data available to plot.")
        return

    device_ids = [item["device_id"] for item in devices]
    avg_temperatures = [float(item["average_temperature"]) for item in devices]

    # Create a readable bar chart.
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(device_ids, avg_temperatures)

    ax.set_title("Average Temperature per Device", fontsize=14, pad=14)
    ax.set_xlabel("Device ID", fontsize=11)
    ax.set_ylabel("Average Temperature (°C)", fontsize=11)
    ax.bar_label(bars, fmt="%.2f", padding=3)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    # Rotate labels and adjust spacing to prevent overlap.
    plt.xticks(rotation=30, ha="right")
    fig.tight_layout()

    fig.savefig(output_file, dpi=150, bbox_inches="tight")
    print(f"Chart saved to {output_file}")
    plt.show()


if __name__ == "__main__":
    generate_temperature_chart()
