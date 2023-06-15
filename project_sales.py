import csv

import pandas
# read the data from the csv file
def read_file():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

read_file()

# run data to get a summary of annual results
def get_yearly_results():
    data = read_file()

    sales = []
    expenditure = []

    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
        expenditure_out = int(row['expenditure'])
        expenditure.append(expenditure_out)

    total_sales = sum(sales)
    total_expenditure = sum(expenditure)
    total_profit = total_sales - total_expenditure

    print(f"Total sales for year: £{total_sales}\n")
    print(f"Total expenditure for year: £{total_expenditure}\n")
    print(f"Total profit for year: £{total_profit}\n")

    # output summary to a csv file

    field_names = ['description', 'amount']

    data = [
        {'description': 'Total sales for year', 'amount': 'total_sales'},
        {'description': 'Total expenditure for year', 'amount': 'total_expenditure'},
        {'description': 'Total profit for year', 'amount': 'total_profit'},
    ]

    with open('summary.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

        spreadsheet.writeheader()
        spreadsheet.writerows(data)

get_yearly_results()

# get name of month with lowest sales and sales amount
def lowest_month():
    data = read_file()

    df = pandas.read_csv('sales.csv')
    min = int(df['sales'].min())

    for row in data:
        if(int(row['sales']) == min):
            low_month = (row['month'])

    print(f"Month with lowest sales: {low_month} £{min}\n")

lowest_month()

def highest_month():
    data = read_file()

    df = pandas.read_csv('sales.csv')
    max = int(df['sales'].max())

    for row in data:
        if(int(row['sales']) == max):
            high_month = (row['month'])
    print(f"Month with highest sales: {high_month} £{max}\n")

highest_month()

# annual average of sales

def annual_average_sales():
    data = read_file()
    sales = []
    counter = 0

    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
        counter = counter + 1

    total_sales = sum(sales)

    average_sales = round(total_sales/counter,2)

    print(f"Average sales for the year: £{average_sales}\n")

annual_average_sales()


def mean_annual_sales():
    data = read_file()

    df = pandas.read_csv('sales.csv')
    mean = round(df['sales'].mean(), 2)

    print(f"Mean annual sales for the year: £{mean}\n")

mean_annual_sales()

def percentage_change():
    data = read_file()
# list of months to chose from that match csv rows

    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun' 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# user input for months to compare
    print('Pick the months to calculate percentage change')

    month_1 = input('First month to compare: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec ')
    while month_1 not in months:
            month_1 = input('Try again, input the first 3 letters of the first month ')

    month_2 = input('Second month to compare: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec ')
    while month_2 not in months:
            month_2 = input('Try again, input the first 3 letters of the second month ')

    for row in data:
        if row['month'] == month_1:
            month_1_value = int(row['sales'])
        if row['month'] == month_2:
            month_2_value = int(row['sales'])

 # calculate the percentage difference between the two months
    if month_1_value > month_2_value:
        percent_change = ((month_1_value - month_2_value)/ month_1_value)*100
        print(f"There was a {percent_change} % decrease between {month_1} and {month_2}\n")
    elif month_1_value < month_2_value:
        percent_change = ((month_2_value - month_1_value) / month_1_value)*100
        print(f"There was a {percent_change} % increase between {month_1} and {month_2}\n")
    else:
        print(f"There as no difference between {month_1} and {month_2}\n")

percentage_change()

# user chooses month to view
def choose_monthly_data():
     data = read_file()
     months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun' 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

     choose_month = input('Which month figures do you want to display: jan, feb, mar, apr, jun, jul, aug, sep, oct, nov, dec ')

     for row in data:
         if row ['month'] == choose_month:
             sales_month = int(row['sales'])
             expenditure_month = int(row['expenditure'])
             profit_month = sales_month - expenditure_month
             print(f"For {choose_month} sales £{sales_month}, expenditure £{expenditure_month}, profit £{profit_month}")

choose_monthly_data()