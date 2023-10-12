import pandas as pd

from labs.lab_2.checker import check_hypotheses
from labs.util.benchmarking.measuring import measure_execution_time
from labs.util.file_processing.configuration import DATA_OUTPUT_FOLDER, FISHING_CSV_FILE
from labs.util.file_processing.extensions import mk_dir_abs_from_local
from labs.util.file_processing.loader import load_from_csv


@measure_execution_time
def main():
    """
    Run this only from lab2_classifications.py from content root dir.
    """
    DATAFRAME_PATH: str = f"{mk_dir_abs_from_local(DATA_OUTPUT_FOLDER)}/{FISHING_CSV_FILE}"
    dataframe: pd.DataFrame = load_from_csv(DATAFRAME_PATH)
    check_hypotheses(dataframe)
