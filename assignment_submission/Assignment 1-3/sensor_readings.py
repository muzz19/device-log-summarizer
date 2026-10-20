def clean_sensor_readings(values):
    """Convert usable readings to floats, skip invalid/negative values, cap at 500."""
    cleaned = []
    for value in values:
        if value is None:
            continue
        try:
            number = float(value)
        except (ValueError, TypeError):
            continue
        if number < 0:
            continue
        if number > 500.0:
            number = 500.0
        cleaned.append(number)
    return cleaned


if __name__ == "__main__":
    print(clean_sensor_readings([100, "250.5", None, -10, "invalid", 600]))
    print(clean_sensor_readings([None, -5, "abc", -100]))
    print(clean_sensor_readings([]))
