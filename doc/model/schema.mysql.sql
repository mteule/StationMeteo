-- Parse::SQL::Dia          version 0.20                              
-- Documentation            http://search.cpan.org/dist/Parse-Dia-SQL/
-- Environment              Perl 5.014002, /usr/bin/perl              
-- Architecture             x86_64-linux-gnu-thread-multi             
-- Target Database          mysql-innodb                              
-- Input file               model.dia                                 
-- Generated at             Mon Feb 17 11:40:49 2014                  
-- Typemap for mysql-innodb not found in input file                   

-- get_constraints_drop 
alter table Metering drop foreign key metering_fk_Sensor_id ;

-- get_permissions_drop 

-- get_view_drop

-- get_schema_drop
drop table if exists Sensor;
drop table if exists Metering;

-- get_smallpackage_pre_sql 

-- get_schema_create
create table Sensor (
   id             int          not null,
   name           varchar(255)         ,
   description    varchar(255)         ,
   high_threshold float                ,
   low_threshold  float                ,
   min_value      float                ,
   max_value      float                ,
   unit           varchar(255)         ,
   unit_label     varchar(255)         ,
   unique_key     varchar(255)         ,
   bus_adress     varchar(255)         ,
   constraint pk_Sensor primary key (id)
)   ENGINE=InnoDB DEFAULT CHARSET=latin1;
create table Metering (
   id        int   not null,
   value     float         ,
   date      date          ,
   sensor_id int           ,
   raw       int           ,
   constraint pk_Metering primary key (id)
)   ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- get_view_create

-- get_permissions_create

-- get_inserts
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('1', 'Capteur température', 'Ce capteur permet de mesurer la température ambiante de la pièce où se trouve le module',  '16', '25', '0', '40', '° C','Température','AA','TEMP') ;
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('2', 'Capteur humidité', 'Ce capteur permet de mesurer l\'humidité ambiante de la pièce où se trouve le module', '30', '60', '15', '80', '%','Humidité','BA','HUM') ;
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('3', 'Capteur monoxyde de carbone', 'Ce capteur permet de mesurer le nombre de particule par milliard de monoxyde de carbone ambiant dans la pièce où se trouve le module', '10000', '50000', '0', '100000', 'Ppb','Monoxyde de carbone','CA','CO') ;
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('4', 'Capteur de dioxyde d\'azote', 'Ce capteur permet de mesurer le nombre de particule par milliard de dioxyde d\'Azote de la pièce où se trouve le module', '0', '212', '0', '390', 'Ppb','Dioxyde d\'azote','DA','NO2') ;
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('5', 'Capteur composant organique volatile', 'Ce capteur permet de mesurer le nombre de particules par million de composants organiques volatiles ambiant dans la pièce où se trouve le module', '0', '120', '0', '400', 'Ppm','Composant organique volatile','EA','VOC') ;
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('6', 'Capteur de poussière', 'Ce capteur permet de mesurer le nombre de particules fines par litre ambiant dans la pièce où se trouve le module', '0', '0,2', '0', '1', 'Pcs','Poussière','FA','Dust') ;

-- get_smallpackage_post_sql

-- get_associations_create
alter table Metering add constraint metering_fk_Sensor_id 
    foreign key (sensor_id)
    references Sensor (id) ;
