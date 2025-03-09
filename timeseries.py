import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker for generating synthetic data
fake = Faker()

# Function to generate mock SETI signal data
def generate_seti_data(num_records=1000):
    """Generate mock time series data for SETI@Home-style radio signal analysis."""
    
    # Time Series: Start time for data simulation
    start_time = datetime.utcnow() - timedelta(days=30)  # 30 days of historical data
    
    # Possible signal classifications
    signal_types = ["Noise", "Pulsar", "Unknown Signal", "ET Candidate"]

    data = []
    
    for _ in range(num_records):
        timestamp = start_time + timedelta(seconds=random.randint(1, 86400))  # Random time in a 24-hour period
        frequency = random.uniform(1.0, 10.0) * 10**9  # GHz (simulated radio frequency)
        snr = random.uniform(-10, 50)  # Signal-to-noise ratio in dB
        ra = random.uniform(0, 360)  # Right Ascension (degrees)
        dec = random.uniform(-90, 90)  # Declination (degrees)
        classification = random.choices(signal_types, weights=[80, 15, 4, 1])[0]  # More noise, rare "ET Candidate"

        data.append({
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "frequency_hz": round(frequency, 2),
            "snr_db": round(snr, 2),
            "ra_deg": round(ra, 4),
            "dec_deg": round(dec, 4),
            "classification": classification
        })

    return pd.DataFrame(data)

# Generate mock data
seti_mock_data = generate_seti_data(num_records=5000)

# Display the first few rows
import ace_tools as tools
tools.display_dataframe_to_user(name="Mock SETI Data", dataframe=seti_mock_data)
