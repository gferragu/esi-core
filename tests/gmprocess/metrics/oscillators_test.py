import numpy as np
import pathlib

from esi_core.gmprocess.metrics.oscillators import calculate_spectrals

TESTFILE = (
    pathlib.Path(__file__).parent / ".." / ".." / "data" / "NGNH311106302345.EW1.txt"
)


def test_oscillators():
    data = np.genfromtxt(TESTFILE)
    data -= np.mean(data)
    sa_list = calculate_spectrals(
        data, len(data), 0.01, 1 / 0.01, 1.0, 0.05
    )
    target_sa = 0.027666184187569744
    np.testing.assert_allclose(np.max(sa_list[0]), target_sa)


if __name__ == "__main__":
    test_oscillators()
