from get_data import read_params

import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

# def read_raw_data(raw_data_path):
#     df = pd.read_csv(raw_data_path)


def train_test_split_func(config_path):

    config = read_params(config_path)

    raw_data_path = config["load_data"]["raw_dataset_csv"]
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    test_size = config["split_data"]["test_size"]
    target_col = config["base"]["target_col"]
    random_state = config["base"]["random_state"]

    df = pd.read_csv(raw_data_path)
    #print(df.head(5))
    train, test = train_test_split(
        df, 
        test_size=test_size, 
        random_state=random_state
        )

    train.to_csv(train_data_path, sep=",", index=False, encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index=False, encoding="utf-8")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_test_split_func(config_path=parsed_args.config)