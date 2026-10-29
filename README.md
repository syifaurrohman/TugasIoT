# AVAS - Automatic Vibration & Audio Safety System 

> **Sistem Deteksi Keamanan Kabin Transportasi Berbasis Multi-Sensor & MQTT Cloud**

Proyek IoT ini dirancang untuk mendeteksi kondisi darurat di dalam kabin kendaraan (seperti kecelakaan ringan, benturan, atau suara panik/teriakan) secara *real-time* menggunakan sensor dari *smartphone*.



## Pemenuhan Syarat Tugas IoT

| Kategori | Spesifikasi Terimplementasi |
| :--- | :--- |
| **Edge Devices** | **2 Perangkat** (HP 1 via `iot.myudak.com` & HP 2/Laptop sebagai Receiver Status) |
| **Sensors** | **2 Sensor** (Accelerometer & Microphone) |
| **Data Processing** | 1. **Audio Moving Average Filter** (Peredam *noise* suara)<br>2. **Threshold & Decision Logic** |
| **Algoritma** | **Sensor Fusion Rules** (Kombinasi Amplitudo Suara & *Magnitude* Percepatan) |
| **Protokol Cloud** | **MQTT Broker** (`broker.emqx.io` pada port `1883`) |
| **Topik MQTT** | • Sensor: `kelompok14/avas/sensor`<br>• Status: `kelompok14/avas/status` |



## Cara Menjalankan Program

### 1. Persiapan Perangkat
1. Buka browser di **HP 1**, akses `iot.myudak.com`.
2. Aktifkan sensor **Accelerometer** dan **Microphone**.
3. Atur MQTT WSS Broker dan set topik ke: `kelompok14/avas/sensor`.

### 2. Jalankan Program Laptop / Server
1. Clone repository ini:
   ```bash
   git clone [https://github.com/USERNAME_KAMU/avas-iot-project.git](https://github.com/USERNAME_KAMU/avas-iot-project.git)
   cd avas-iot-project
