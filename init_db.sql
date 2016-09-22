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
points varchar(1000),
query_time timestamp,
primary key (route_num)
);

drop table if exists RouteInfo;

create table RouteInfo
(
route_info_num int auto_increment,
route_num int,
segment_info varchar (2000),
summary varchar (1000),
date_time timestamp DEFAULT CURRENT_TIMESTAMP,
primary key (route_info_num)
);


