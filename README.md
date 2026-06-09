#  Enterprise Weather Data Pipeline

A lightweight, real-time data ingestion pipeline and RESTful API built with Python and FastAPI. This backend application fetches live meteorological data, processes it into a clean format, and stores it in a relational database for historical tracking.

##  Features
* **Real-Time Data Ingestion:** Connects to external weather APIs to fetch live current conditions.
* **Data Transformation:** Cleans and processes raw JSON payloads into structured, usable dictionaries.
* **Persistent Storage:** Utilizes SQLite to automatically log and store historical weather queries.
* **REST API Endpoints:** Exposes clean endpoints for users to trigger pipelines and view historical data.

##  Tech Stack
* **Language:** Python 3
* **Framework:** FastAPI
* **Server:** Uvicorn (ASGI)
* **Database:** SQLite (Relational SQL)

##  How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/weather-fastapi-pipeline.git](https://github.com/YOUR_USERNAME/weather-fastapi-pipeline.git)
   cd weather-fastapi-pipeline