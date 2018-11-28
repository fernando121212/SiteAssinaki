USE assinaki;


INSERT INTO pais(pais_nome)
VALUES("Brasil");

INSERT INTO uf(uf_nome,id_pais)
VALUES("Ba","1");

INSERT INTO cidade(cidade_nome,id_uf)
VALUES("Madre de Deus","1");

INSERT INTO bairro(bairro_nome,id_cidade)
VALUES("centro","1");

INSERT INTO rua(
rua_nome,
rua_numero,
rua_complemento,
rua_cep,id_bairro)
VALUES(
"Rua direta",
"25",
"Predio",
"41181052",
"1");

INSERT INTO planos(planos_nome)
VALUES("Mensal"),
("Bimestral"),
("Timestral"),
("Simestral"),
("Anoal");

insert into cliente (
cliente_nome,
cliente_sobrenome,
cliente_data_nascimento,
cliente_estado_civil,
clientes_email,
cliente_phone_fixo,
cliente_celphone,
cliente_cpf,
id_rua)
value(
"Fernando3",
"gomes",
"1989/04/11",
"solteiro",
"fernandoti@live.com",
"7133224565",
"71992114683",
"04234356784",
"1"),
(
"Fernando4",
"gomes1",
"2989/04/11",
"solteiro1",
"1fernandoti@live.com",
"1133224565",
"11992114683",
"14234356784",
"1"),
(
"Fernando5",
"gomes2",
"3989/04/11",
"Casado",
"3fernandoti@live.com",
"4133224565",
"41992114683",
"44234356784",
"1");

INSERT INTO pessoa_juridica(
pj_nome,
pj_razao_social,
pj_cnpj,
pj_insc_municipal,
pj_insc_estadual,
id_cliente)
VALUES(
"Tiago",
"CNPJ",
"0687648976423",
"34556",
"23565",
"1");

INSERT INTO dados_cartao(
cartao_name,
cartao_number,
cartao_data,
cartao_security_cod,
cartao_password,
id_pais)
VALUES(
"Mastercard",
"34536646476475",
"11/12/20",
"005",
"1221",
"1");

INSERT INTO login(
login_username,
login_password,
id_cliente)
VALUES
("fernandoti@live.com",
"02345",
"1"),
("1fernandoti@live.com",
"12345",
"2"),
("2fernandoti@live.com",
"22345",
"3");

INSERT INTO preco_assinatura(preco_custo)
VALUES("50");

INSERT INTO tipo_documento(nome_tipo_documento)
VALUES
("Minuta"),
("Aluguel"),
("Prestação de serviço"),
("Contrato de crédito");

INSERT INTO documento(
documento_content,
documento_data,
documento_quantidade_partes,
id_tipo_documento)
VALUES
("Documento3.pdf",
"11/12/20",
4,
"4"),
("Documento4.pdf",
"11/12/20",
3,
"3");

INSERT INTO assinatura(assinatura_cod,id_cliente)
VALUES
("452543535355456","1"),
("052543535355443","2"),
("352543535355987","3"),
("242543535355443","4");

INSERT INTO documento_assinado(
doc_ass_status,
id_cliente,
id_documento)
VALUES
("Falta", -- saber se a quantidade de assinaturas, de clientes, é igual a quantidade de partes envolvidas para assinar um documento
"1", "3"),
("Falta",
"2", "3"),
("Falta",
"1", "4"),
-- novo documento
("Falta",
"3", "4");


INSERT INTO status_pagamento(
id_cliente,
id_cartao,
pagamento_status)
VALUES(
"1",
"1",
"p");



