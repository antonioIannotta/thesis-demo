import pandas as pd
from fairness.fairness import Fairness

def fairness_through_unawareness(dataset: pd.DataFrame, metric) -> pd.DataFrame:
    fairness = Fairness(metric)
    fairness_metric = fairness.return_fairness_metric()
    sensitive_attributes = fairness_metric.return_sensitive_attributes()
    for attribute in sensitive_attributes:
        dataset.drop(attribute, axis=1, inplace=True)
        
    return dataset


