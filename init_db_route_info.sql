drop table if exists Routes;

create table Routes
(
route_num int auto_increment,
user_name varchar(100),
route_name varchar(50),
segments varchar(1000),
destination varchar(200),
query_time varchar (200),
primary key (route_num)
);