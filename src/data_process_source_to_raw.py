from get_data import get_data,read_params

import argparse
import pandas as pd

def save_to_raw(config_path):
    config = read_params(config_path)

    source_path = config["data_source"]["source"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]

    df = get_data(config_path)

    column_names = [cols.replace(" ", "_") for cols in df.columns]
    print(column_names)

    df.to_csv(raw_data_path,header=column_names)

    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    save_to_raw(config_path=parsed_args.config)