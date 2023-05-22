class FairnessMetric:
    pass

class EqualOpportunity(FairnessMetric):
    pass

class EqualizedOdds(FairnessMetric):
    pass

class Prevalence(FairnessMetric):
    pass

class UnbalancedDataset(FairnessMetric):
    pass


def _snake_to_pascal_case(string: str) -> str:
    words = string.split('_')
    return ''.join(word.capitalize() for word in words)


def find_metric_by_name(name: str) -> type:
    if "_" in name:
        name = _snake_to_pascal_case(name)
    try:
        return globals()[name]
    except KeyError:
        raise KeyError("No such metric: " + name)
