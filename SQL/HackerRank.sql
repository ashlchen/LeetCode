-- Binary Tree Node
SELECT CASE
    WHEN P IS NULL THEN CONCAT(N, ' Root')
    WHEN N IN (SELECT P FROM BST) THEN CONCAT(N, ' Inner')
    ELSE CONCAT(N, ' Leaf') END
FROM BST
ORDER BY N ASC;

-- Pivot Table
set @r1=0, @r2=0, @r3=0, @r4=0;
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
  select case when Occupation='Doctor' then (@r1:=@r1+1)
            when Occupation='Professor' then (@r2:=@r2+1)
            when Occupation='Singer' then (@r3:=@r3+1)
            when Occupation='Actor' then (@r4:=@r4+1) end as RowNumber,
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  from OCCUPATIONS
  order by Name
	) temp
group by RowNumber;

-- advanced select from multiple table
select company_code, founder, 
    (select count(distinct lead_manager_code) from Lead_Manager where company_code = c.company_code),
    (select count(distinct senior_manager_code) from Senior_Manager where company_code = c.company_code),
    (select count(distinct manager_code) from Manager where company_code = c.company_code),
    (select count(distinct employee_code) from Employee where company_code = c.company_code)
from Company c
group by company_code, founder
order by company_code

-- Project planning
select Start_Date, min(End_Date)
from (select Start_Date from Projects where Start_Date not in (
        select End_Date from Projects)) t1, 
    (select End_Date from Projects where End_Date not in (
        select Start_Date from Projects)) t2
where Start_Date < End_Date
group by Start_Date
order by datediff(min(End_Date), Start_Date) ASC, Start_Date


-- Compare Salary
select s.Name
from Students s, Friends f, Packages p, 
    (select f.ID, Friend_ID, Salary from Friends f, Packages p where f.Friend_ID = p.ID) t1
where s.ID = f.ID and s.ID = p.ID and 
    t1.ID = s.ID and 
    t1.Salary > p.Salary
order by t1.Salary

-- Symmetric pairs
select f1.X, f1.Y
from Functions f1 INNER JOIN Functions f2
on f1.X = f2.Y and f1.Y = f2.X
group by f1.X, f1.Y
having count(f1.X) > 1 or f1.X < f1.Y
order by f1.X

-- left join because there might be null value in View_Stats and Submission_Stats
select c1.contest_id, c3.hacker_id, c3.name, sum(total_sub), sum(total_accepted_sub), sum(total_views), sum(total_unique_views)
from Colleges c1 
    join Challenges c2 on c1.college_id = c2.college_id
    join Contests c3 on c1.contest_id = c3.contest_id
    left join (select challenge_id, sum(total_views) as total_views, sum(total_unique_views) as total_unique_views
              from View_Stats 
              group by challenge_id) v on c2.challenge_id = v.challenge_id
    left join (select challenge_id, sum(total_submissions) as total_sub, sum(total_accepted_submissions) as total_accepted_sub
              from Submission_Stats 
              group by challenge_id) s on c2.challenge_id = s.challenge_id
group by c1.contest_id, c3.hacker_id, c3.name
having (sum(total_views) + sum(total_unique_views) + sum(total_sub) + sum(total_accepted_sub) != 0)
order by c1.contest_id


-- row number
set @row_number := 0;

SELECT 
    @row_number:=CASE
        WHEN @customer_no = customerNumber 
			THEN @row_number + 1
        ELSE 1
    END AS num,
    @customer_no:=customerNumber customerNumber,
    paymentDate,
    amount
FROM
    payments
ORDER BY customerNumber;


-- rank
WITH order_values AS(
    SELECT 
        orderNumber, 
        YEAR(orderDate) order_year,
        quantityOrdered*priceEach AS order_value,
        RANK() OVER (
            PARTITION BY YEAR(orderDate)
            ORDER BY quantityOrdered*priceEach DESC
        ) order_value_rank
    FROM
        orders
    INNER JOIN orderDetails USING (orderNumber)
)
SELECT 
    * 
FROM 
    order_values
WHERE 
    order_value_rank <=3;