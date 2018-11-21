select * from tipo_documento;

INSERT INTO pais(pais_nome)VALUES("Brasil");
INSERT INTO uf(uf_nome,id_pais)VALUES("Ba","1");
INSERT INTO cidade(cidade_nome,id_uf)VALUES("Madre de Deus","1");
INSERT INTO bairro(bairro_nome,id_cidade)VALUES("centro","4");
INSERT INTO rua(rua_nome,rua_numero,rua_complemento,rua_cep,id_bairro)
VALUES("Rua direta","25","Predio","41181052","1");
INSERT INTO planos(planos_nome)VALUES("Mensal");
ALTER TABLE pessoa_juridica CHANGE pj_razão_social pj_razao_social VARCHAR(150);
INSERT INTO pessoa_juridica(pj_nome,pj_razao_social,pj_cnpj,pj_insc_municipal,pj_insc_estadual)
VALUES("Tiago","CNPJ","02687648976423","34556","23565");
INSERT INTO assinatura(assinatura_cod)VALUES("452543535355456");
INSERT INTO dados_cartao(cartao_name,cartao_number,cartao_data,cartao_security_cod,cartao_password,id_pais)
VALUES("Mastercard","34536646476475","11/12/20","005","1221","1");
INSERT INTO documento(documento_content,documento_data)
VALUES("Documento.jpg","11/12/20");
INSERT INTO login(login_username,login_password)VALUES("fernandoti@live.com","12345");
INSERT INTO preco_assinatura(preco_custo)VALUES("50");
insert into cliente (cliente_nome,cliente_sobrenome,cliente_data_nascimento,cliente_estado_civil,clientes_email,cliente_phone_fixo,cliente_celphone,cliente_cpf,id_pj,id_rua,id_login)
value("Fernando","gomes","1989/04/11","solteiro","fernandoti@live.com","7133224565","71992114683","04234356784","1","1","1");
INSERT INTO registro(id_cliente,id_assinatura,id_documento)VALUES("1","1","1");
INSERT INTO _release(titulo,img_path,video_path)VALUES("texto","imagem","video");
INSERT INTO status_pagamento(id_cliente,id_cartao,pagamento_status)VALUES("1","1","p");
INSERT INTO tipo_documento(nome_tipo_documento)VALUES("PDF");
