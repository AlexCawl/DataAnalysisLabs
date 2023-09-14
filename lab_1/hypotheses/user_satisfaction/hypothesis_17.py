import datetime
from typing import Tuple, Dict, List

import pandas as pd

from lab_1.util.Hypothesis import Hypothesis
from lab_1.util.decorators import measure_execution_time
from lab_1.util.constants import *

# №17
# Вопрос: Какова удовлетворенность клиентов от взаимодействия с сайтом?
# Гипотеза: Среднее время браузинга товаров на сайте больше, чем $VAL минут

@measure_execution_time
def compute(dataframe: pd.DataFrame, comparable_value: float) -> Tuple[str, str]:
    hypothesis: Hypothesis = Hypothesis(
        h0="Среднее время браузинга товаров на сайте больше, чем {val}",
        h1="Среднее время браузинга товаров на сайте не больше, чем {val}",
        condition=lambda x: x > comparable_value
    )

    users: Dict[str, List[str]] = dict()
    users_count: int = 0

    for index in range(len(dataframe)):
        row: pd.Series = dataframe.loc[index]
        user_id: str = str(row[ID])
        _datetime: str = str(row[DATETIME])[:19]
        if users.get(user_id) is None:
            users.update({user_id: [_datetime]})
            users_count += 1
        else:
            list_to_update: List[str] = users[user_id]
            if len(users[user_id]) == 1:
                list_to_update.append(_datetime)
                users.update({user_id: list_to_update})
            else:
                list_to_update[1] = _datetime
                users.update({user_id: list_to_update})
    total_diff: float = 0
    for key in users.keys():
        if len(users[key]) > 1:
            first_request: datetime.datetime = datetime.datetime.strptime(users[key][0], "%d/%b/%Y:%H:%M:%S")
            last_request: datetime.datetime = datetime.datetime.strptime(users[key][1], "%d/%b/%Y:%H:%M:%S")

            diff: float = (last_request-first_request).total_seconds()/60
            total_diff += diff

    value: float = total_diff/users_count
    return hypothesis.compute(value), f"{value}"