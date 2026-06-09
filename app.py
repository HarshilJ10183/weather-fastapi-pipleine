from fastapi import FastAPI
import urllib.request
import json
import sqlite3  # I added this so I can talk to my SQL database!

app = FastAPI()

# My personal API Key and the name I want for my database file
API_KEY = "8a470e00b51841df94a150534260906"
DB_NAME = "my_weather_tracker.db"

# I'm setting up my database table here. If it doesn't exist yet, I'll create it.
def setup_my_database():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                temperature_c REAL,
                condition TEXT
            )
        """)
        conn.commit()

# I want my database to be ready the second my server starts up
setup_my_database()

@app.get("/")
def read_root():
    return {"status": "Success", "message": "My backend has a memory now!"}

@app.get("/weather")
def get_weather(city: str = "Oshawa"):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    
    try:
        # I am reaching out to the live internet to grab my raw data
        with urllib.request.urlopen(url) as response:
            raw_data = response.read()
            weather_dict = json.loads(raw_data)
            
            # I only want to keep the specific data that matters to me
            clean_data = {
                "city": weather_dict["location"]["name"],
                "temperature_c": weather_dict["current"]["temp_c"],
                "condition": weather_dict["current"]["condition"]["text"]
            }
            
            # Now, I'm saving my clean data straight into my SQL database!
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO weather_logs (city, temperature_c, condition)
                    VALUES (?, ?, ?)
                """, (clean_data["city"], clean_data["temperature_c"], clean_data["condition"]))
                conn.commit()
            
            # Finally, I'll return a success message so I know it worked
            return {"message": "Data saved successfully to my database!", "data": clean_data}
            
    except Exception as e:
        return {"error": "Could not fetch weather data", "details": str(e)}

# I need a new web page to look at all the historical data I've saved!
@app.get("/history")
def get_my_history():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row  # This makes my SQL rows look like clean dictionaries
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM weather_logs ORDER BY id DESC")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]