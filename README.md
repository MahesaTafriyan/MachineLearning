# 🤖 Hand Gesture Recognition & Control System  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)  
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10%2B-orange)  
![YOLOv8](https://img.shields.io/badge/YOLOv8-8.0%2B-red)  

Sistem canggih yang menggabungkan:  
- **Deteksi gestur tangan** dengan klasifikasi pesan  
- **Kontrol mouse** menggunakan jari telunjuk  
- **Deteksi objek real-time** dengan YOLOv8  

## 🌟 Fitur Utama
1. **Gesture Recognition**  
   - Mengenali 6+ gestur tangan (e.g., "Haloo", "Nama aku Gamma")  
   - Deteksi sentuhan jempol-telunjuk ("sehat selalu")  

2. **Air Mouse Controller**  
   - Kontrol kursor komputer dengan gerakan jari telunjuk  
   - Optimasi FPS tinggi (>30fps)  

3. **Object Detection**  
   - Integrasi YOLOv8 untuk deteksi objek bersamaan  

## 🛠️ Instalasi
### Prasyarat
- Python 3.8+
- Webcam

### Langkah Instalasi
```bash
https://github.com/MahesaTafriyan/MachineLearning.git
cd MachineLearning
pip install -r requirements.txt
```

## Cara Menjalankan

### 1. Deteksi Gestur + YOLOv8
```bash
python gesture_control.py
```

Gestur yang dikenali:

Gestur (Jari Terbuka)	Pesan
👍 + 👆	"sehat selalu"
✋ (5 jari)	"Haloo"
✌️ (2 jari)	"HAIII"

### 2. Kontrol Mouse
```bash
python mouse_controller.py
```
Fitur:

- Gerakkan jari telunjuk untuk kontrol kursor
- FPS real-time display
