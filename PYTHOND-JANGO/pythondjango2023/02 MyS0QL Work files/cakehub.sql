create database cakehubs;
use cakehubs;

create table cakes(
	id int auto_increment primary key,
    name varchar(200) unique,
    shape enum('rectangle','circle','square','heart')default 'square'
    
);

insert into cakes (name,shape) values ('blue forest','square');
select * from cakes;

create table cakexvarients(
		id int auto_increment primary key,
        weight varchar(100) default '1kg',
        price int not null,
        cake_id int,
        foreign key(cake_id) references cakes(id) on delete cascade
);
select * from cakexvarients;
insert into cakexvarients (weight,price,cake_id) values ('5kg','1950',6);

alter table cakexvarients add constraint unique(weight,price,cake_id);

select c.name,v.weight,v.price from cakes as c , cakexvarients as v where c.id=v.cake_id;

desc cakes;

desc cakexvarients;

create table reviews(
					id int auto_increment primary key,
                    user varchar(200)not null,
                    comment varchar(200)not null,
                    rating int not null check(rating<6),
                    cake_id int,
                    foreign key(cake_id) references cakes(id) on delete cascade
                    );
desc reviews;

insert into reviews (user,comment,rating,cake_id) value('suttu','good','10','2');

select * from reviews;

select * from cakes;

select cakes.name,reviews.comment,reviews.rating from cakes left join  reviews on cakes.id=reviews.cake_id;

select cakes.name,reviews.comment,reviews.rating from cakes inner join  reviews on cakes.id=reviews.cake_id;

select cakes.name,reviews.comment,reviews.rating from cakes right join  reviews on cakes.id=reviews.cake_id;

select * from reviews;

select name from cakes where id in (select distinct (r1.cake_id) from reviews as r1,reviews as r2  where  r1.cake_id=r2.cake_id and r1.id != r2.id);


