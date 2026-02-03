CREATE OR REPLACE VIEW revenue_daily AS
SELECT
    o.order_date,
    SUM(oi.total_price) AS daily_revenue
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
WHERE o.valid_status = TRUE
GROUP BY o.order_date
ORDER BY o.order_date;


CREATE OR REPLACE VIEW revenue_by_seller AS
SELECT
    s.seller_id,
    s.seller_name,
    SUM(oi.total_price) AS seller_revenue,
    SUM(oi.total_price * s.commission_rate) AS commission_paid
FROM order_items oi
JOIN sellers s
    ON oi.seller_id = s.seller_id
GROUP BY s.seller_id, s.seller_name
ORDER BY seller_revenue DESC;
