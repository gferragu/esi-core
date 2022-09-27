import pathlib
import numpy as np

from esi_core.gmprocess.waveform_processing.auto_fchp import get_fchp

TESTFILE = (
    pathlib.Path(__file__).parent / ".." / ".." / "data" / "NGNH311106302345.EW1.txt"
)


def test_oscillators():
    data = np.genfromtxt(TESTFILE)
    data -= np.mean(data)
    dt = 0.01
    fc = get_fchp(dt=dt, acc=data)
    target_fc = 0.3935295398772336
    np.testing.assert_allclose(fc, target_fc)


if __name__ == "__main__":
    test_oscillators()
