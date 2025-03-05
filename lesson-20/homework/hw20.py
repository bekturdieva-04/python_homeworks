import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")
conn = sqlite3.connect("chinook.db")
df = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(df)

query = """
    SELECT Customer.CustomerId, Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS TotalSpent
    FROM Invoice
    JOIN Customer ON Invoice.CustomerId = Customer.CustomerId
    GROUP BY Customer.CustomerId
    ORDER BY TotalSpent DESC
    LIMIT 5;
"""
top_customers = pd.read_sql(query, conn)
print("Top 5 Customers by Total Purchases:\n", top_customers)

query_albums = """
    SELECT DISTINCT Invoice.CustomerId
    FROM InvoiceLine
    JOIN Track ON InvoiceLine.TrackId = Track.TrackId
    JOIN Album ON Track.AlbumId = Album.AlbumId
    GROUP BY Invoice.CustomerId, Album.AlbumId
    HAVING COUNT(DISTINCT Track.TrackId) = (SELECT COUNT(Track.TrackId) FROM Track WHERE Track.AlbumId = Album.AlbumId)
"""
customers_who_bought_albums = pd.read_sql(query_albums, conn)

query_all_customers = "SELECT DISTINCT CustomerId FROM Invoice"
all_customers = pd.read_sql(query_all_customers, conn)

album_buyers = set(customers_who_bought_albums["CustomerId"])
all_customers_set = set(all_customers["CustomerId"])
individual_buyers = all_customers_set - album_buyers

percent_album_buyers = len(album_buyers) / len(all_customers_set) * 100
percent_individual_buyers = len(individual_buyers) / len(all_customers_set) * 100

print("\nPercentage of customers buying full albums: {:.2f}%".format(percent_album_buyers))
print("Percentage of customers buying individual tracks: {:.2f}%".format(percent_individual_buyers))

conn.close()
