drop table if exists Users;

create table Users
(
user_num int,
user_name varchar(100),
primary key (user_num)
);


drop table if exists Routes;

create table Routes
(
route_num int auto_increment,
user_name varchar(100),
route_name varchar(50),
segments varchar(1000),
destination varchar(200),
primary key (route_num)
);
