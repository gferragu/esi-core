#!/usr/bin/env python

# third party imports
import numpy as np

# local imports
from esi_core.shakemap.covariance_matrix import (
    eval_lb_correlation,
    make_sigma_matrix,
    make_sd_array,
)


def test_covariance_matrix():
    # Mock up some coefficient arrays for Loth and Baker model
    B1 = np.array(
        [
            [0.29, 0.25],
            [0.25, 0.30],
        ]
    )
    B2 = np.array(
        [
            [0.47, 0.40],
            [0.40, 0.42],
        ]
    )
    B3 = np.array(
        [
            [0.24, 0.22],
            [0.22, 0.28],
        ]
    )
    # Evaluate the model for 4 stations, mixing imts
    ix1 = np.array([[0, 0, 1, 1]])
    ix2 = np.array([[0, 1, 0, 1]])
    h = np.array([[0.0, 1.2, 3.0, 10.0]])
    rho = np.array(eval_lb_correlation(B1, B2, B3, ix1, ix2, h))
    rho_target = np.array([[1.0, 0.58876615, 0.51114734, 0.34054345]])
    np.testing.assert_allclose(rho, rho_target)

    # Get inputs ready for the make_sd_array function

    # assume prediction is at a single location from 4 stations,
    # so corr12 has dim 1x4
    corr12 = rho.copy()
    sdsta = np.array([0.5, 0.5, 0.6, 0.7])
    sdarr = np.array([0.5])
    make_sigma_matrix(corr12, sdsta, sdarr)
    corr12_target = np.array([[0.25, 0.14719154, 0.1533442, 0.11919021]])
    np.testing.assert_allclose(corr12, corr12_target)

    pout_sd2 = np.array([[0.6]])
    sdgrid = np.zeros_like(pout_sd2)
    iy = 0
    matrix22 = np.zeros((4, 4), dtype=np.double)
    np.fill_diagonal(matrix22, sdsta * sdsta)
    cov_WD_WD_inv = np.linalg.pinv(matrix22)
    rcmatrix = np.dot(corr12, cov_WD_WD_inv)
    iy = 0
    make_sd_array(sdgrid, pout_sd2, iy, rcmatrix, corr12)
    sdgrid_target = np.array([[0.16902824]])
    np.testing.assert_allclose(sdgrid, sdgrid_target)


if __name__ == "__main__":
    test_covariance_matrix()
