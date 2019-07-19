# My Answer
'''
Runtime: 316 ms, faster than 51.82% of MySQL online submissions for Employees Earning More Than Their Managers.
Memory Usage: N/A
'''
SELECT A.Name AS Employee FROM Employee AS A
LEFT JOIN Employee AS B ON A.ManagerId=B.Id
WHERE A.Salary > B.Salary