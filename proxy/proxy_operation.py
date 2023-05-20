import pandas as pd
import numpy as np
from scipy.stats import boxcox
from fairness.fairness import Fairness


# In this method the effect of the sensitive variables has been canceled
def fairness_through_unawareness(dataset: pd.DataFrame, metric) -> pd.DataFrame:
    fairness = Fairness(metric)
    fairness_metric = fairness.return_fairness_metric()
    sensitive_attributes = fairness_metric.return_sensitive_attributes()
    for attribute in sensitive_attributes:
        dataset[attribute] = dataset[attribute].mean()

    return dataset


# (ideally reweighing)
# each proxy variable has been normalized and then the only value considered has been the mean
def variable_calibration(proxy_variables, dataset: pd.DataFrame) -> pd.DataFrame:
    for proxy_variable in proxy_variables:
        if -0.5 <= dataset[proxy_variable].skew() <= 0.5:
            dataset[proxy_variable] = dataset[proxy_variable].mean()
        else:
            dataset[proxy_variable] = boxcox(dataset[proxy_variable])
            dataset[proxy_variable] = dataset[proxy_variable].mean()

    return dataset
