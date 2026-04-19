import json
import datetime
import os

# Simulando la captura de noticias del día
# En el futuro, aquí conectarías APIs reales de ESPN o X
today = datetime.date.today().strftime("%B %d, %Y")

daily_intelligence = [
    {
        "source": "ESPN National",
        "trend": f"NCAA officials discussing new NIL eligibility rules for {today}."
    },
    {
        "source": "X (Recruit Tracker)",
        "trend": "Four-star Offensive Lineman schedules official visit to South Bend."
    },
    {
        "source": "Irish Breakdown Boards",
        "trend": "Trending: Debate over quarterback rotation intensity in spring practice."
    }
]

# Guardamos el archivo que app.py va a leer
with open('news_data.json', 'w', encoding='utf-8') as f:
    json.dump(daily_intelligence, f, indent=4)

print(f"Success: news_data.json updated for {today}")
