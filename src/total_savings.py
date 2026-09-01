import csv

EMISSION_FACTOR = 0.40
DAYS_PER_YEAR = 365

total_energy = 0

with open("data/devices.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for device in reader:
        power = float(device["power_watt"])
        daily_hours = float(device["daily_hours"])

        daily_energy = (power * daily_hours) / 1000
        yearly_energy = daily_energy * DAYS_PER_YEAR

        total_energy += yearly_energy


print("=" * 70)
print("TIBBİ CİHAZLAR - TOPLAM TASARRUF POTANSİYELİ")
print("=" * 70)

print(f"\nMevcut yıllık enerji : {total_energy:.2f} kWh")
print(f"Mevcut yıllık CO2e   : {total_energy * EMISSION_FACTOR:.2f} kg")

for rate in [0.10, 0.20, 0.30]:

    energy_saving = total_energy * rate
    carbon_saving = energy_saving * EMISSION_FACTOR

    remaining_energy = total_energy - energy_saving
    remaining_carbon = (total_energy * EMISSION_FACTOR) - carbon_saving

    percentage = int(rate * 100)

    print(f"\n%{percentage} TASARRUF SENARYOSU")
    print("-" * 50)
    print(f"Enerji tasarrufu : {energy_saving:.2f} kWh/yıl")
    print(f"CO2e azaltımı    : {carbon_saving:.2f} kg/yıl")
    print(f"Kalan enerji     : {remaining_energy:.2f} kWh/yıl")
    print(f"Kalan CO2e       : {remaining_carbon:.2f} kg/yıl")

print("\n" + "=" * 70)
print("TOPLAM TASARRUF ANALİZİ TAMAMLANDI")
print("=" * 70)