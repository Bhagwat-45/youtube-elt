import json
from datetime import date

def save_to_json(extracted_data: list):
    file_path = f"./data/data_{date.today()}.json"
    try:
        with open(file_path, 'w') as file:
            file.write(json.dumps(extracted_data, indent=4))
    except OSError as e:
        raise e
    