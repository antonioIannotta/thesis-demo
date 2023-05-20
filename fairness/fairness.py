import pandas as pd
import numpy as np
from fairness_metric.unbalanced_dataset import UnbalancedDataset
from fairness_metric.prevalence import Prevalence
from fairness_metric.equal_opportunity import EqualOpportunity
from fairness_metric.equalized_odds import EqualizedOdds
from fairness_metric.disparate_impact import DisparateImpact

list_metric = ["unbalanced_dataset", "prevalence", "equal_opportunity", "equalized_odds", "disparate_impact"]


class Fairness():
    def __init__(self, metric) -> None:
        self.metric = metric

    # This method allow to check bias into the dataset according to a specific metric
    def check_for_bias(self, dataset: pd.DataFrame):
        fairness_metric = self.return_fairness_metric(self.metric)
        fairness_metric_obj = fairness_metric()
        return fairness_metric_obj.check(dataset)

    # This method executes a fairness evaluation starting from the result of the check
    def establish_fairness(self, bias_analysis_dataframe: pd.DataFrame):
        fairness_metric = self.return_fairness_metric(self.metric)
        fairness_metric_obj = fairness_metric()
        return fairness_metric_obj.fairness_evaulation(bias_analysis_dataframe)
    
    # This method returns the class of the selected metric
    def return_fairness_metric(self):
        match self.metric:
            case "unbalanced_dataset":
                return UnbalancedDataset
            case "prevalence":
                return Prevalence
            case "equal_opportunity":
                return EqualOpportunity
            case "equalized_odds":
                return EqualizedOdds
            case "disparate_impact":
                return DisparateImpact



