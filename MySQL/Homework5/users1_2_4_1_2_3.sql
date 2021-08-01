#1.Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем 
update shop.users set created_at = NOW(), updated_at = now();
SELECT * FROM shop.users;

#2.Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате 20.10.2017 8:10. Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.
#Преобразовал даты к некорректным в воркбенче
ALTER TABLE shop.users ADD COLUMN created_at_new DATETIME,
ADD COLUMN updated_at_new DATETIME after updated_at;
UPDATE shop.users
SET created_at_new = STR_TO_DATE(created_at, '%d.%m.%Y %h:%i'),
    updated_at_new = STR_TO_DATE(updated_at, '%d.%m.%Y %h:%i');
ALTER TABLE shop.users 
DROP created_at, DROP updated_at, 
RENAME COLUMN created_at_new TO created_at, RENAME COLUMN updated_at_new TO updated_at;
SELECT * FROM shop.users;
#2.1.Подсчитайте средний возраст пользователей в таблице users.
SELECT id,name, avg (YEAR(CURDATE())-YEAR(birthday_at)) as sredniy 
from shop_hw.users
GROUP BY name with rollup;
#2.2.Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.
SELECT
    DAYNAME(CONCAT(YEAR(NOW()), '-', SUBSTRING(birthday_at, 6, 10))) AS day_of_the_week,
    COUNT(*) AS summ from shop_hw.users group by day_of_the_week;
#2.3 Подсчитайте произведение чисел в столбце таблицы.

SELECT round((exp(sum(ln(id))))) as proizvedenie from shop_hw.users;