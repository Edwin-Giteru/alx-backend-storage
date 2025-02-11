-- a script that creates a trigger that decreases the quantity of an item after adding anew order

DROP TRIGGER IF EXISTS decrease_quantity;
DELIMITER $$

CREATE TRIGGER decrease_quantity
AFTER INSERT 
ON orders FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - New.number
	WHERE name = New.item_name;
END $$
DELIMITER ;
