import json
import datetime

# Aquí simularías el scraping de ESPN, X y Boards
new_data = [
    {"source": "ESPN", "trend": f"Update for {datetime.date.today()}: Portal changes..."},
    {"source": "X", "trend": "New recruit activity detected..."},
    {"source": "Boards", "trend": "Latest fan sentiment analysis..."}
]

with open('news_data.json', 'w') as f:
    json.dump(new_data, f)
