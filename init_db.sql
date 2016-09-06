drop table if exists Users;

create table Users
(
user_num int,
user_name varchar(30),
primary key (user_num)
);


drop table if exists Routes;

create table Routes
(
route_num int auto_increment,
user_name varchar(30),
route_name varchar(100),
origin varchar(100),
destination varchar(100),
waypoints varchar(255),
primary key (route_num)
);
