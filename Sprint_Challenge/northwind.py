#import statement
import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

#check table names
query = """SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;"""
curs.execute(query).fetchall()

#most expensive products
query = """SELECT ProductName FROM Product
ORDER BY UnitPrice DESC 
LIMIT 10;"""
print('Ten most expensive items by unitprice:', curs.execute(query).fetchall())

#age of hires
query = """SELECT SUM(HireDate - BirthDate) 
/ COUNT(*) FROM Employee;"""
print('Average age at hire:', curs.execute(query).fetchall()[0][0], 'years old')

#Who supplies the expensive items
query = """
SELECT ProductName, CompanyName
FROM Product
INNER JOIN Supplier
ON Product.SupplierId = Supplier.id
GROUP BY ProductName
ORDER BY UnitPrice DESC 
LIMIT 10;"""
print('The ten more expsenives items and their supplilers:',
      curs.execute(query).fetchall())

#What category at the most items?
query = """
SELECT CategoryName
FROM Product
INNER JOIN Category
ON Product.CategoryId = Category.id
GROUP BY CategoryName
ORDER BY count(*) DESC
LIMIT 1;"""
print('Largest category by unique products:',curs.execute(query).fetchall()[0][0])