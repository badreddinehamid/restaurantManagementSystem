use restaurantManangementDB;

create table reservation (
    id int not null,
    num_table int not null ,
    primary key(id)
)

create table commande (
    id int not null ,
    num_table int ,
    id_product int not null ,
    primary key (id)
)

create table product (
    id int not null ,
    quantity int not null ,
    nom varchar(50) not null ,
    price float not null ,
    primary key(id)
)