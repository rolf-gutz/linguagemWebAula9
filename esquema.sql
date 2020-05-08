drop table if exists mensagens;
create table mensagens(
    id integer primary key autoincrement,
    usuario string not null,
    texto string not null
);