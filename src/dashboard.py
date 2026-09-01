import csv
import streamlit as st
import pandas as pd

EMISSION_FACTOR = 0.40
DAYS_PER_YEAR = 365

# ---------------------------------------------------------
# SAYFA AYARLARI
# ---------------------------------------------------------

st.set_page_config(
    page_title="Medical Device Carbon Footprint",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Tıbbi Cihaz Enerji ve Karbon Ayak İzi")

st.markdown(
    "Tıbbi cihazların enerji tüketimini, karbon ayak izini, "
    "maliyetini ve tasarruf potansiyelini analiz eden akıllı sistem."
)

# ---------------------------------------------------------
# ELEKTRİK BİRİM FİYATI
# ---------------------------------------------------------

st.sidebar.header("⚙️ Sistem Ayarları")

electricity_price = st.sidebar.number_input(
    "Elektrik birim fiyatı (TL/kWh)",
    min_value=0.0,
    value=3.50,
    step=0.10
)

st.sidebar.info(
    "Elektrik birim fiyatını kullandığınız güncel tarifeye "
    "göre değiştirebilirsiniz."
)

# ---------------------------------------------------------
# VERİLERİ OKU
# ---------------------------------------------------------

devices = []

with open("data/devices.csv", "r", encoding="utf-8-sig") as file:

    reader = csv.DictReader(file)

    for device in reader:

        name = device["device_name"]
        power = float(device["power_watt"])
        daily_hours = float(device["daily_hours"])
        standby_hours = float(device["standby_hours"])

        daily_energy = (power * daily_hours) / 1000
        monthly_energy = daily_energy * 30
        yearly_energy = daily_energy * DAYS_PER_YEAR

        daily_carbon = daily_energy * EMISSION_FACTOR
        yearly_carbon = yearly_energy * EMISSION_FACTOR

        daily_cost = daily_energy * electricity_price
        monthly_cost = monthly_energy * electricity_price
        yearly_cost = yearly_energy * electricity_price

        devices.append({
            "Cihaz": name,
            "Güç (W)": power,
            "Günlük Kullanım (saat)": daily_hours,
            "Bekleme (saat)": standby_hours,
            "Günlük Enerji (kWh)": daily_energy,
            "Yıllık Enerji (kWh)": yearly_energy,
            "Günlük CO2e (kg)": daily_carbon,
            "Yıllık CO2e (kg)": yearly_carbon,
            "Günlük Maliyet (TL)": daily_cost,
            "Aylık Maliyet (TL)": monthly_cost,
            "Yıllık Maliyet (TL)": yearly_cost
        })

df = pd.DataFrame(devices)

# ---------------------------------------------------------
# TOPLAM HESAPLAR
# ---------------------------------------------------------

total_daily_energy = df["Günlük Enerji (kWh)"].sum()
total_monthly_energy = total_daily_energy * 30
total_energy = df["Yıllık Enerji (kWh)"].sum()

total_daily_carbon = df["Günlük CO2e (kg)"].sum()
total_carbon = df["Yıllık CO2e (kg)"].sum()

total_daily_cost = total_daily_energy * electricity_price
total_monthly_cost = total_monthly_energy * electricity_price
total_yearly_cost = total_energy * electricity_price

highest_device = df.loc[
    df["Yıllık Enerji (kWh)"].idxmax()
]

# ---------------------------------------------------------
# GENEL ÖZET
# ---------------------------------------------------------

st.header("📊 Genel Sistem Özeti")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "⚡ Yıllık Enerji",
        f"{total_energy:,.2f} kWh"
    )

with col2:
    st.metric(
        "🌱 Yıllık CO₂e",
        f"{total_carbon:,.2f} kg"
    )

with col3:
    st.metric(
        "💰 Yıllık Maliyet",
        f"{total_yearly_cost:,.2f} TL"
    )

with col4:
    st.metric(
        "🔴 En Yüksek Tüketici",
        highest_device["Cihaz"]
    )

st.divider()

# ---------------------------------------------------------
# MALİYET ÖZETİ
# ---------------------------------------------------------

st.subheader("💰 Enerji Maliyet Analizi")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Günlük Maliyet",
        f"{total_daily_cost:,.2f} TL"
    )

with col2:
    st.metric(
        "Aylık Maliyet",
        f"{total_monthly_cost:,.2f} TL"
    )

with col3:
    st.metric(
        "Yıllık Maliyet",
        f"{total_yearly_cost:,.2f} TL"
    )

st.caption(
    f"Kullanılan elektrik birim fiyatı: "
    f"{electricity_price:.2f} TL/kWh"
)

st.divider()

# ---------------------------------------------------------
# GRAFİKLER
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("⚡ Yıllık Enerji Tüketimi")

    energy_chart = df.set_index("Cihaz")[
        "Yıllık Enerji (kWh)"
    ]

    st.bar_chart(energy_chart)

with col2:

    st.subheader("🌱 Yıllık Karbon Ayak İzi")

    carbon_chart = df.set_index("Cihaz")[
        "Yıllık CO2e (kg)"
    ]

    st.bar_chart(carbon_chart)

st.divider()

# ---------------------------------------------------------
# MALİYET GRAFİĞİ
# ---------------------------------------------------------

st.subheader("💰 Cihaz Bazlı Yıllık Enerji Maliyeti")

cost_chart = df.set_index("Cihaz")[
    "Yıllık Maliyet (TL)"
]

st.bar_chart(cost_chart)

st.divider()

# ---------------------------------------------------------
# CİHAZ TABLOSU
# ---------------------------------------------------------

st.subheader("📋 Tıbbi Cihaz Analizi")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# ---------------------------------------------------------
# AKILLI CİHAZ SEÇİMİ
# ---------------------------------------------------------

st.header("🤖 Akıllı Cihaz Analizi")

selected_device = st.selectbox(
    "Analiz etmek istediğiniz cihazı seçin:",
    df["Cihaz"].tolist()
)

selected = df[
    df["Cihaz"] == selected_device
].iloc[0]

device_energy = selected["Yıllık Enerji (kWh)"]
device_carbon = selected["Yıllık CO2e (kg)"]
device_power = selected["Güç (W)"]
device_hours = selected["Günlük Kullanım (saat)"]
device_standby = selected["Bekleme (saat)"]
device_yearly_cost = selected["Yıllık Maliyet (TL)"]

# ---------------------------------------------------------
# SEÇİLEN CİHAZ ÖZETİ
# ---------------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Güç",
        f"{device_power:.0f} W"
    )

with col2:
    st.metric(
        "Günlük Kullanım",
        f"{device_hours:.1f} saat"
    )

with col3:
    st.metric(
        "Yıllık Enerji",
        f"{device_energy:,.2f} kWh"
    )

with col4:
    st.metric(
        "Yıllık CO₂e",
        f"{device_carbon:,.2f} kg"
    )

with col5:
    st.metric(
        "Yıllık Maliyet",
        f"{device_yearly_cost:,.2f} TL"
    )

# ---------------------------------------------------------
# OTOMATİK AKILLI ÖNERİ
# ---------------------------------------------------------

st.subheader("💡 Akıllı Tasarruf Önerisi")

if device_energy >= 2000:

    st.error(
        f"🔴 {selected_device} yüksek enerji tüketen bir cihazdır. "
        "Enerji verimli çalışma modları, kullanım süresi optimizasyonu "
        "ve mümkün olan durumlarda düşük güç modlarının kullanılması önerilir."
    )

elif device_energy >= 500:

    st.warning(
        f"🟠 {selected_device} orta-yüksek seviyede enerji tüketmektedir. "
        "Kullanılmadığı dönemlerde güç yönetimi ve tasarruf modlarının "
        "kullanılması önerilir."
    )

else:

    st.success(
        f"🟢 {selected_device} düşük enerji tüketim seviyesindedir. "
        "Bekleme süresinin azaltılması ve uygun güç yönetimi ile "
        "ek tasarruf sağlanabilir."
    )

# ---------------------------------------------------------
# BEKLEME SÜRESİ ANALİZİ
# ---------------------------------------------------------

st.subheader("⏱️ Bekleme Süresi Analizi")

if device_standby > 12:

    st.warning(
        f"⚠️ Cihazın günlük bekleme süresi "
        f"{device_standby:.1f} saattir. "
        "Bekleme süresinin azaltılması enerji tüketimini düşürebilir."
    )

elif device_standby > 0:

    st.info(
        f"ℹ️ Cihazın günlük bekleme süresi "
        f"{device_standby:.1f} saattir. "
        "Uygun güç yönetimi ile bekleme tüketimi optimize edilebilir."
    )

else:

    st.success(
        "✅ Cihaz için tanımlanan günlük bekleme süresi bulunmamaktadır."
    )

st.divider()

# ---------------------------------------------------------
# TASARRUF SİMÜLASYONU
# ---------------------------------------------------------

st.header("📉 Akıllı Tasarruf Simülasyonu")

st.write(
    "Tasarruf oranını değiştirerek toplam sistem ve seçilen cihaz "
    "üzerindeki olası enerji, karbon ve maliyet azaltımını inceleyebilirsiniz."
)

savings_rate = st.slider(
    "Tasarruf oranı (%)",
    min_value=0,
    max_value=50,
    value=20,
    step=5
)

rate = savings_rate / 100

# ---------------------------------------------------------
# TOPLAM TASARRUF
# ---------------------------------------------------------

energy_saving = total_energy * rate
remaining_energy = total_energy - energy_saving

carbon_saving = total_carbon * rate
remaining_carbon = total_carbon - carbon_saving

money_saving = total_yearly_cost * rate
remaining_cost = total_yearly_cost - money_saving

# ---------------------------------------------------------
# TOPLAM TASARRUF SONUÇLARI
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Enerji Tasarrufu",
        f"{energy_saving:,.2f} kWh/yıl"
    )

with col2:
    st.metric(
        "CO₂e Azaltımı",
        f"{carbon_saving:,.2f} kg/yıl"
    )

with col3:
    st.metric(
        "💰 Para Tasarrufu",
        f"{money_saving:,.2f} TL/yıl"
    )

with col4:
    st.metric(
        "Kalan Yıllık Maliyet",
        f"{remaining_cost:,.2f} TL"
    )

st.divider()

# ---------------------------------------------------------
# TASARRUF SONRASI DURUM
# ---------------------------------------------------------

st.subheader("📊 Tasarruf Sonrası Sistem Durumu")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Tasarruf Sonrası Enerji",
        f"{remaining_energy:,.2f} kWh/yıl"
    )

with col2:

    st.metric(
        "Tasarruf Sonrası CO₂e",
        f"{remaining_carbon:,.2f} kg/yıl"
    )

with col3:

    st.metric(
        "Tasarruf Sonrası Maliyet",
        f"{remaining_cost:,.2f} TL/yıl"
    )

st.divider()

# ---------------------------------------------------------
# SEÇİLEN CİHAZ İÇİN TASARRUF
# ---------------------------------------------------------

st.subheader(
    f"🏥 {selected_device} İçin Tasarruf Simülasyonu"
)

selected_energy_saving = device_energy * rate
selected_carbon_saving = device_carbon * rate
selected_money_saving = device_yearly_cost * rate

selected_remaining_energy = (
    device_energy - selected_energy_saving
)

selected_remaining_carbon = (
    device_carbon - selected_carbon_saving
)

selected_remaining_cost = (
    device_yearly_cost - selected_money_saving
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Enerji Tasarrufu",
        f"{selected_energy_saving:,.2f} kWh/yıl"
    )

with col2:

    st.metric(
        "CO₂e Azaltımı",
        f"{selected_carbon_saving:,.2f} kg/yıl"
    )

with col3:

    st.metric(
        "💰 Para Tasarrufu",
        f"{selected_money_saving:,.2f} TL/yıl"
    )

# ---------------------------------------------------------
# CİHAZ TASARRUF KARŞILAŞTIRMASI
# ---------------------------------------------------------

comparison_df = pd.DataFrame({
    "Durum": [
        "Mevcut",
        "Tasarruf Sonrası"
    ],
    "Enerji (kWh/yıl)": [
        device_energy,
        selected_remaining_energy
    ],
    "CO₂e (kg/yıl)": [
        device_carbon,
        selected_remaining_carbon
    ],
    "Maliyet (TL/yıl)": [
        device_yearly_cost,
        selected_remaining_cost
    ]
})

st.subheader("📊 Cihaz Tasarruf Karşılaştırması")

st.bar_chart(
    comparison_df.set_index("Durum")
)

st.divider()

# ---------------------------------------------------------
# CİHAZ BAZLI TASARRUF
# ---------------------------------------------------------

st.subheader("🏥 Tüm Cihazların Tasarruf Potansiyeli")

simulation_df = df.copy()

simulation_df["Enerji Tasarrufu (kWh/yıl)"] = (
    simulation_df["Yıllık Enerji (kWh)"] * rate
)

simulation_df["CO2e Azaltımı (kg/yıl)"] = (
    simulation_df["Yıllık CO2e (kg)"] * rate
)

simulation_df["Para Tasarrufu (TL/yıl)"] = (
    simulation_df["Yıllık Maliyet (TL)"] * rate
)

simulation_df["Tasarruf Sonrası Enerji (kWh/yıl)"] = (
    simulation_df["Yıllık Enerji (kWh)"]
    - simulation_df["Enerji Tasarrufu (kWh/yıl)"]
)

simulation_df["Tasarruf Sonrası CO2e (kg/yıl)"] = (
    simulation_df["Yıllık CO2e (kg)"]
    - simulation_df["CO2e Azaltımı (kg/yıl)"]
)

simulation_df["Tasarruf Sonrası Maliyet (TL/yıl)"] = (
    simulation_df["Yıllık Maliyet (TL)"]
    - simulation_df["Para Tasarrufu (TL/yıl)"]
)

st.dataframe(
    simulation_df[
        [
            "Cihaz",
            "Yıllık Enerji (kWh)",
            "Enerji Tasarrufu (kWh/yıl)",
            "Yıllık CO2e (kg)",
            "CO2e Azaltımı (kg/yıl)",
            "Yıllık Maliyet (TL)",
            "Para Tasarrufu (TL/yıl)"
        ]
    ],
    use_container_width=True
)

# ---------------------------------------------------------
# EN FAZLA TASARRUF SAĞLAYACAK CİHAZ
# ---------------------------------------------------------

best_saving_device = simulation_df.loc[
    simulation_df["Enerji Tasarrufu (kWh/yıl)"].idxmax()
]

best_money_device = simulation_df.loc[
    simulation_df["Para Tasarrufu (TL/yıl)"].idxmax()
]

st.success(
    f"💡 %{savings_rate} tasarruf senaryosunda "
    f"enerji açısından en yüksek tasarruf potansiyeline sahip cihaz: "
    f"**{best_saving_device['Cihaz']}** "
    f"({best_saving_device['Enerji Tasarrufu (kWh/yıl)']:.2f} kWh/yıl)"
)

st.info(
    f"💰 Ekonomik açıdan en yüksek yıllık tasarruf potansiyeline sahip cihaz: "
    f"**{best_money_device['Cihaz']}** "
    f"({best_money_device['Para Tasarrufu (TL/yıl)']:.2f} TL/yıl)"
)

# ---------------------------------------------------------
# GENEL SONUÇ
# ---------------------------------------------------------

st.divider()

st.header("🌍 Genel Değerlendirme")

st.write(
    f"Mevcut durumda cihaz grubunun yıllık enerji tüketimi "
    f"**{total_energy:,.2f} kWh**, yıllık karbon ayak izi "
    f"**{total_carbon:,.2f} kg CO₂e** ve yıllık enerji maliyeti "
    f"**{total_yearly_cost:,.2f} TL** olarak hesaplanmıştır."
)

st.write(
    f"Seçilen **%{savings_rate} tasarruf senaryosunda**, "
    f"yıllık **{energy_saving:,.2f} kWh enerji**, "
    f"**{carbon_saving:,.2f} kg CO₂e** ve "
    f"**{money_saving:,.2f} TL** tasarruf potansiyeli bulunmaktadır."
)

st.write(
    f"Seçilen cihaz **{selected_device}** için aynı senaryoda "
    f"**{selected_energy_saving:,.2f} kWh/yıl enerji**, "
    f"**{selected_carbon_saving:,.2f} kg CO₂e/yıl** ve "
    f"**{selected_money_saving:,.2f} TL/yıl** azaltım potansiyeli bulunmaktadır."
)

# ---------------------------------------------------------
# PROJE DURUMU
# ---------------------------------------------------------

st.divider()

st.caption(
    "Tıbbi Cihaz Enerji ve Karbon Ayak İzi Analiz Sistemi | "
    "Enerji • Karbon • Maliyet • Akıllı Tasarruf"
)
