# My Answer
'''
Wrong Answer
'''
SELECT Salary AS SecondHighestSalary
FROM Employee 
ORDER BY Salary DESC 
LIMIT 1 OFFSET 1


'''
Runtime: 119 ms, faster than 99.24% of MySQL online submissions for Second Highest Salary.
Memory Usage: N/A
'''
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary