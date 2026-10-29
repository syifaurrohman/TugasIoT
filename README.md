# AVAS - Automatic Vibration & Audio Safety System 🚨

> **Sistem Deteksi Keamanan Kabin Transportasi Berbasis Multi-Sensor & MQTT Cloud**

Proyek IoT ini dirancang untuk mendeteksi kondisi darurat di dalam kabin kendaraan (seperti kecelakaan ringan, benturan, atau suara panik/teriakan) secara *real-time* menggunakan sensor dari *smartphone*.

---

## 📌 Pemenuhan Syarat Tugas IoT

| Kategori | Spesifikasi Terimplementasi |
| :--- | :--- |
| **Edge Devices** | **3 Perangkat** 3 Perangkat (HP 1 sebagai Sensor Node, Laptop sebagai Gateway, & HP 2 sebagai Dashboard).  Note: dalam pembuatan ini kedua HP merupakan iPhone. |
| **Sensors** | **2 Sensor** (Accelerometer & Microphone) |
| **Data Processing** | 1. **Audio Moving Average Filter** (Peredam *noise* suara, $N=5$)<br>2. **Threshold Check & Decision Logic** |
| **Algoritma** | **Sensor Fusion Rules** (Kombinasi Amplitudo Suara & *Magnitude* Percepatan) |
| **Protokol Cloud** | **MQTT Broker** (`broker.emqx.io` pada port `1883`) |
| **Topik MQTT** | • Sensor: `kelompok14/avas/sensor`<br>• Status: `kelompok14/avas/status` |

---

## ⚙️ Cara Menjalankan Program

### 1. Persiapan Perangkat Pengirim (HP 1)
1. Buka browser di **HP 1**, akses `iot.myudak.com`[cite: 23].
2. Aktifkan sensor **Accelerometer** dan **Microphone**[cite: 23].
3. Atur MQTT Broker ke `broker.emqx.io` (Port `1883`) dan set topik pengiriman ke: `kelompok14/avas/sensor`[cite: 23, 40].

### 2. Menjalankan Processing Gateway (Laptop)
1. Clone repository ini ke laptop Anda:
   ```bash
   git clone [https://github.com/syifaurrohman/TugasIoT.git](https://github.com/syifaurrohman/TugasIoT.git)
   cd TugasIoT

2. Pastikan library paho-mqtt sudah terinstal:
```bash
pip install paho-mqtt
```
3. Jalankan script Python pemrosesan:
python AVAS.py
### 3. Konfigurasi Dashboard Pemantau (HP 2)
1. Buka aplikasi **IoT MQTT Panel** di iOS/Android.
2. Buat koneksi baru ke broker `broker.emqx.io` (Port `1883`).
3. Tambahkan widget *Text View* dengan subscribe ke topik: `kelompok14/avas/status`.
