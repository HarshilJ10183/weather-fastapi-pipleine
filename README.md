
# 🌤️ Enterprise Weather Data Pipeline

A lightweight, real-time data ingestion pipeline and RESTful API built with Python and FastAPI. This backend application fetches live meteorological data, processes it into a clean format, and stores it in a relational database for historical tracking.

## 🚀 Features
* **Real-Time Data Ingestion:** Connects to external weather APIs to fetch live current conditions.
* **Data Transformation:** Cleans and processes raw JSON payloads into structured, usable dictionaries.
* **Persistent Storage:** Utilizes SQLite to automatically log and store historical weather queries.
* **REST API Endpoints:** Exposes clean endpoints for users to trigger pipelines and view historical data.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Framework:** FastAPI
* **Server:** Uvicorn (ASGI)
* **Database:** SQLite (Relational SQL)

## 💻 How to Run Locally

1. **Clone the repository:**
```bash
git clone [https://github.com/HarshilJ10183/weather-fastapi-pipleine.git](https://github.com/HarshilJ10183/weather-fastapi-pipleine.git)
cd weather-fastapi-pipleine

```

2. **Install the required dependencies:**

```bash
pip install fastapi uvicorn

```

3. **Start the server:**

```bash
python3 -m uvicorn app:app --reload

```

4. **Test the Endpoints:**

* Open your browser and go to `http://127.0.0.1:8000/weather?city=Oshawa` to run the pipeline.
* Go to `http://127.0.0.1:8000/history` to view your saved SQL database logs.

```

Once you hit that Commit button, click on your "weather-fastapi-pipleine" repository name at the top left to go back to your main repo page. It should now render beautifully with proper headers, bold text, and clean grey code blocks! Let me know if it looks correct on the main page now.

```
