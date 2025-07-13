# 🔌 ESP32 Controller Logger

A complete IoT system where an ESP32 microcontroller sends JSON data (such as button presses or sensor readings) to a FastAPI backend, which logs it in a PostgreSQL database.

---

## 🚀 Features

- 📡 ESP32 sends interaction or sensor data as JSON
- ⚡ FastAPI backend handles HTTP POST requests
- 🗃️ Data logged to PostgreSQL using SQLAlchemy ORM
- 🔐 Structured using Pydantic for validation
- 🧱 Modular architecture for clean, scalable code

---

## 🏗️ Architecture
ESP32 Device ──(HTTP POST)──▶ FastAPI Server ──▶ PostgreSQL

---

## 🧰 Tech Stack

- **ESP32** (Arduino framework, C++)
- **FastAPI** (Python 3.9+)
- **PostgreSQL** (JSONB logging)
- **SQLAlchemy** (ORM for DB access)
- **Uvicorn** (ASGI server)
