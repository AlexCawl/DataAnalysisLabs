from typing import Any
from typing import List

import pandas as pd

from .LogDTO import LogDTO
from .constants import *


def map_logs_to_dataframe(logs: List[LogDTO], size: int = 100) -> pd.DataFrame:
    dataframe: pd.DataFrame = pd.DataFrame(columns=[ID, IP_ADDRESS, DATETIME, HTTP_TYPE, HTTP_CODE, URL])
    for index, log in enumerate(logs):
        dataframe.loc[index] = map_log_dto_to_values(log)
        if index == size:
            break
    return dataframe


def map_log_dto_to_values(log: LogDTO) -> List[Any]:
    return [
        log.user_id,
        log.ip,
        log.date_time,
        log.http_type,
        log.code,
        log.url
    ]