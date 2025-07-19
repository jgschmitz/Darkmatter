import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from faker import Faker
import secrets

# Initialize Faker and constants
fake = Faker()
SIGNAL_TYPES = ["Noise", "Pulsar", "Unknown Signal", "ET Candidate"]
SIGNAL_WEIGHTS = [0.80, 0.15, 0.04, 0.01]  # Probabilities must sum to 1

def generate_seti_data(num_records=1000):
    """
    Generate mock SETI-style radio signal time series data.
    
    Returns:
        pd.DataFrame: DataFrame with synthetic observations.
    """
    now = datetime.utcnow()
    base_time = now - timedelta(days=30)

    # Pre-allocate arrays for performance
    timestamps = [(base_time + timedelta(seconds=int(np.random.uniform(0, 86400)))).isoformat() for _ in range(num_records)]
    frequencies = np.round(np.random.uniform(1.0, 10.0, num_records) * 1e9, 2)
    snrs = np.round(np.random.uniform(-10, 50, num_records), 2)
    ras = np.round(np.random.uniform(0, 360, num_records), 4)
    decs = np.round(np.random.uniform(-90, 90, num_records), 4)
    classifications = np.random.choice(SIGNAL_TYPES, size=num_records, p=SIGNAL_WEIGHTS)

    return pd.DataFrame({
        "timestamp": timestamps,
        "frequency_hz": frequencies,
        "snr_db": snrs,
        "ra_deg": ras,
        "dec_deg": decs,
        "classification": classifications
    })

# Generate and display the data
seti_mock_data = generate_seti_data(5000)

import ace_tools as tools
tools.display_dataframe_to_user(name="Mock SETI Data", dataframe=seti_mock_data)
