DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS sellers;

CREATE TABLE sellers (
    seller_id VARCHAR PRIMARY KEY,
    seller_name VARCHAR,
    commission_rate NUMERIC(5,4),
    valid_commission BOOLEAN
);

CREATE TABLE orders (
    order_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR,
    order_date DATE,
    order_status VARCHAR,
    valid_status BOOLEAN,
    valid_order_date BOOLEAN
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id VARCHAR REFERENCES orders(order_id),
    seller_id VARCHAR REFERENCES sellers(seller_id),
    quantity INTEGER,
    unit_price NUMERIC(10,2),
    total_item_amount NUMERIC(12,2),
    valid_quantity BOOLEAN,
    validate_price BOOLEAN
);
