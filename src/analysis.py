import csv
import matplotlib.pyplot as plt

EMISSION_FACTOR = 0.40
DAYS_PER_YEAR = 365

device_names = []
yearly_energy = []
yearly_carbon = []

with open("data/devices.csv", "r", encoding="utf-8-sig") as file:

    reader = csv.DictReader(file)

    for device in reader:

        name = device["device_name"]
        power = float(device["power_watt"])
        daily_hours = float(device["daily_hours"])

        daily_energy = (power * daily_hours) / 1000
        annual_energy = daily_energy * DAYS_PER_YEAR
        annual_carbon = annual_energy * EMISSION_FACTOR

        device_names.append(name)
        yearly_energy.append(annual_energy)
        yearly_carbon.append(annual_carbon)


# Enerji tüketimi grafiği
plt.figure(figsize=(10, 6))

plt.bar(device_names, yearly_energy)

plt.title("Tıbbi Cihazların Yıllık Enerji Tüketimi")
plt.xlabel("Tıbbi Cihaz")
plt.ylabel("Enerji (kWh/yıl)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/energy_analysis.png", dpi=300)

plt.show()


# Karbon ayak izi grafiği
plt.figure(figsize=(10, 6))

plt.bar(device_names, yearly_carbon)

plt.title("Tıbbi Cihazların Yıllık Karbon Ayak İzi")
plt.xlabel("Tıbbi Cihaz")
plt.ylabel("CO2e (kg/yıl)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/carbon_analysis.png", dpi=300)

plt.show()

print("=" * 60)
print("GRAFİK ANALİZİ TAMAMLANDI")
print("=" * 60)

print()
print("Oluşturulan dosyalar:")
print("outputs/energy_analysis.png")
print("outputs/carbon_analysis.png")