# My Answer
'''
Runtime: 194 ms, faster than 72.45% of MySQL online submissions for Duplicate Emails.
Memory Usage: N/A
'''
SELECT Email FROM Person
GROUP BY Email
HAVING COUNT(*) > 1