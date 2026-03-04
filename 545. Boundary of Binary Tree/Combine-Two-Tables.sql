1# Write your MySQL query statement below
2
3select FirstName, LastName, City, State
4from Person left join Address
5on Person.PersonId = Address.PersonId;