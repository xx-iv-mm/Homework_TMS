# Exercise 1
drop table if exists sales;
drop table if exists books;
drop table if exists authors;

CREATE TABLE authors(
	id SERIAL PRIMARY KEY,
	first_name text,
	last_name text
);

CREATE TABLE books(
	id SERIAL PRIMARY KEY,
	title text,
	author_id int REFERENCES authors(id),
	publication_year int
);

CREATE TABLE sales(
	id SERIAL PRIMARY KEY,
	book_id int REFERENCES books(id),
	quantity int
);

INSERT INTO authors(first_name, last_name)
values
('Лео','Месси'),
('Луис','Суарес'),
('Жорди','Альба'),
('Ферран','Торрес'),
('Фил','Фоден');

INSERT INTO sales(book_id, quantity)
VALUES
(3, 13),
(1, 32),
(2, 39),
(4, 47),

INSERT INTO books (title, author_id, publication_year)
VALUES
('Barcelona',1, 2020),
('Football FIFA',3, 1932),
('REAL MADRID',2, 1989),
('Arcenal',4, 2007),
('Spartak'),
('PSG',1, 1999),

# Exercise 2

select a.first_name,
	a.last_name,
	b.title
from authors as a
INNER JOIN books as b ON a.id = b.author_id

select a.first_name,
	a.last_name,
	b.title
from authors as a
LEFT JOIN books as b ON a.id = b.author_id

select
	b.title,
	a.first_name,
	a.last_name,
	b.publication_year
from authors as a
RIGHT JOIN books as b ON a.id = b.author_id;

# Exercise 3

select a.first_name, a.last_name, b.title, s.quantity
from authors AS a
INNER JOIN books as b ON a.id = b.author_id
INNER JOIN sales as s ON b.author_id = s.book_id

select a.first_name, a.last_name, b.title, s.quantity
from authors AS a
LEFT JOIN books as b ON a.id = b.author_id



# Exercise 4

select a.first_name, a.last_name, sum(s.quantity)
from authors as a
inner join books as b on b.author_id = a.id
inner join sales as s on s.book_id = b.id
group by a.first_name, a.last_name

select a.first_name, a.last_name, sum(s.quantity)
from authors as a
left join books as b on b.author_id = a.id
left join sales as s on s.book_id = b.id
group by a.first_name, a.last_name

# Exercise 5

select first_name, last_name,
	(select sum(s.quantity) from sales as s
	 join books as b on b.author_id = a.id
	 where s.book_id = b.id
	) as max_sale
from authors as a
order by max_sale desc
limit 1;


select a.first_name, a.last_name, b.title, s.quantity from authors as a
inner join books as b on b.author_id = a.id
inner join sales as s on s.book_id = b.id
where s.quantity > (select avg(s.quantity) from sales as s)

select a.first_name, a.last_name, avg(s.quantity) from authors as a
inner join books as b on b.author_id = a.id
inner join sales as s on s.book_id = b.id
group by a.first_name, a.last_name
having avg(s.quantity) > (
	select avg(sales.quantity) from sales
)