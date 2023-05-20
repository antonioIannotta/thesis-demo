import unittest
from fairness.fairness import Fairness
from fairness_metric.equal_opportunity import EqualOpportunity
from fairness_metric.equalized_odds import EqualizedOdds
from fairness_metric.disparate_impact import DisparateImpact
from fairness_metric.prevalence import Prevalence
from fairness_metric.unbalanced_dataset import UnbalancedDataset


class FairnessTest(unittest.TestCase):

    def test_return_fairness_metric(self):
        fairness = Fairness('equal_opportunity')
        self.assertEqual(EqualOpportunity, fairness.return_fairness_metric())
        fairness = Fairness('equalized_odds')
        self.assertEqual(EqualizedOdds, fairness.return_fairness_metric())
        fairness = Fairness('disparate_impact')
        self.assertEqual(DisparateImpact, fairness.return_fairness_metric())
        fairness = Fairness('prevalence')
        self.assertEqual(Prevalence, fairness.return_fairness_metric())
        fairness = Fairness('unbalanced_dataset')
        self.assertEqual(UnbalancedDataset, fairness.return_fairness_metric())


if __name__ == '__main__':
    unittest.main()
