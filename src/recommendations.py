import csv

print("=" * 70)
print("TIBBİ CİHAZLAR - AKILLI ENERJİ TASARRUF ÖNERİ SİSTEMİ")
print("=" * 70)

devices = []

with open("data/devices.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    print("\nCSV SÜTUNLARI:")
    print(reader.fieldnames)

    for device in reader:
        values = list(device.values())

        name = values[0]
        power = float(values[1])
        usage = float(values[2])
        standby = float(values[3])

        daily_energy = (power * usage) / 1000
        yearly_energy = daily_energy * 365

        devices.append({
            "name": name,
            "power": power,
            "usage": usage,
            "standby": standby,
            "daily_energy": daily_energy,
            "yearly_energy": yearly_energy
        })

print("\nCİHAZ BAZLI TASARRUF ANALİZİ")
print("=" * 70)

for device in devices:

    if device["yearly_energy"] >= 2000:
        level = "YÜKSEK"
        recommendation = "Enerji verimli çalışma modları ve kullanım süresi optimizasyonu uygulanmalı."

    elif device["yearly_energy"] >= 500:
        level = "ORTA"
        recommendation = "Kullanılmadığı zamanlarda güç yönetimi ve tasarruf modu kullanılmalı."

    else:
        level = "DÜŞÜK"
        recommendation = "Bekleme süresi azaltılmalı ve cihaz kullanılmadığında uygun güç yönetimi uygulanmalı."

    print(f"\nCihaz: {device['name']}")
    print(f"Günlük enerji: {device['daily_energy']:.2f} kWh")
    print(f"Yıllık enerji: {device['yearly_energy']:.2f} kWh")
    print(f"Tüketim seviyesi: {level}")
    print(f"Öneri: {recommendation}")

print("\n" + "=" * 70)
print("AKILLI TASARRUF ANALİZİ TAMAMLANDI")
print("=" * 70)