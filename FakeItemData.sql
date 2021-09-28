DELETE FROM item 
WHERE itemID = 2002
	AND EXISTS (SELECT temp.itemID FROM (SELECT itemID FROM item WHERE itemID = 2002) temp);
DELETE FROM item 
WHERE itemID = 2003
	AND EXISTS (SELECT temp.itemID FROM (SELECT itemID FROM item WHERE itemID = 2003) temp);
DELETE FROM item 
WHERE itemID = 2004
	AND EXISTS (SELECT temp.itemID FROM (SELECT itemID FROM item WHERE itemID = 2004) temp);
INSERT INTO item (itemid, productid, adminid, customerid, purchasestatus, servicestatus, dateofpurchase) 
values (2002, 7, NULL, 1, 'Sold', '', '2020-09-28');
INSERT INTO item (itemid, productid, adminid, customerid, purchasestatus, servicestatus, dateofpurchase) 
values (2003, 7, NULL, 1, 'Sold', '', '2020-09-28');
INSERT INTO item (itemid, productid, adminid, customerid, purchasestatus, servicestatus, dateofpurchase) 
values (2004, 7, NULL, 1, 'Sold', '', '2020-09-28');