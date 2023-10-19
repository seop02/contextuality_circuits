from QCNN import *
from layers import *
import numpy as np
from scipy.stats import rv_continuous
import os
import logging

logging.basicConfig(level=logging.WARNING)
logging.getLogger().setLevel(logging.INFO)
LOG = logging.getLogger(__name__)

class sin_prob_dist(rv_continuous):
    def _pdf(self, theta):
        # The 0.5 is so that the distribution is normalized
        return 0.5 * np.sin(theta)




if __name__=="__main__":
    
    sin_sampler = sin_prob_dist(a=0, b=np.pi)
    
    if not os.path.exists('data'):
        os.mkdir('data')
    
    trial = 0
    
    circuit_num = 400
    
    #indexes of theta in SU4 convolutional layers
    theta_idx = [0, 3, 9, 12, 15, 18, 24, 27, 30, 33, 39, 42]
    
    state1 = np.zeros((circuit_num, 256), dtype='complex_')
    state2 = np.zeros((circuit_num, 256), dtype='complex_')
    state3 = np.zeros((circuit_num, 256), dtype='complex_')
    
    density1 = np.zeros((circuit_num, 256, 256), dtype='complex_')
    density2 = np.zeros((circuit_num, 256, 256), dtype='complex_')
    density3 = np.zeros((circuit_num, 256, 256), dtype='complex_')
    
    while trial < circuit_num:
        LOG.info(f'currently on {trial}th circuit')
        params = np.random.rand(45)*2*np.pi
        
        for idx in theta_idx:
            params[idx] = sin_sampler.rvs(size=1)
        
        params1 = params[0:15]
        params2 = params[15:30]
        params3 = params[30:45]
        
        
        state1[trial] = QCNN_1(SU4, params1)
        state2[trial] = QCNN_2(SU4, params1, params2)
        state3[trial] = QCNN_3(SU4, params1, params2, params3)
        
        density1[trial] = np.outer(state1[trial], np.conj(state1[trial]))
        density2[trial] = np.outer(state2[trial], np.conj(state2[trial]))
        density3[trial] = np.outer(state3[trial], np.conj(state3[trial]))
        
        trial += 1
    
    np.save('data/state1.npy', state1)
    np.save('data/state2.npy', state2)
    np.save('data/state3.npy', state3)
    
    np.save('data/density1.npy', density1)
    np.save('data/density2.npy', density2)
    np.save('data/density3.npy', density3)
    
    