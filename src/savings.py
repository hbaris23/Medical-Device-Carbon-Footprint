import csv

EMISSION_FACTOR = 0.40
DAYS_PER_YEAR = 365

SAVING_RATES = [0.10, 0.20, 0.30]

print("=" * 70)
print("TIBBİ CİHAZLAR - ENERJİ VE KARBON TASARRUF SENARYOSU")
print("=" * 70)

with open("data/devices.csv", "r", encoding="utf-8-sig") as file:

    reader = csv.DictReader(file)

    print("\nTASARRUF SENARYOLARI")
    print("=" * 70)

    for device in reader:

        name = device["device_name"]
        power = float(device["power_watt"])
        daily_hours = float(device["daily_hours"])

        daily_energy = (power * daily_hours) / 1000
        yearly_energy = daily_energy * DAYS_PER_YEAR

        yearly_carbon = yearly_energy * EMISSION_FACTOR

        print(f"\nCihaz: {name}")
        print(f"Mevcut yıllık enerji : {yearly_energy:.2f} kWh")
        print(f"Mevcut yıllık CO2e   : {yearly_carbon:.2f} kg")

        for rate in SAVING_RATES:

            energy_saving = yearly_energy * rate
            carbon_saving = energy_saving * EMISSION_FACTOR

            remaining_energy = yearly_energy - energy_saving
            remaining_carbon = yearly_carbon - carbon_saving

            percentage = int(rate * 100)

            print(f"\n  %{percentage} TASARRUF SENARYOSU")
            print(f"  Enerji tasarrufu : {energy_saving:.2f} kWh/yıl")
            print(f"  CO2e azaltımı    : {carbon_saving:.2f} kg/yıl")
            print(f"  Kalan enerji     : {remaining_energy:.2f} kWh/yıl")
            print(f"  Kalan CO2e       : {remaining_carbon:.2f} kg/yıl")

print("\n" + "=" * 70)
print("TASARRUF SENARYOSU TAMAMLANDI")
print("=" * 70)