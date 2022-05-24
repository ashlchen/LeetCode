
select product_id, store, price
from (
select product_id,'store1' as store, store1 as price
from Products
union all
select product_id,'store2' as store, store2 as price
from Products
union all
select product_id,'store3' as store, store3 as price
from Products) sub
where price IS NOT NULL

-- Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

--Return the result table in any order.