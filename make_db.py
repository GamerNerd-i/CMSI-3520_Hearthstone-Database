import pandas as pd
import sqlite3

df = pd.read_csv("deck_data.csv")
print(df.head())
print(df.tail())


connection = sqlite3.connect("decks.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS decks")

df.to_sql("decks", connection)
connection.close()
