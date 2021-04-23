# Import packages
import model_search
from model_search import constants
from model_search import single_trainer
from model_search.data import csv_data
from pathlib import Path

myPath = r'C:\Users\shahi\Documents\git\cognitive-frailty-classification\features.csv'

myPath = Path(myPath)

myPath = str(myPath)

trainer = single_trainer.SingleTrainer(
    data=csv_data.Provider(
        label_index=0,
        logits_dimension=6,
        record_defaults=[0, 0, 0, 0],
        filename="model_search/data/testdata/csv_random_data.csv"),
        spec=constants.DEFAULT_DNN)

trainer.try_models(
    number_models=5,
    train_steps=1000,
    eval_steps=100,
    root_dir="/tmp/run_example",
    batch_size=32,
    experiment_name="example",
    experiment_owner="model_search_user")