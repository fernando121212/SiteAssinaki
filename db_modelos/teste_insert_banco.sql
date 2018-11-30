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

-- ###############################
use assinaki;
DROP PROCEDURE teste_quant_partes;
CALL teste_quant_partes(1,
					@documento.documento_quantidade_partes,
					@documento_assinado.id_cliente,
					@documento_assinado.doc_ass_status,
                    @status_doc);
                    
SELECT @documento_quantidade_partes as _status;

select * from documento;
SELECT id_documento,
(SELECT SUM(documento_quantidade_partes) FROM documento WHERE documento.id_documento = 1) - 
(SELECT SUM(id_documento) FROM documento_assinado WHERE documento_assinado.id_documento = 1) FROM documento AS ok;

SELECT count(id_cliente) FROM documento_assinado where documento_assinado.id_documento = 4;


DELIMITER $$
CREATE PROCEDURE teste_quant_partes(
IN id_documento INT(11),
OUT documento_quantidade_partes int(11),
OUT id_cliente int(11),
OUT doc_ass_status VARCHAR(15),
OUT status_doc VARCHAR(15)
)
BEGIN

DECLARE status_doc VARCHAR(15);

SELECT DISTINCT
	documento.documento_quantidade_partes AS quant
FROM
	assinaki.documento
WHERE
	documento.id_documento IN (SELECT DISTINCT
			id_documento
        FROM
			assinaki.documento_assinado
		WHERE
			documento_assinado.id_documento = id_documento);
        /*retorna o quantidade de partes*/
        
SELECT
	COUNT(documento_assinado.id_cliente) as assinaturas_ok
FROM
	assinaki.documento_assinado
WHERE
	documento_assinado.id_documento = id_documento;
        /*retorna a soma dos assinantes*/

SET status_doc = IF(@documento_quantidade_partes = @id_cliente,"OK", "Falta");

INSERT INTO documento_assinado(
doc_ass_status,
id_cliente,
id_documento)
VALUES
(@status_doc,
"1", "2");


SELECT * FROM documento_assinado;
SELECT * FROM cliente;
SELECT * FROM documento;

UPDATE documento
SET documento_quantidade_partes = 2
WHERE id_documento = 3;

SELECT cli.id_cliente,cli.cliente_nome,doca.doc_ass_status,
doca.id_documento,documento_quantidade_partes
FROM cliente AS cli,documento AS doc,documento_assinado AS doca
WHERE doc.id_documento = doca.id_documento
AND doca.id_cliente = cli.id_cliente;