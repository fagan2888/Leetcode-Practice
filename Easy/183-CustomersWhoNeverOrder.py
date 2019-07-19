# My Answer
'''
Runtime: 339 ms, faster than 7.14% of MySQL online submissions for Customers Who Never Order.
Memory Usage: N/A
'''
SELECT Name AS Customers FROM customers
WHERE Id not in (SELECT CustomerId FROM Orders)


# Solution
'''
Runtime: 227 ms, faster than 98.64% of MySQL online submissions for Customers Who Never Order.
Memory Usage: N/A

https://leetcode.com/problems/customers-who-never-order/discuss/336406/Mysql-Beats-99.94
'''
select Name as Customers from
Customers as a
left join
Orders as b
on a.Id = b.CustomerId
where b.CustomerId is null