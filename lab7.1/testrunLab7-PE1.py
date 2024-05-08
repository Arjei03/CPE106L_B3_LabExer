import csv
import matplotlib.pyplot as plt

# Load the data set and clean it
data = {}
with open('breadprice.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        year = int(row[0])
        prices = [float(price) for price in row[1:] if price]
        average_price = sum(prices) / len(prices)
        data[year] = average_price

# Display a line plot of the average price for each year
plt.figure(figsize=(10, 6))
plt.plot(list(data.keys()), list(data.values()), marker='o')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.title('Average Price of Bread per Year')
plt.grid(True)
plt.show()
