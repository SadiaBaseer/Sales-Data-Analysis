import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("supermarket_sales - Sheet1.csv")


# Convert Date column to proper format
df["Date"] = pd.to_datetime(df["Date"], format="mixed")


#Displaying columns Name
print(df.columns) # or you can use .keys() function or this .columns method

#for basic info like datatypes and list out all columns
df.info()

#checkiing for missing values
print(df.isnull().sum())

#checking for duplicates value
print(df.duplicated().sum())

# Calculate total sales per branch
branch_sales = df.groupby('Branch')['Total'].sum()
plt.figure(figsize=(4, 2)) #Sets width=6 and height=4 (inches)
branch_sales.plot(kind='bar', color=['red', 'blue', 'green'])
plt.title("Total Sales by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.show()

# Count the number of sales per product category
product_counts = df["Product line"].value_counts()

plt.figure(figsize=(4,2))
product_counts.plot(kind="bar", color="purple")
plt.title("Most Sold Product Categories")
plt.xlabel("Product Line")
plt.ylabel("Number of Sales")
plt.xticks(rotation=0)
plt.show()

#Best-Selling Payment Method
payment_counts = df["Payment"].value_counts()
plt.figure(figsize=(4,2))
payment_counts.plot(kind="bar", color = "orange")
plt.title("Most Used Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=0)
plt.show()

#Sales Over Time
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
daily_sales = df.groupby("Date")["Total"].sum() # Sum of total sales per day
plt.figure(figsize=(5,3))
daily_sales.plot(marker="o", color="blue")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid()
plt.show()
