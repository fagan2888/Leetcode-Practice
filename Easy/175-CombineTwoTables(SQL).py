# My Answer
'''
Runtime: 216 ms, faster than 77.36% of MySQL online submissions for Combine Two Tables.
Memory Usage: N/A
'''
SELECT A.FirstName, A.LastName, B.City, B.State
FROM Person AS A
LEFT JOIN Address AS B ON A.PersonId = B.PersonId