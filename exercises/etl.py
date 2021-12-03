def transform(legacy_data):
    new_data = {}
    for key, item in legacy_data.items():
        for sub_item in item:
            new_data[sub_item.lower()] = key

    return new_data


legacy_data = {1: ["A", "E", "I", "O", "U"]}
print(transform(legacy_data))
