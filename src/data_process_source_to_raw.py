from get_data import get_data,read_params

import argparse

def save_to_raw(config_path):
    config = read_params(config_path)

    source_path = config["data_source"]["source"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]

    df = get_data(config_path)

    new_cols = [col.replace(" ", "_") for col in df.columns]
    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)

    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    save_to_raw(config_path=parsed_args.config)