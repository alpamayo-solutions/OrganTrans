import yaml
import pathlib


def convert_v3_to_v5(yamlv3_path, yamlv5_path=None):
    yamlv3_path = None

    while yamlv3_path is None:
        yamlv3_path = input("Enter the path to the v3 dataset yaml file (e.g. 'dataset.yaml'): ").strip().replace("'", "").replace('"', '')
        yamlv3_path = pathlib.Path(yamlv3_path)
        
        if not pathlib.Path(yamlv3_path).exists():
            print("File does not exist. Please try again.")
            yamlv3_path = None

    with open(yamlv3_path, 'r') as stream:
        yamlv3_data = dict(yaml.safe_load(stream))


    yamlv5_data = yamlv3_data.copy()
    yamlv5_data["path"] = str(pathlib.Path(yamlv5_data["train"]).parent)

    yamlv5_data["names"] = {idx: name for idx, name in enumerate(yamlv5_data["names"])}

    yamlv5_path = yamlv3_path.parent / (yamlv3_path.stem + "_v5.yaml")
    with open(yamlv5_path, 'w') as stream:
        yaml.dump(yamlv5_data, stream)
        
    print(f"Successfully upgraded {yamlv3_path} to {yamlv5_path}")
    
if __name__ == "__main__":
    convert_v3_to_v5(None)
    

    
