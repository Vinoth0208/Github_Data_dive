import streamlit as st
import pandas as pd
import mysql.connector
def datamigration(topic):
    data=pd.read_csv(f'{topic}.csv')
    data.drop('Unnamed: 0', axis=1, inplace=True)

    myConnection = mysql.connector.connect(host="localhost", user="root", password="root")
    mycursor = myConnection.cursor()
    sqlQuery="CREATE DATABASE IF NOT EXISTS github_data_dive;"
    usequery="USE github_data_dive;"

    sqlQueryTables=['''CREATE TABLE IF NOT EXISTS Alldata(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''',
    '''CREATE TABLE IF NOT EXISTS Machine_Learning(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''',
    '''CREATE TABLE IF NOT EXISTS Web_Development(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''',
    '''CREATE TABLE IF NOT EXISTS Data_Science(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''',
    '''CREATE TABLE IF NOT EXISTS Blockchain(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''',
    '''CREATE TABLE IF NOT EXISTS DevOps(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''',
    '''CREATE TABLE IF NOT EXISTS Game_Development(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''',
    '''CREATE TABLE IF NOT EXISTS Cybersecurity(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''',
    '''CREATE TABLE IF NOT EXISTS IoT(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''',
    '''CREATE TABLE IF NOT EXISTS Mobile_Development(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''',
    '''CREATE TABLE IF NOT EXISTS Open_Source_Tools(id INT AUTO_INCREMENT PRIMARY KEY, Repository_Name VARCHAR(255),
    Owner VARCHAR(255), Description LONGTEXT, URL VARCHAR(255), Programming_Language VARCHAR(255),
    Creation_Date DATETIME, Last_Updated_Date DATETIME, Number_of_Stars INT, Number_of_Forks INT,
    Number_of_Open_Issues INT, License_Type VARCHAR(255), Repository_Age INT, Created_Year INT);''']


    tables={"All":"Alldata",
        "Machine Learning":"Machine_Learning",
        "Web Development":"Web_Development",
        "Data Science":"Data_Science",
        "Blockchain":"Blockchain",
        "DevOps":"DevOps",
        "Game Development":"Game_Development",
        "Cybersecurity":"Cybersecurity",
        "Internet of Things (IoT)":"IoT",
        "Mobile Development":"Mobile_Development",
        "Open Source Tools":"Open_Source_Tools"}

    table=tables[topic]
    datainsert= f"""insert into {table}(Repository_Name, Owner, Description, URL, Programming_Language,
    Creation_Date, Last_Updated_Date, Number_of_Stars, Number_of_Forks,
    Number_of_Open_Issues, License_Type, Repository_Age, Created_Year)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""


    for i in sqlQueryTables:
        try:
            myConnection = mysql.connector.connect(host="localhost", user="root", password="root")
            mycursor = myConnection.cursor()
            mycursor.execute(sqlQuery)
            mycursor.execute(usequery)
            mycursor.execute(i)
            myConnection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            mycursor.close()
            myConnection.close()

    def truncate_text(text, max_length=100):
        if len(str(text)) > max_length:
            return text[:max_length]
        return text

    rows_as_tuples = []
    for index, row in data.iterrows():
        row_tuple = tuple(row)
        row['Description']=truncate_text(row['Description'])
        rows_as_tuples.append(row_tuple)

    for data in range(len(rows_as_tuples)):
        myConnection = mysql.connector.connect(host="localhost", user="root", password="root")
        mycursor = myConnection.cursor()
        mycursor.execute(usequery)
        mycursor.execute(datainsert, rows_as_tuples[data])
        myConnection.commit()

    st.write(f":green[{table } Data Migrated Successfully]")

    mycursor.close()
    myConnection.close()