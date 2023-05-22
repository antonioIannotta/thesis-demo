import unittest
from fairness import Fairness
from fairness.metric import EqualOpportunity
from fairness.metric import EqualizedOdds
from fairness.metric import DisparateImpact
from fairness.metric import Prevalence
from fairness.metric import UnbalancedDataset


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
