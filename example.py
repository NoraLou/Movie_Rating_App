import sqlite3, unicodecsv


# Write a python script to load the data from the CSV files and INSERT it into your database


def main():

    #Connect to database file (Note: can also pass as a file using sys)
    CONN = sqlite3.connect('melon.db')

    #This cursor object passes commands from python and executes them in the sqlite3 melon.db
    DB = CONN.cursor()

    #Deletes tables if they exist. Good if I made a mistake creating them.
    DB.execute('''DROP TABLE IF EXISTS Customers;''')
    DB.execute('''DROP TABLE IF EXISTS Orders;''')

    #Create 2 tables of Customers & Orders
    DB.execute('''CREATE TABLE Customers (customer_id INTEGER PRIMARY KEY NOT NULL, first varchar(30), last varchar(30), email varchar(60), telephone varchar(30), called DATE);''')

    #Note: Foreign key & Reference needs to be stated at the end of the create table dialog.
    DB.execute('''CREATE TABLE Orders (order_id INTEGER PRIMARY KEY NOT NULL, order_date DATE,status varchar(30), customer_id INTEGER,email varchar(60),address varchar(30),city varchar(30),state varchar(30),postalcode varchar(30),num_watermelons INTEGER,num_othermelons INTEGER ,subtotal INTEGER ,tax INTEGER ,order_total INTEGER, FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)); ''')


    #CSV reader reads each line and strips, splits each line into a list object. :)

    f1reader = unicodecsv.reader(open('customers.csv'), encoding='utf-8')
    f2reader = unicodecsv.reader(open('orders.csv'), encoding='utf-8')

    
    #Next skips collumn names // headers of csv file

    next(f1reader)
    next(f2reader)

# Text formatting in file (nyee '~' & special charecters) cannot be interpreted by sqlite. Need to import unicode csv module to parse code.

#Note: There are some shity looking customer files with strange charecters. What up with dat? Can they be flagged and edited later on? (eg., like editing student records) 


    for row in f1reader:

        DB.executemany('''INSERT INTO customers (customer_id, first, last, email, telephone, called) VALUES(?, ?, ?, ?, ?, ?);''', (row, ))

    for row2 in f2reader:

        DB.executemany('''INSERT INTO orders (order_id, order_date, status, customer_id, email, address, city, state, postalcode, num_watermelons, num_othermelons, subtotal, tax, order_total) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (row2, ))

        #Change empty string row values to Null.
        # DB.executemany('''UPDATE orders SET VALUES 
        #   ''')



    
    CONN.commit()
    CONN.close()
    


if __name__ == '__main__':
    main()