import pandas as pd
import numpy as np
import typing
from fairness.metric import FairnessMetric


MetricConstructor = typing.Callable[[], FairnessMetric]


class Fairness:
    def __init__(self, metric: MetricConstructor) -> None:
        self.metric = metric()

    def check_for_bias(self, dataset: pd.DataFrame):
        """This method allow to check bias into the dataset according to a specific metric"""
        fairness_metric = self.metric
        fairness_metric_obj = fairness_metric()
        return fairness_metric_obj.check(dataset)

    # This method executes a fairness evaluation starting from the result of the check
    def establish_fairness(self, bias_analysis_dataframe: pd.DataFrame):
        fairness_metric = self.metric
        fairness_metric_obj = fairness_metric()
        return fairness_metric_obj.fairness_evaulation(bias_analysis_dataframe)
