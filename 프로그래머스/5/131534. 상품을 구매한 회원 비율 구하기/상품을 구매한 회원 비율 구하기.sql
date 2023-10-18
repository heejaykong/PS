
SELECT YEAR(os.sales_date) year, MONTH(os.sales_date) month, 
       COUNT(DISTINCT u.user_id) puchased_users,
       ROUND( COUNT(DISTINCT u.user_id) / (SELECT COUNT(DISTINCT user_id) FROM USER_INFO u WHERE YEAR(u.joined) = 2021), 1) puchased_ratio
FROM ONLINE_SALE os JOIN USER_INFO u ON os.user_id = u.user_id AND YEAR(u.joined) = 2021
GROUP BY 1, 2 
ORDER BY 1, 2;