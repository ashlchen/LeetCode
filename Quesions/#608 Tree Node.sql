select distinct t1.id, 
case
when t1.p_id is null then "Root"
when t2.p_id is Null then "Leaf"
else "Inner"
end as type
from Tree t1
left join Tree t2
on t1.id = t2.p_id
order by t1.id
-- Each node in the tree can be one of three types:

--"Leaf": if the node is a leaf node.
--"Root": if the node is the root of the tree.
--"Inner": If the node is neither a leaf node nor a root node.