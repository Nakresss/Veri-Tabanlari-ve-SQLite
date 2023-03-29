# Manuel Tablo Oluşturma İşlemleri
CREATE TABLE yeni_tablo(firstname varchar(20),
                       lastname varchar(20)); 
INSERT INTO yeni_tablo values('Ali', 'Uzaya_Git')
SELECT * FROM yeni_tablo
INSERT INTO yeni_tablo values('Işık', 'Süte_Devam')
SELECT * FROM yeni_tablo

# SELECT İşlemleri
SELECT * FROM Products LIMIT 5
SELECT name FROM sqlite_master WHERE type = 'table'
SELECT * FROM Customers where 1=0
SELECT * FROM Customers LIMIT 3
SELECT CustomerName, City, Country FROM Customers LIMIT 5
SELECT * from Products LIMIT 3

#matemattiksel islemler
SELECT Price, Price*3, Price*3-100 from Products LIMIT 3

#alias: takma isim, kısayol
SELECT Price AS ilk_price, Price*3 AS yeni_price, Price*3-100 AS islemli_price from Products LIMIT 3

#count
SELECT COUNT(*) AS satir_sayisi FROM Customers

#order by
SELECT * from Products LIMIT 3
SELECT * from Products ORDER BY Price DESC LIMIT 10

# WHERE
SELECT * FROM Customers LIMIT 10

#text string seçim
SELECT * FROM Customers WHERE Country = 'Sweden'
SELECT * FROM Customers WHERE NOT City = 'Berlin' LIMIT 10

#numerik/sayisal seçim
SELECT * FROM Customers WHERE PostalCode = 5021
SELECT * FROM Customers WHERE PostalCode > 5021

#and ve or ifadeleri
SELECT * FROM Customers WHERE Country = 'UK' AND City = 'London'
SELECT * FROM Customers WHERE Country = 'UK' OR Country = 'USA'
SELECT * FROM Customers WHERE Country = 'USA' AND (City = 'Eugene' OR City = 'Elgin')
SELECT * FROM Customers WHERE Country = 'USA' AND PostalCode = 97403 AND (City = 'Eugene' OR City = 'Elgin')

#in / not in kullanımı
SELECT * FROM Customers WHERE CustomerID in (1,3,5,7)
SELECT * FROM Customers WHERE Country = 'USA' AND City IN ('Eugene','Elgin')
SELECT * FROM Customers WHERE CustomerID NOT IN (1,3,5,7)
SELECT * FROM Customers WHERE Country = 'USA' AND City NOT IN ('Eugene','Elgin')

# LIKE ile Seçim işlemleri
* 'a%' : “a” ile başlayan değerler
* '%a' : “a” ile biten değerler
* %or%' : herhangi bir yerinde “or” olan değerler
* '_r%' : ikinci sirasında “r” olan değerler
* 'a%%' : “a” ile başlayıp en az 3 karakterden oluşan değerler
* 'a%o' : “a” ile başlayıp “o” ile biten değerler

SELECT * FROM Customers LIMIT 10
SELECT * FROM Customers WHERE CustomerName LIKE '%or%'LIMIT 10
SELECT * FROM Customers WHERE CustomerName LIKE '%a'LIMIT 10
SELECT * FROM Customers WHERE CustomerName LIKE 'A%' AND Country LIKE '%o'

# BETWEEN
SELECT * FROM Products LIMIT 10
SELECT * FROM Products WHERE Price NOT BETWEEN 10 AND 20 LIMIT 10
SELECT * FROM Products WHERE (Price BETWEEN 10 AND 20) AND NOT CategoryID IN (1,2,3) LIMIT 10
SELECT ProductName FROM Products WHERE (Price BETWEEN 10 AND 20) AND NOT CategoryID IN (1,2,3) LIMIT 10
SELECT * FROM Products WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Govanni'

# Aggregation Fonksiyonları: Temel İstatistiksel İşlemler
SELECT * FROM Products LIMIT 10
SELECT MIN(Price) FROM Products
SELECT MAX(Price) FROM Products
SELECT MIN(Price) AS min_fiyat, MAX(Price) AS max_fiyat FROM Products
SELECT AVG(Price) FROM Products
SELECT SUM(Price) FROM Products
SELECT COUNT(Price), MIN(Price), MAX(Price), AVG(Price), SUM(Price) FROM Products

# GROUP BY ve Aggregation Fonksiyonları
SELECT * FROM Customers LIMIT 3
SELECT COUNT(CustomerID) AS MUSTERI_SAYISI, Country FROM Customers GROUP BY Country ORDER BY MUSTERI_SAYISI DESC
SELECT * FROM Products LIMIT 2
SELECT AVG(Price) AS ORT_FIYAT, CategoryID FROM Products GROUP BY CategoryID

# JOIN İşlemleri
SELECT name FROM sqlite_master WHERE type='table'
SELECT * FROM Categories LIMIT 3
SELECT * FROM Products LIMIT 3

#left join
SELECT * FROM Products LEFT OUTER JOIN Categories ON Products.CategoryID = Categories.CategoryID LIMIT 5
SELECT PR.ProductName, CA.CategoryID, CA.CategoryName FROM Products AS PR LEFT OUTER JOIN Categories AS CA ON PR.CategoryID = CA.CategoryID LIMIT 5
SELECT PR.ProductName, CA.CategoryID, CA.CategoryName FROM Products PR LEFT OUTER JOIN Categories CA ON PR.CategoryID = CA.CategoryID LIMIT 5

#inner join
SELECT * FROM Customers LIMIT 3
SELECT * FROM Orders LIMIT 3
SELECT Orders.OrderID, Customers.CustomerName FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
SELECT COUNT(*) FROM (SELECT Orders.OrderID, Customers.CustomerName FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)


# SQL ve Pandas DataFrame Operasyonları
import pandas as pd
%load_ext sql

%sql SELECT COUNT(CustomerID) AS MUSTERI_SAYISI, Country FROM Customers GROUP BY Country ORDER BY MUSTERI_SAYISI DESC
df = %sql SELECT COUNT(CustomerID) AS MUSTERI_SAYISI, Country FROM Customers GROUP BY Country ORDER BY MUSTERI_SAYISI DESC
df
df.head()
type(df)

dff = pd.DataFrame(df, columns = ["MUS_SAY","ULKE"])
dff.head()

dff.plot.barh(x = "ULKE", y = "MUS_SAY")

# sqlite3
import sqlite3
conn = sqlite3.connect('database yazın')
c = conn.cursor()
pd.read_sql

#read_sql
pd.read_sql("SELECT COUNT(CustomerID) AS MUSTERI_SAYISI, Country FROM Customers GROUP BY Country;", conn)
pd.read_sql("""SELECT COUNT(CustomerID) AS MUSTERI_SAYISI, Country FROM Customers GROUP BY Country;""", conn)
ab = pd.read_sql("""SELECT COUNT(CustomerID) AS MUSTERI_SAYISI, Country FROM Customers GROUP BY Country;""", conn)

type(ab)

#conn.close()

c.execute("SELECT CustomerName FROM Customers LIMIT 5;")
c.fetchone()
c.fetchall()

for row in c.execute('SELECT CustomerName FROM Customers LIMIT 5;'):
                     print(row)
conn.close()

# SQL ALIŞTIRMALARI 1
SELECT * FROM Customers LIMIT 3

# 1. Orders tablosunda kaç müşteri oldugunu bulunuz.
## 2. Orders tablosunda kaç tane eşsiz müşteri olduğunu bulunuz.
## 3. Customers tablosunda hangi ülkeden kaçar tane müşteri olduğunu bulunuz.
## 4. Müşterilerin ülkesi Brazil ya da USA olanlarını bulunuz.
## 5. Önce ülkeye sonra şehre göre group by işlemi yapıp bu kırılımda müşteri sayısını bulunuz.

# SQL ALIŞTIRMALARI II
## 6. Müşterileri adreslerinin herhangi bir yerinde "da" ifadesi geçen tüm adresleri bulunuz.
## 7. Germany-Berlin'de yaşayan müşteri/müşterilerin isimleri nelerdir?
## 8. Canada'da yaşayıp isimlerinde "in" ifadesi geçen müşteri/müşterileri bulunuz.
## 9. Fiyatı 40 TL ile 90 TL arasında olan ürünlerin isimleri ve fiyatları nelerdir?
## 10. Fiyatı 30 TL'den büyük olan ürünlerin isimlerini, fiyatlarini ve fiyatlarinin karesini bulunuz ve tüm değişkenlerin isimlendirmelerini aşağıdaki şekilde yapınız:
#urun ismi, urun_fiyati, ürün_fiyatinin_karesi

# SQL ALIŞTIRMALARI III
## 11. Products tablosundaki CategoryID’lerin yani kategorilerin isimleri nelerdir? 
## 12. beverages ürün kategorisindeki ürünlerin fiyat ortalaması nedir?
## 13. USA'de yaşayan müşterilerin kazandırdığı toplam kazancı bulunuz.
## 14. Products tablosundaki CategoryID'lerin isimlerini bulunuz ve sonrasında kategori başına ortalama ürün fiyatını gösteriniz.
## 15. Çalışanları (EmployeeID) isimleri ile birlikte yaptıkları toplam satışlara göre sıralayınız.

# SQL ALIŞTIRMALARI IV
## 16. Germany'dan verilen siparişlerin kategorilerine göre ortalama fiyatları nelerdir?
## 17. Almanya ya da USA'den verilen siparişlerin kategorilerine göre ortalama fiyatları nelerdir?
## 18. Haziran Temmuz Ağustos aylarında verilen siparişlerin ortalama fiyatı nedir?
## 19. Müşterilerin 1997 yılına ait siparişlerinin maksimum miktarlarını bulup müşterilerin isimleri ile birlikte büyükten küçüğe sıralayınız.
## 20. Sipariş yılı 1997 olan siparişleri alan çalışanları sipariş alma sayılarına göre sıralayınız.
















