import pathlib
import numpy as np

from esi_core.gmprocess.waveform_processing.smoothing.konno_ohmachi import (
    konno_ohmachi_smooth,
)

TESTFILE = (
    pathlib.Path(__file__).parent
    / ".."
    / ".."
    / ".."
    / "data"
    / "NGNH311106302345.EW1.txt"
)


def test_oscillators():
    data = np.genfromtxt(TESTFILE)
    data -= np.mean(data)
    npts = len(data)
    dt = 0.01
    spec = abs(np.fft.rfft(data, n=npts)) * dt
    freqs = np.fft.rfftfreq(npts, dt)

    nkofreqs = 30
    ko_freqs = np.logspace(np.log10(freqs[1]), np.log10(freqs[-1]), nkofreqs)
    # An array to hold the output
    spec_smooth = np.empty_like(ko_freqs)

    # Konno Omachi Smoothing
    konno_ohmachi_smooth(spec.astype(np.double), freqs, ko_freqs, spec_smooth, 20)
    # fmt: off
    target_spec = np.array([
        0.00524574, 0.00524574, 0.00872497, 0.00588279, 0.00369508,
        0.00412656, 0.00121808, 0.00461715, 0.0046903 , 0.00303195,
        0.00208538, 0.00146396, 0.00172822, 0.00230647, 0.00394352,
        0.00634458, 0.00822907, 0.00785533, 0.01298493, 0.02088832,
        0.01573672, 0.01954229, 0.01365153, 0.01216181, 0.01026609,
        0.01661667, 0.01107656, 0.00494471, 0.00091639, 0.00013611
    ])
    # fmt: on
    np.testing.assert_allclose(target_spec, spec_smooth, rtol=1e-4)


if __name__ == "__main__":
    test_oscillators()
