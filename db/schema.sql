-- -----------------------------------------------------
-- Cadets table
-- -----------------------------------------------------
CREATE TABLE cadets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    company VARCHAR(10) NOT NULL,
    class_year INTEGER NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------
-- Items table
-- -----------------------------------------------------
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    in_stock_qty INTEGER DEFAULT 0
);

-- -----------------------------------------------------
-- Orders table
-- -----------------------------------------------------
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    cadet_id INTEGER NOT NULL REFERENCES cadets(id),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------
-- Order Items table
-- -----------------------------------------------------
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(id),
    item_id INTEGER NOT NULL REFERENCES items(id),
    quantit
