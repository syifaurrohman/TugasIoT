# AVAS - Automatic Vibration & Audio Safety System
import json
from collections import deque
import paho.mqtt.client as mqtt

# Konfigurasi MQTT Broker EMQX
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC_SENSOR = "kelompok14/avas/sensor"
TOPIC_STATUS = "kelompok14/avas/status"

# Buffer untuk Moving Average Audio
audio_buffer = deque(maxlen=5)

# Threshold Pengujian
AUDIO_THRESHOLD = 0.6  # Batas suara
ACCEL_THRESHOLD = 11.5  # Batas percepatan guncangan


def on_connect(client, userdata, flags, rc):
  print(f"[INFO] Terhubung ke Broker MQTT dengan kode hasil: {rc}")
  client.subscribe(TOPIC_SENSOR)


def on_message(client, userdata, msg):
  try:
    payload_str = msg.payload.decode()
    data = json.loads(payload_str)

    # Mengambil data dari struktur iot.myudak.com (HP 1)
    sensors = data.get("sensors", {})
    accel_data = sensors.get("accelerometer", {})
    mic_data = sensors.get("microphone", {})

    accel_total = accel_data.get("magnitude", 9.8)
    raw_rms = mic_data.get("rms", 0.0)

    # Scaling nilai mic agar tidak terlalu kecil
    rms_audio = raw_rms * 10.0

    # PROCESSING 1: Audio Moving Average Filter
    audio_buffer.append(rms_audio)
    avg_audio = (
        sum(audio_buffer) / len(audio_buffer) if audio_buffer else rms_audio
    )

    # PROCESSING 2: Threshold Check & Decision Logic
    is_noisy = avg_audio > AUDIO_THRESHOLD
    is_shaken = accel_total > ACCEL_THRESHOLD

    # Menentukan status
    if is_noisy and is_shaken:
      status = "BAHAYA: TERDETEKSI BENTURAN DAN SUARA PANIK"
      details = (
          f"Guncangan Ekstrem ({accel_total:.2f}) & Suara Tinggi"
          f" ({avg_audio:.4f})"
      )
    elif is_noisy:
      status = "PERINGATAN: TERDETEKSI SUARA TINGGI"
      details = (f"Suara Tinggi ({avg_audio:.4f}), Guncangan Normal ({accel_total:.2f})")
    elif is_shaken:
      status = "PERINGATAN: TERDETEKSI GUNCANGAN KERAS"
      details = (f"Guncangan Tinggi ({accel_total:.2f}), Suara Normal ({avg_audio:.4f})")
    else:
      status = "KABIN AMAN"
      details = f"Normal - Accel: {accel_total:.2f}, Audio RMS: {avg_audio:.4f}"

    print(f"[PROSES LAPTOP] {status} | {details}")

    # Kirim hasil status ke dashboard HP 2
    status_message = f"{status} | {details}"
    client.publish(TOPIC_STATUS, status_message)

  except Exception as e:
    print(f"[ERROR] Gagal memproses data: {e}")


# Inisialisasi MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
print("[INFO] Laptop mendengarkan data dari HP 1...")
client.loop_forever()
