
import unittest, os, pickle

import numpy as np


class Test_weight_matrix_equals_initial(unittest.TestCase):
    '''
    STDP/iSTDP and other weight changes are disabled,
    weight matrix should equal the initial weights
    '''
    
    with open('builds/0000/raw/synee_a.p', 'rb') as pfile:
        synee_a = pickle.load(pfile)

    def test_min_weight_equals_zero(self):
        self.assertEqual(np.min(self.synee_a['a']),0.)

    def test_max_weight_equals_aEE(self):
        self.assertEqual(np.max(self.synee_a['a']),0.005)

    

if __name__ == '__main__':
    unittest.main()
