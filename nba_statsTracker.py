import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html'  # Replace with url u need

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting table data
table = soup.find('table', {'id': 'per_game_stats'})
rows = table.find_all('tr')

data = []
for row in rows[1:]:
    cols = row.find_all(['th', 'td'])
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Creating a DataFrame
columns = ['Rk', 'Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%',
           'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

df = pd.DataFrame(data, columns=columns)

# Increase the display option to show more rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Displaying the entire DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('NBA_2024_stats.csv', index=False)

print("CSV file saved successfully.")