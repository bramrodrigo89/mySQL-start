import os
import datetime
import pymysql

# Get username
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    # In order to retrieve information in Dictionary format, use:
    # with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    with connection.cursor() as cursor:
        """Create tables like this"""
        #cursor.execute("""CREATE TABLE IF NOT EXISTS
        #                    Friends(name char(20), age int, DOB datetime);""")
        # The above will still display a warning (not error) if the table already exists
        """Insert rows of data into tables like this"""
        row = ("Bob", 21, "1990-02-06 23:06:04")
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Jim", 56, "1955-05-09 13:12:45"),
                ("Fred", 100, "1911-09-12 01:01:01")]
        names_list_delete = ['Fred','Bob']
        update_rows= [(23, 'Bob'),(25, 'Jim'),(26, 'Fred')]
        # When only adding one row to the table use "execute"
        # cursor.execute("INSERT INTO Friends VALUES(%s,%s,%s);",row)
        
        # When adding multiple rows to table use "executemany"
        # cursor.executemany("INSERT INTO Friends VALUES(%s,%s,%s);",rows)

        # In order to update a specific row use "UPDATE"
        # cursor.execute("UPDATE Friends SET age = %s where name = %s;",(23,'Bob'))
        
        # In order to update several rows at the same time
        # cursor.executemany("UPDATE Friends SET age = %s where name = %s;",update_rows)

        # In order to delete an entry from the table
        # cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")

        # Or using DELETE Alternate with String Interpolation
        # cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Bob')

        # DELETE many is also possible using executemany
        # cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob','Jim'])

        #DELETE and WHERE IN 
        #Prepare list with same numer of placeholders as name_list_delete
        format_strings =  ','.join(['%s']*len(names_list_delete))
        cursor.execute("DELETE FROM Friends WHERE name IN ({0});".format(format_strings),names_list_delete)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()