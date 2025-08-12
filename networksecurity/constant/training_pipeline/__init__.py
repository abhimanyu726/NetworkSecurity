import os
import pandas as pd
import numpy as np
import sys

"""
Defining common constant variable for training pipeline

"""

TARGET_COLUMN = "Result"
PIPELINE_NAME = "NetworkSecurity"
ARTIFACT_DIR = "Artifacts"
FILE_NAME = "phisingData.csv"

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")

DATA_INGESTION_COLLECTION_NAME = 'NetworkData'
DATA_INGESTION_DATABASE_NAME = 'ABHIMANYU'
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = 'feature_store'
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2

"""
Data validation related constant
"""
DATA_VALIDATION_DIR_NAME:str = 'data_validation'
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME :str = "report.yaml"
PREPROCESSING_OBJECT_FILE_NAME:str = "preprocessing.pkl"

DATA_TRANSFORMATION_DIR_NAME: str ="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_OBJECT_DIR:str = "transformed_object"

DATA_TRANSFORMATION_IMPUTER_PARAMS : dict = {
    "missing_values":np.nan,
    "n_neighbors":3,
    "weights":"uniform"
}