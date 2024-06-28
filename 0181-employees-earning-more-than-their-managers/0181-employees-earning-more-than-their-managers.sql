# Write your MySQL query statement below
# select name from employee  where managerId is not null group by name having max(salary) < (select max(salary) from employee where managerId is  null);

-- select table1.name as employee from Employee as table1 join Employee as table2 on 
-- table1.mangerId = table2.Id where table1.salary >table2.salary; 
SELECT e2.name as Employee
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE
e1.salary < e2.salary

# SELECT tb1.Name as Employee
# FROM Employee as tb1
# LEFT JOIN Employee as tb2
# ON tb1.ManagerId = tb2.Id
# WHERE tb1.Salary > tb2.Salary ;