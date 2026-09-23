+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+


Courses =
| student | class    |
| ------- | -------- |
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |

Write a solution to find all the classes that have at least five students.

Return the result table in any order.

The result format is in the following example.

#-------------------------------------------------------------

Solution:

-- Write your PostgreSQL query statement below
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(student) >= 5

#-------------------------------------------------------------

OUTPUT:

| class |
| ----- |
| Math  |