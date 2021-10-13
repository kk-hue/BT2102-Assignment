SELECT * FROM oshes.item;

UPDATE item
SET purchaseStatus = 'Sold'
WHERE purchaseStatus = ( 
   SELECT purchaseStatus WHERE purchaseStatus = 'Unsold' AND color = 'White' AND powerSupply = 'Battery' AND productID = '001'
   ORDER BY itemID DESC LIMIT 1);

SELECT * FROM item
ORDER BY itemID DESC LIMIT 3;    