# Display snum, sname, city and comm of all salespeople.
SELECT * FROM salespeople;

# Display all snum without duplicates from all orders.
SELECT DISTINCT snum FROM orders;

# Display names and commissions of all salespeople in london.
SELECT sname, comm FROM salespeople WHERE city = 'London';

# All customers with rating of 100.
SELECT cname FROM cust WHERE rating = 100;

# Produce orderno, amount and date form all rows in the order table.
SELECT onum, amt, odate FROM orders;

# All customers in San Jose, who have rating more than 200.
SELECT cname FROM cust WHERE city = 'San Jose' AND rating > 200;

# All customers who were either located in San Jose or had a rating above 200.
SELECT cname FROM cust WHERE city = 'San Jose' OR rating > 200;

# All orders for more than $1000.
SELECT * FROM orders WHERE amt > 1000;

# Names and cities of all salespeople in london with commission above 0.10.
SELECT sname, city FROM salespeople WHERE city = 'London' AND comm > .1;

# All customers excluding those with rating <= 100 unless they are located in Rome.
SELECT cname FROM cust WHERE rating > 100 OR city = 'Rome';

# All salespeople either in Barcelona or in london.
SELECT sname, city FROM salespeople WHERE city IN ('Barcelona', 'London');

# All salespeople with commission between 0.10 and 0.12. (Boundary values should be excluded)
SELECT sname, comm FROM salespeople WHERE comm > .1 AND comm < .12;  # "comm BETWEEN .1 AND .12" included both values

# All customers with NULL values in city column.
SELECT cname FROM cust WHERE city IS NULL;  # https://stackoverflow.com/questions/2749044/whats-the-difference-between-null-and-is-null

# All orders taken on Oct 3rd and Oct 4th 1994.
SELECT * FROM orders WHERE odate IN ('1994-10-03', '1994-10-04');

# All customers serviced by Peel or Motika.
SELECT cname FROM cust WHERE snum IN (SELECT snum FROM salespeople WHERE sname IN ('Peel', 'Motika'));

# All customers whose names begin with a letter from A to B.
SELECT cname FROM cust WHERE cname LIKE 'A%' OR cname LIKE 'B%';

# All orders except those with 0 or NULL value in amt field.
SELECT * FROM orders WHERE amt != 0 AND amt IS NOT NULL;

# Count the number of salespeople currently listing orders in the order table.
SELECT count(DISTINCT snum) FROM orders;

# Largest order taken by each salesperson, datewise.
# 1) Shows salesperson number:
SELECT snum, max(amt), odate 
FROM orders 
GROUP BY snum 
ORDER BY odate;
# 2) Shows salesperson name instead of number! (harder but worth it):
SELECT sname, max(amt), odate 
FROM salespeople s INNER JOIN orders o 
ON s.snum = o.snum 
GROUP BY o.snum  # coz 'snum' is in both the tables
ORDER BY odate;

# Largest order taken by each salesperson with order value more than $3000.
# 1) Shows salesperson number:
SELECT snum, max(amt) 
FROM orders 
WHERE amt > 3000 
GROUP BY snum;
# 2) Shows salesperson name instead of number! (harder but worth it):
SELECT sname, max(amt) 
FROM salespeople s INNER JOIN orders o 
ON s.snum = o.snum 
WHERE amt > 3000 
GROUP BY o.snum;  # coz 'snum' is in both the tables

# Which day had the hightest total amount ordered.
SELECT odate, amt FROM orders WHERE amt = (SELECT max(amt) FROM orders);  # ❌
SELECT odate, sum(amt) FROM orders GROUP BY odate ORDER BY sum(amt) DESC LIMIT 1;  # ✔️

# Count all orders for Oct 3rd.
SELECT count(*) FROM orders WHERE odate = '1994-10-03';

# Count the number of different non NULL city values in customers table.
SELECT count(DISTINCT city) FROM cust;

# Select each customer’s smallest order.
SELECT cnum, onum, min(amt) FROM orders GROUP BY cnum;

# First customer in alphabetical order whose name begins with G.
SELECT cname FROM cust WHERE cname LIKE 'G%' ORDER BY cname LIMIT 1;
# or
SELECT min(cname) FROM cust WHERE cname LIKE 'G%';

# Get the output like "For dd/mm/yy there are _ orders".
SELECT 'For', date_format(odate, '%d/%m/%y') as 'dd/mm/yy', 'there are', count(*), 'orders' FROM orders GROUP BY odate;  # https://www.w3schools.com/sql/func_mysql_date_format.asp

# Assume that each salesperson has a 12% commission. Produce order no., salesperson no., and amount of salesperson’s commission for that order.
SELECT onum, snum, amt*.12 FROM orders;

# Find highest rating in each city. Put the output in this form. For the city (city), the highest rating is: (rating).
SELECT 'For the city', city, 'the highest rating is:', max(rating) FROM cust GROUP BY city;

# Display the totals of orders for each day and place the results in descending order.
SELECT sum(amt), odate FROM orders GROUP BY odate ORDER BY sum(amt) DESC;
# or 
SELECT count(*), odate FROM orders GROUP BY odate ORDER BY count(*) DESC;
# whatever the questioner meant

# All combinations of salespeople and customers who shared a city. (ie same city)
SELECT sname, cname FROM salespeople JOIN cust ON salespeople.city = cust.city;  # JOIN by default is INNER JOIN
# or
Select sname, cname FROM salespeople, cust WHERE salespeople.city = cust.city; 

# Name of all customers matched with the salespeople serving them.
SELECT cname, sname FROM cust, salespeople WHERE cust.snum = salespeople.snum;

# List each order number followed by the name of the customer who made the order.
SELECT onum, cname FROM orders, cust WHERE orders.cnum = cust.cnum;

# Names of salesperson and customer for each order after the order number.
SELECT onum, sname, cname FROM orders, salespeople, cust WHERE orders.snum = salespeople.snum AND orders.snum = cust.snum;

# Produce all customer serviced by salespeople with a commission above 12%.
SELECT cname FROM cust WHERE snum in (SELECT snum FROM salespeople WHERE comm > .12); 
# or
SELECT cname FROM cust, salespeople WHERE cust.snum = salespeople.snum AND comm > .12;

# Calculate the amount of the salesperson’s commission on each order with a rating above 100.
SELECT sname, amt*comm, onum FROM orders, salespeople, cust WHERE orders.snum = salespeople.snum AND orders.snum = cust.snum AND rating > 100;

# Find all pairs of customers having the same rating.
SELECT group_concat(cname), rating FROM cust GROUP BY rating;

# Policy is to assign three salesperson to each customers. Display all such combinations.
SELECT cname, sname FROM cust, salespeople;  # TODO
# result rows should be (5C3) * 6 = 10 * 6 = 60

# Display all customers located in cities where salesman serres has customer.
# Process:
SELECT snum FROM salespeople WHERE sname = 'Serres';
SELECT city FROM cust WHERE snum = (SELECT snum FROM salespeople WHERE sname = 'Serres');
SELECT * FROM cust WHERE city IN (SELECT city FROM cust WHERE snum = (SELECT snum FROM salespeople WHERE sname = 'Serres'));  # Result

# Find all pairs of customers served by single salesperson.
SELECT group_concat(cname), snum FROM cust GROUP BY snum;

# Produce all pairs of salespeople which are living in the same city. Exclude combinations of salespeople with themselves as well as duplicates with the order reversed.
SELECT group_concat(sname), city FROM salespeople GROUP BY city;

# Produce names and cities of all customers with the same rating as Hoffman.
SELECT cname, city FROM cust WHERE rating = (SELECT rating FROM cust WHERE cname = 'Hoffman') AND cname != 'Hoffman';

# Extract all the orders of Motika.
SELECT * FROM orders WHERE snum = (SELECT snum FROM salespeople WHERE sname = 'Motika');

# All orders credited to the same salesperson who services Hoffman.
SELECT * FROM orders WHERE snum = (SELECT snum FROM cust WHERE cname = 'Hoffman');

# All orders that are greater than the average for Oct 4.
SELECT * FROM orders WHERE amt > (SELECT avg(amt) FROM orders WHERE odate = '1994-10-04');

# Find average commission of salespeople in london.
SELECT avg(comm) FROM salespeople WHERE city = 'London';

# Find all orders attributed to salespeople servicing customers in london.
SELECT * FROM orders WHERE snum IN (SELECT snum FROM cust WHERE city = 'LONDON');

# Extract commissions of all salespeople servicing customers in London.
SELECT comm FROM salespeople WHERE snum IN (SELECT snum FROM cust WHERE city = 'LONDON');

# Find all customers whose cnum is 1000 above the snum of serres.
SELECT * FROM cust WHERE cnum-1000 > (SELECT snum FROM salespeople WHERE sname = 'Serres');

# Count the customers with rating above San Jose’s average.
SELECT count(*) FROM cust WHERE rating > (SELECT avg(rating) FROM cust WHERE city = 'San Jose');
