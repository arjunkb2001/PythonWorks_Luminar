create database olx;
show databases;
use olx;

create table vehicle (
						id int unique,
                        name varchar(200) not null,
                        kms int not null,
                        price int not null,
                        model varchar(100) not null,
                        owner_type varchar(100) not null
);

insert into vehicle (id,name,kms,price,model,owner_type) value (1,"hondacity",30000,180000,2010,"single");
insert into vehicle (id,name,kms,price,model,owner_type) value (2,"activa",30000,20000,2010,"single");
insert into vehicle (id,name,kms,price,model,owner_type) value (3,"rc200",40000,200000,2018,"single");
insert into vehicle (id,name,kms,price,model,owner_type) value (4,"honda",30000,180000,2010,"single");
insert into vehicle (id,name,kms,price,model,owner_type) value (5,"r15v3",45000,165000,2020,"single");
insert into vehicle (id,name,kms,price,model,owner_type) value (6,"duke390",30000,180000,2017,"second");
show tables;

select * from vehicle;

alter table vehicle add column location varchar(200) default "ekm";

insert into vehicle (id,name,kms,price,model,owner_type,location) value (7,"duke200",35000,180000,2018,"third","kerala");

select name,price from vehicle;


