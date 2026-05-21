-- Write your PostgreSQL query statement below
with t as (select e1.name as name, e1.salary as esalary, e2.salary as e2salary from Employee e1  join Employee e2 on e1.managerID = e2.id)

select t.name as Employee from t where t.esalary > t.e2salary 