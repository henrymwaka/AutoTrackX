<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue.svg?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Django-4.2-092E20.svg?style=for-the-badge&logo=django"/>
  <img src="https://img.shields.io/badge/DRF-REST_API-orange.svg?style=for-the-badge&logo=django"/>
  <img src="https://img.shields.io/badge/Gunicorn-Server-success.svg?style=for-the-badge&logo=gunicorn"/>
  <img src="https://img.shields.io/badge/Nginx-Reverse_Proxy-brightgreen.svg?style=for-the-badge&logo=nginx"/>
  <img src="https://img.shields.io/badge/Cloudflare-Tunnel-orange.svg?style=for-the-badge&logo=cloudflare"/>
</p>

<h1 align="center">🚗 AutoTrackX</h1>
<p align="center">
  <strong>Hybrid Vehicle Tracking & Maintenance Intelligence Platform</strong><br>
  Integrated under <a href="https://reslab.dev">reslab.dev</a> — built by Dr. Henry Mwaka.
</p>

---

## 🧭 Overview

**AutoTrackX** is a hybrid fleet and personal-vehicle management system that unifies  
GPS tracking, repair history, mechanic accountability, and cost analytics.  
It extends beyond conventional trackers to integrate **maintenance intelligence**,  
**predictive service alerts**, and **verified workshop logs**.

| Component | Function |
|------------|-----------|
| Frontend | Web dashboard & mobile app |
| Backend | Django + REST Framework API |
| Database | PostgreSQL (production) / SQLite (local) |
| Deployment | Ubuntu 22.04 LTS · Gunicorn · Nginx · Cloudflare Tunnel |
| Repository | [github.com/henrymwaka/AutoTrackX](https://github.com/henrymwaka/AutoTrackX) |

---

## ⚙️ Core Modules

| Module | Description |
|---------|--------------|
| `core` | Users, vehicles, ownership, authentication |
| `tracking` | GPS data, trip logs, driver behaviour |
| `maintenance` | Repairs, spare parts, invoices, workshop feedback |
| `analytics` | Cost trends, predictive service intervals |
| `api` | REST endpoints and authentication (JWT/Token) |

---

## 🧩 File Structure
AutoTrackX/
├── backend/
│ ├── autotrackx_site/ # Django project settings, urls, wsgi
│ ├── core/ # User & vehicle base app
│ ├── tracking/ # Trip & GPS logic
│ ├── maintenance/ # Repair logs, invoices
│ ├── analytics/ # Reports & summaries
│ ├── manage.py
│ └── requirements.txt
├── frontend/ # (optional React / Next.js UI)
├── docs/
│ └── deployment.md
└── .github/workflows/deploy.yml


---

## 🧰 Quick Setup (Manual)

```bash
git clone https://github.com/henrymwaka/AutoTrackX.git
cd AutoTrackX/backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

🚀 Deployment (Production)

AutoTrackX is deployed under:

Frontend: https://autotrackx.reslab.dev

API: https://api.autotrackx.reslab.dev

Server pattern (ResLab standard):
Cloudflare → Nginx (127.0.0.1:80)
→ Gunicorn (/run/gunicorn/autotrackx.sock)
→ Django (AutoTrackX backend)
sudo systemctl restart autotrackx.service
sudo systemctl reload nginx
🔄 Continuous Deployment

A GitHub Actions workflow .github/workflows/deploy.yml automatically:

SSHs into your ResLab server

Pulls the latest code

Installs dependencies

Runs migrations + collectstatic

Restarts autotrackx.service safely

Secrets required:

RESLAB_SSH_KEY

📦 Requirements

See requirements.txt
.

👤 Maintainer

Dr. Henry Mwaka
National Agricultural Research Laboratories (NARL) — NARO, Uganda
📧 henry.mwaka@naro.go.ug

🔗 https://reslab.dev

<p align="center"> <img src="https://img.shields.io/badge/Version-1.0.0-blue.svg?style=for-the-badge"/> <img src="https://img.shields.io/badge/Deployment-Nov_2025-important.svg?style=for-the-badge"/> <img src="https://img.shields.io/badge/Maintainer-Dr_Henry_Mwaka-lightgrey.svg?style=for-the-badge"/> </p> <p align="center"> © 2025 ResLab — National Agricultural Research Laboratories (NARL), Uganda </p> ```
📦 requirements.txt
# Core Framework
Django==4.2.11
djangorestframework==3.15.2
django-cors-headers==4.3.1

# Database
psycopg2-binary==2.9.9

# Web Server
gunicorn==22.0.0

# Utilities
python-dotenv==1.0.1
requests==2.32.3
pytz==2024.1

# Optional extras for analytics
pandas==2.2.3
numpy==2.1.3

