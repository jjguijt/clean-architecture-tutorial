from abc import ABC
from dataclasses import dataclass
from datetime import datetime, date, timedelta
from typing import List
from zoneinfo import ZoneInfo


@dataclass
class Order:
    items: List


class Scheduler(ABC):
    def schedule_order(self, order: Order):
        raise NotImplementedError()


def schedule_production_of_order(order: Order, scheduler: Scheduler):
    """
    Schedule an order and return the expected production date of the order
    :param order:
    :param scheduler:
    :return:
    """
    current_time = datetime.now(tz=ZoneInfo("Europe/Amsterdam"))

    scheduler.schedule_order(order)

    # If we're past 6PM, we expect the order to be produced the next day.
    if current_time.hour >= 18:
        expected_date = current_time.day + timedelta(days=1)
    else:
        expected_date = current_time.day

    return expected_date
