from src.data_loader import get_driver_laps, normalize_sequences, save_sequences

# === Select which race/drivers to pull ===
targets = [
    (2021, 'Silverstone', 'HAM'),
    (2021, 'Silverstone', 'VER'),
    (2022, 'Hungary', 'ALO'),
    (2022, 'Hungary', 'LEC'),
    (2023, 'Brazil', 'NOR'),
]

all_laps = []
for year, gp, driver in targets:
    print(f"Loading {driver} - {gp} {year}")
    laps = get_driver_laps(year, gp, driver)
    all_laps.extend(laps)

# === Normalize across all collected laps ===
normalized = normalize_sequences(all_laps)

# === Save to disk ===
save_sequences(normalized, out_dir="data/processed")
