# ⚡ DRIEMX-CyberToolkit

> **Lightweight Cyber Reconnaissance & Network Diagnostics Suite for Android & Mobile Environments.**

![Python](https://img.shields.io/badge/Python-3.x-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Linux-blue)
![Author](https://img.shields.io/badge/Author-elisandroofc-cyan)
![Brand](https://img.shields.io/badge/Brand-DRIEMX-amber)

---

## 📌 About The Project

**DRIEMX-CyberToolkit** is a fast, terminal-based reconnaissance tool built by **elisandroofc** under the **DRIEMX Ecosystem**. Designed specifically to run natively on mobile devices via **Termux** or **Pydroid 3**, it provides essential tools for web header analysis, DNS resolution, and IP geolocation without heavy dependencies.

🌐 **Official Website:** [https://elisandroofc.netlify.app/](https://elisandroofc.netlify.app/)

---

## 🚀 Features

- 🔍 **HTTP Header Analyzer:** Audit target web servers for security headers and server exposure.
- 🌐 **IP & Domain Recon:** Extract IP addresses, ISP information, country location, and ASN records.
- 📱 **Mobile Native:** 100% optimized for Android terminal environments (Termux / Pydroid).
- 🎨 **Cyberpunk Terminal UI:** Lightweight ASCII UI with zero heavy external library requirements.

---

## 🛠️ Installation & Usage

### On Android (Termux):
```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python & Git
pkg install python git -y

# Clone repository
git clone [https://github.com/elisandrocontreras2024-cmd/DRIEMX-CyberToolkit.git](https://github.com/elisandrocontreras2024-cmd/DRIEMX-CyberToolkit.git)

# Navigate and run
cd DRIEMX-CyberToolkit
python main.py
