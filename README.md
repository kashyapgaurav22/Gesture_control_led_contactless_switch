# 🔌 Gesture Controlled LED using Contactless Switch

A **gesture-based LED control system** that allows users to turn LEDs ON/OFF using **hand gestures**, without any physical contact. This project uses **computer vision** and **hand tracking** to act as a **contactless switch**, making it ideal for smart and touch-free applications.

---

## 📌 Project Overview

This project captures live video from a webcam, detects hand gestures in real time, and maps each finger to a specific LED connected to an **Arduino**. When a finger is raised, the corresponding LED turns ON; lowering the finger turns it OFF.

---

## 🚀 Features

- 🖐️ Real-time hand gesture recognition  
- 💡 Individual LED control using fingers  
- ❌ No physical switches (contactless control)  
- ⚡ Fast and responsive system  
- 🧠 Computer vision + hardware integration  

---

## 🛠️ Tech Stack

### Software
- Python  
- OpenCV  
- CVZone (Hand Tracking Module)  
- PyFirmata  

### Hardware
- Arduino (UNO / Nano)  
- LEDs (5)  
- Resistors  
- Breadboard  
- USB Webcam  

---

## ⚙️ Working Principle

1. Webcam captures real-time video.
2. Hand landmarks are detected using CVZone.
3. Each finger represents a virtual switch.
4. Python sends control signals to Arduino via PyFirmata.
5. Arduino controls LEDs based on finger gestures.

---

## 🔧 Pin Configuration

| Finger  | LED Pin |
|--------|---------|
| Thumb  | D8      |
| Index  | D9      |
| Middle | D10     |
| Ring   | D11     |
| Pinky | D12     |


---

