INSERT INTO documento(documento_content,documento_data)
VALUES("Documento1.jpg","11/12/20");

insert into cliente (cliente_nome,cliente_sobrenome,cliente_data_nascimento,cliente_estado_civil,
clientes_email,cliente_phone_fixo,cliente_celphone,cliente_cpf,id_rua)
value("Fernando1","gomes","1989/04/11","solteiro",
"fernandoti@live.com","7133224565","71992114683","04234356784","1");

INSERT INTO assinatura(assinatura_cod,id_cliente)VALUES("552543535355456","2");

INSERT INTO documento_assinado(id_cliente,id_documento)VALUES("1","1");
-- insert na tabela documento assinado ok!

select * from cliente;
select * from assinatura;
select * from documento_assinado;
select * from login;

-- ########################################################

insert into cliente (cliente_nome,cliente_sobrenome,cliente_data_nascimento,cliente_estado_civil,
clientes_email,cliente_phone_fixo,cliente_celphone,cliente_cpf,id_rua)
value("Fernando1","gomes","1989/04/11","solteiro",
"fernandoti@live.com","7133224565","71992114683","04234356784","1");

insert into assinaki.login(login_username, login_password, id_cliente)
select l.id_cliente
from (select id_cliente from cliente order by id_cliente desc limit 1) l
where not exists(select 1 from cliente where
				cliente_nome="Fernando"
                and
                cliente_cpf="04234356784");

select id_login,login_username,login_password from login;

select id_cliente from cliente order by id_cliente desc limit 1;

select 1 from cliente where
				cliente_nome="Fernando"
                and
                cliente_cpf="04234356784";
