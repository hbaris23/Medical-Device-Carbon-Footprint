import csv

print("=" * 70)
print("TIBBİ CİHAZLARIN ENERJİ VE KARBON AYAK İZİ ANALİZİ")
print("=" * 70)

EMISSION_FACTOR = 0.40
DAYS_PER_YEAR = 365

devices = []

with open("data/devices.csv", "r", encoding="utf-8-sig") as file:

    reader = csv.DictReader(file)

    for device in reader:

        device_name = device["device_name"]
        power = float(device["power_watt"])
        daily_hours = float(device["daily_hours"])

        daily_energy = (power * daily_hours) / 1000
        yearly_energy = daily_energy * DAYS_PER_YEAR

        daily_carbon = daily_energy * EMISSION_FACTOR
        yearly_carbon = yearly_energy * EMISSION_FACTOR

        devices.append({
            "name": device_name,
            "daily_energy": daily_energy,
            "yearly_energy": yearly_energy,
            "daily_carbon": daily_carbon,
            "yearly_carbon": yearly_carbon
        })


# Enerji tüketimine göre sıralama
energy_ranking = sorted(
    devices,
    key=lambda x: x["yearly_energy"],
    reverse=True
)

# Karbon emisyonuna göre sıralama
carbon_ranking = sorted(
    devices,
    key=lambda x: x["yearly_carbon"],
    reverse=True
)


print()
print("=" * 70)
print("ENERJİ TÜKETİMİ SIRALAMASI")
print("=" * 70)

for i, device in enumerate(energy_ranking, start=1):

    print(
        f"{i}. {device['name']} -> "
        f"{device['yearly_energy']:.2f} kWh/yıl"
    )


print()
print("=" * 70)
print("KARBON AYAK İZİ SIRALAMASI")
print("=" * 70)

for i, device in enumerate(carbon_ranking, start=1):

    print(
        f"{i}. {device['name']} -> "
        f"{device['yearly_carbon']:.2f} kg CO2e/yıl"
    )


print()
print("=" * 70)
print("EN YÜKSEK TÜKETİCİ")
print("=" * 70)

highest_energy = energy_ranking[0]

print(
    f"Cihaz: {highest_energy['name']}"
)

print(
    f"Yıllık enerji: "
    f"{highest_energy['yearly_energy']:.2f} kWh"
)

print(
    f"Yıllık karbon: "
    f"{highest_energy['yearly_carbon']:.2f} kg CO2e"
)

print()
print("=" * 70)
print("ANALİZ TAMAMLANDI")
print("=" * 70)