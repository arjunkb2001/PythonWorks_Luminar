create database vegbox;
use vegbox;

create table items(
					id int auto_increment primary key,
                    name varchar (200) unique);

insert into items(name) values ('tomatto');

select * from items order by id ;

create table stock(
					id int auto_increment primary key,
                    item_id int,
                    qty int,
                    price int not null,
                    selling int ,
                    foreign key (item_id) references items(id) on delete cascade 
                    );
select * from stock;
insert into stock (item_id,qty,price,selling) values ('1','10','30','45');

create table bill(
					id int auto_increment primary key,
                    user varchar(200) not null,
                    phone int
                    );
select * from bill;
insert into bill(user,phone) values ('vijay','952656');

create table billitems(
					id int auto_increment primary key,
                    bill_id int,
                    item_id int,
                    qty int
                    );
select * from billitems;
insert into billitems(bill_id,item_id,qty) values ('2','2','2');
                    

                    

