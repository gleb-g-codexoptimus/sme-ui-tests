def parse_log_values(data, key, value=None):
    if not data: raise ValueError("Data is empty")
    if value:
        values_list = [entry.get(key, "Key not found") for entry in data if value in entry.get(key, "")]
    else:
        values_list = [entry.get(key, "Key not found") for entry in data]
    return values_list

