import os
import json
def read_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    file_path = os.path.join(project_root, "data","data.json")
    with open(file_path,"r") as f:
        data = json.load(f)
        return data
