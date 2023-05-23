import pandas as pd
from apyori import apriori


def return_proxy_variables(dataset: pd.DataFrame, confidence_threshold: float) -> pd.DataFrame:
    records = _return_apriori_dataset_format(dataset)
    association_rules = apriori(records, min_confidence=confidence_threshold)
    association_results = list(association_rules)
    return _return_apriori_dataframe(association_results)


def _return_apriori_dataframe(association_results: list) -> pd.DataFrame:
    antecedent = []
    consequent = []
    confidence = []

    for association_result in association_results:
        # print(association_result.ordered_statistics[0]['items_base'])
        for ordered_statistic in association_result.ordered_statistics:
            # print(ordered_statistic.items_base)
            antecedent_elements = list(ordered_statistic.items_base)
            print(antecedent_elements)
            antecedent.append(antecedent_elements)
            # print(ordered_statistic.items_base)
            consequent_elements = list(ordered_statistic.items_add)
            consequent.append(consequent_elements)
            confidence_elements = ordered_statistic.confidence
            confidence.append(confidence_elements)

    antecedent_series = pd.Series(antecedent)
    consequent_series = pd.Series(consequent)
    confidence_series = pd.Series(confidence)

    return pd.DataFrame(
        {'Antecedent': antecedent_series, 'Consequent': consequent_series, 'Confidence': confidence_series})


def _return_apriori_dataset_format(dataset: pd.DataFrame) -> list:
    records = []
    for i in range(len(dataset)):
        records.append(
            [str(dataset.columns[j] + " = " + str(dataset.values[i, j])) for j in range(len(dataset.columns) - 1)])

    return records