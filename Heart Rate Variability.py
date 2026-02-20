import neurokit2 as nk
import pandas as pd

# Simulate ECG signal
sig = nk.ecg_simulate(duration=30, sampling_rate=250)

# Detect R-peaks
signals, info = nk.ecg_peaks(sig, sampling_rate=250)

# Compute HRV (time-domain features)
hrv = nk.hrv_time(info, sampling_rate=250)

print(hrv.head())
