-- Parse::SQL::Dia     version 0.17                              
-- Documentation       http://search.cpan.org/dist/Parse-Dia-SQL/
-- Environment         Perl 5.014002, /usr/bin/perl              
-- Architecture        i686-linux-gnu-thread-multi-64int         
-- Target Database     sqlite3                                   
-- Input file          model.dia                                 
-- Generated at        Fri Jan 31 16:05:30 2014                  
-- Typemap for sqlite3 not found in input file                   

-- get_constraints_drop 
drop trigger if exists metering_fk_Sensor_id_bi_tr;
drop trigger if exists metering_fk_Sensor_id_bu_tr;
drop trigger if exists metering_fk_Sensor_id_buparent_tr;
drop trigger if exists metering_fk_Sensor_id_bdparent_tr;


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
)   ;

create table Metering (
   id        int   not null,
   value     float         ,
   date      date          ,
   sensor_id int           ,
   constraint pk_Metering primary key (id)
)   ;

-- get_view_create

-- get_permissions_create
/*
-- get_inserts
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('1', 'Capteur température', 'Ce capteur permet de mesurer la température ambiante de la pièce où se trouve le module',  '16', '25', '0', '40', '° C','Température','AA','TEMP') ;
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('2', 'Capteur humidité', 'Ce capteur permet de mesurer l\'humidité ambiante de la pièce où se trouve le module', '30', '60', '15', '80', '%','Humidité','BA','HUM') ;
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('3', 'Capteur monoxyde de carbone', 'Ce capteur permet de mesurer le nombre de particule par milliard de monoxyde de carbone ambiant dans la pièce où se trouve le module', '10000', '50000', '0', '100000', 'Ppb','Monoxyde de carbone','CA','CO') ;
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('4', 'Capteur de dioxyde d\'azote', 'Ce capteur permet de mesurer le nombre de particule par milliard de dioxyde d\'Azote de la pièce où se trouve le module', '0', '212', '0', '390', 'Ppb','Dioxyde d\'azote','DA','NO2') ;
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('5', 'Capteur composant organique volatile', 'Ce capteur permet de mesurer le nombre de particules par million de composants organiques volatiles ambiant dans la pièce où se trouve le module', '0', '120', '0', '400', 'Ppm','Composant organique volatile','EA','VOC') ;
insert into Sensor(id, name, description, high_threshold, low_threshold, min_value, max_value, unit, unit_label, unique_key, bus_adress) values('6', 'Capteur de poussière', 'Ce capteur permet de mesurer le nombre de particules fines par litre ambiant dans la pièce où se trouve le module', '0', '0,2', '0', '1', 'Pcs','Poussière','FA','Dust') ;
*/
-- get_smallpackage_post_sql

-- get_associations_create
create trigger metering_fk_Sensor_id_bi_tr before insert on Metering for each row begin select raise(abort, 'insert on table Metering violates foreign key constraint metering_fk_Sensor_id') where new.sensor_id is not null and (select id from Sensor where id=new.sensor_id) is null;end;
create trigger metering_fk_Sensor_id_bu_tr before update on Metering for each row begin select raise(abort, 'update on table Metering violates foreign key constraint metering_fk_Sensor_id') where new.sensor_id is not null and (select id from Sensor where id=new.sensor_id) is null;end;
create trigger metering_fk_Sensor_id_bdparent_tr before delete on Sensor for each row begin select raise(abort, 'delete on table Sensor violates foreign key constraint metering_fk_Sensor_id on Metering') where (select sensor_id from Metering where sensor_id=old.id) is not null;end;
create trigger metering_fk_Sensor_id_buparent_tr before update on Sensor for each row when new.id <> old.id begin select raise(abort, 'update on table Sensor violates foreign key constraint metering_fk_Sensor_id on Metering') where (select sensor_id from Metering where sensor_id=old.id) is not null;end;

