import os
import numpy as np
import pandas as pd
import fastf1
from fastf1.core import Laps
from sklearn.preprocessing import MinMaxScaler

fastf1.Cache.enable_cache('./.fastf1_cache')  # Store data locally to avoid re-downloading

SEQUENCE_LENGTH = 100  # Number of time steps per lap

# Features to extract from telemetry
FEATURE_COLUMNS = ['Speed', 'Throttle', 'Brake', 'RPM', 'nGear', 'DRS']

def get_driver_laps(year, gp_name, driver_code):
    """
    Download and return telemetry data for all quick laps of a driver in a given race session.
    """
    session = fastf1.get_session(year, gp_name, 'R')
    session.load()

    laps = session.laps.pick_drivers(driver_code).pick_quicklaps()
    lap_sequences = []

    for _, lap in laps.iterrows():
        tel = lap.get_telemetry()
        tel = tel[FEATURE_COLUMNS].interpolate().dropna()

        # Uniform length: pad or truncate
        tel = pad_or_truncate(tel, SEQUENCE_LENGTH)

        lap_array = tel.to_numpy()
        lap_sequences.append({
            "lap_array": lap_array,
            "lap_time": lap['LapTime'].total_seconds() if pd.notnull(lap['LapTime']) else -1,
            "driver": driver_code,
            "lap_number": lap['LapNumber']
        })

    return lap_sequences


def pad_or_truncate(df, length):
    """
    Pads or truncates the DataFrame to a fixed number of rows.
    """
    if len(df) >= length:
        return df.iloc[:length]
    else:
        pad_df = pd.DataFrame(np.zeros((length - len(df), len(df.columns))), columns=df.columns)
        return pd.concat([df, pad_df], ignore_index=True)


def normalize_sequences(sequences):
    """
    Normalizes all lap sequences across the dataset using MinMaxScaler (0–1).
    """
    all_data = np.array([lap["lap_array"] for lap in sequences])
    shape = all_data.shape  # (num_laps, seq_len, num_features)
    all_data_flat = all_data.reshape(-1, shape[2])  # Collapse time and laps

    scaler = MinMaxScaler()
    all_scaled = scaler.fit_transform(all_data_flat)

    normalized = all_scaled.reshape(shape)
    for i, lap in enumerate(sequences):
        lap["lap_array"] = normalized[i]
    return sequences


def save_sequences(sequences, out_dir):
    """
    Saves lap sequences to compressed .npz format.
    """
    os.makedirs(out_dir, exist_ok=True)

    for lap in sequences:
        filename = f"{lap['driver']}_lap{int(lap['lap_number']):02d}.npz"
        path = os.path.join(out_dir, filename)
        np.savez_compressed(path, data=lap["lap_array"], time=lap["lap_time"])

