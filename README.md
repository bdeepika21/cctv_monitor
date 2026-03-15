
# 🎥 CCTV & SIM Monitoring System

This project is a backend prototype designed to automate the monitoring of centralized CCTV systems. It focuses on detecting camera downtime and SIM connectivity issues in real-time.

## 🚀 Overview
The system bridges the gap between hardware status and maintenance response. By polling SIM service provider APIs, it identifies faults early and logs them for the technical team, ensuring "Audit Logging" compliance as required by government standards.

## ⚙️ Backend Logic & Fault Detection
The core monitoring engine is built with **Python** and handles:

* **Data Acquisition:** Processes incoming **JSON** data feeds from service providers (e.g., Jio, Airtel) to track `status` and `signal_strength`.
* **Threshold Analysis:** Uses the `datetime` module to calculate downtime. If a camera is unreachable for more than **10 minutes**, it triggers an alert.
* **Automated Alerting:** Generates a structured alert dictionary containing the `camera_id`, `message`, and `status`.

## 🗄️ Database Architecture
The system uses **SQLite** for data persistence and accountability:

* **Tickets Table:** Logs every detected fault with location and downtime duration for repair prioritization.
* **Audit Logs:** A mandatory security feature that tracks every administrative action.
    * **Columns:** `id`, `user_name`, `action_type`, `target_id`, `timestamp`.
    * **Purpose:** Ensures a transparent "paper trail" for all status updates and deletions.

## 🔑 Role-Based Access Control (RBAC)
To maintain **Cybersecurity Compliance**, the system enforces strict permission levels:

* **Admin:** Full access to create, update, and delete camera records and tickets.
* **Technician:** Limited access to view dashboards and update ticket statuses (e.g., from "Open" to "Fixed").

## 🛠️ Tech Stack & Setup
* **Language:** Python 3.x
* **Framework:** Flask / Django
* **Database:** SQLite
* **Data Format:** JSON

---
