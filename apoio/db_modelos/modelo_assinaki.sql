CREATE DATABASE assinaki CHARACTER SET utf8;
 
USE assinaki;

CREATE TABLE pais(
    id_pais INT(11) NOT NULL AUTO_INCREMENT,
    pais_nome VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_pais)
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
para integrar o local de um endereço';

CREATE TABLE uf(
    id_uf INT(11) NOT NULL AUTO_INCREMENT,
    uf_nome VARCHAR(50) NOT NULL,
    id_pais INT(11) NOT NULL,
    PRIMARY KEY (id_uf),
    FOREIGN KEY (id_pais)
        REFERENCES pais (id_pais)
        ON DELETE NO ACTION ON UPDATE CASCADE
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
para integrar o local de um endereço';

CREATE TABLE cidade(
    id_cidade INT(11) NOT NULL AUTO_INCREMENT,
    cidade_nome VARCHAR(50) NOT NULL,
    id_uf INT(11) NOT NULL,
    PRIMARY KEY (id_cidade),
    FOREIGN KEY (id_uf)
        REFERENCES uf (id_uf)
        ON DELETE NO ACTION ON UPDATE CASCADE
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
para integrar o local de um endereço';

CREATE TABLE bairro(
    id_bairro INT(11) NOT NULL AUTO_INCREMENT,
    bairro_nome VARCHAR(50) NOT NULL,
    id_cidade INT(11) NOT NULL,
    PRIMARY KEY (id_bairro),
    FOREIGN KEY (id_cidade)
        REFERENCES cidade (id_cidade)
        ON DELETE NO ACTION ON UPDATE CASCADE
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
para integrar o local de um endereço';

CREATE TABLE rua(
    id_rua INT(11) NOT NULL AUTO_INCREMENT,
    rua_nome VARCHAR(150) NOT NULL,
    rua_numero VARCHAR(10) NOT NULL,
    rua_complemento VARCHAR(150) NOT NULL,
    rua_cep VARCHAR(50) NOT NULL,
    id_bairro INT(11) NOT NULL,
    PRIMARY KEY (id_rua),
    FOREIGN KEY (id_bairro)
        REFERENCES bairro (id_bairro)
        ON DELETE NO ACTION ON UPDATE CASCADE
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
para integrar o local de um endereço';

CREATE TABLE preco_assinatura(
    id_preco INT(11) NOT NULL AUTO_INCREMENT,
    preco_custo DECIMAL(9,3) NOT NULL,
    PRIMARY KEY (id_preco)
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
base para o calculo do preço de venda do ingresso';

CREATE TABLE _release(
    id_release INT(11) NOT NULL AUTO_INCREMENT,
    titulo varchar(250) NOT NULL,
    texto TEXT NULL,
    img_path TEXT NULL,
    video_path TEXT NULL,
    PRIMARY KEY (id_release)
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
conteúdo em forma de texto e o caminha para a imagem vinculada ao conteúdo de promoção do  serviço de assinatuta';

CREATE TABLE planos(
    id_planos INT(11) NOT NULL AUTO_INCREMENT,
    planos_nome VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_planos)
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
nome dos planos conforme a demanda de cada cliente';

CREATE TABLE cliente(
    id_cliente INT(11) NOT NULL AUTO_INCREMENT,
    cliente_nome VARCHAR(150) NOT NULL,
    cliente_sobrenome VARCHAR(150) NOT NULL,
    cliente_data_nascimento DATE NOT NULL,
    cliente_estado_civil VARCHAR(150) NOT NULL,
    clientes_email VARCHAR(150) NOT NULL,
    cliente_phone_fixo VARCHAR(50) NOT NULL,
    cliente_celphone VARCHAR(50) NOT NULL,
    cliente_cpf VARCHAR(11) NOT NULL,
    id_rua INT(11) NOT NULL,
    PRIMARY KEY (id_cliente),
	FOREIGN KEY (id_rua)
        REFERENCES rua (id_rua)
        ON DELETE NO ACTION ON UPDATE CASCADE
)  ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
os clientes são dividodos em PF e PJ e cada natureza tem suas especificações e endereços e cada assinatura 
pertence apenas um cliente';

CREATE TABLE pessoa_juridica(
    id_pj INT(11) NOT NULL AUTO_INCREMENT,
    pj_nome VARCHAR(150) NOT NULL,
    pj_razao_social VARCHAR(150) NOT NULL,
    pj_cnpj VARCHAR(14) NOT NULL,
    pj_insc_municipal VARCHAR(20) NOT NULL,
    pj_insc_estadual VARCHAR(20) NOT NULL,
    id_cliente INT(11) NOT NULL,
    PRIMARY KEY (id_pj),
    FOREIGN KEY (id_cliente)
        REFERENCES cliente (id_cliente)
        ON DELETE NO ACTION ON UPDATE CASCADE    
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
nome dos planos conforme a demanda de cada cliente';

CREATE TABLE login(
    id_login INT(11) NOT NULL AUTO_INCREMENT,
    login_username VARCHAR(150) NOT NULL,
    login_password VARBINARY(150) NOT NULL,
    id_cliente INT(11) NOT NULL,
    PRIMARY KEY (id_login),
    FOREIGN KEY (id_cliente)
		REFERENCES cliente (id_cliente)
        ON DELETE NO ACTION ON UPDATE CASCADE
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
login para cada cliente usuário do serviço de assinatura';

CREATE TABLE tipo_documento(
    id_tipo_documento INT(11) NOT NULL AUTO_INCREMENT,
    nome_tipo_documento VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_tipo_documento)
)  ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
classificação dos tipos em grupos';

CREATE TABLE documento(
    id_documento INT(11) NOT NULL AUTO_INCREMENT,
    documento_content LONGTEXT NOT NULL,
    documento_data DATE NOT NULL,
    documento_quantidade_partes INT(11) DEFAULT 2,
    id_tipo_documento INT(11) NOT NULL,
    PRIMARY KEY (id_documento),
    FOREIGN KEY (id_tipo_documento)
        REFERENCES tipo_documento (id_tipo_documento)
        ON DELETE NO ACTION ON UPDATE CASCADE
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
documento que será assinado';

CREATE TABLE assinatura(
    id_assinatura INT(11) NOT NULL AUTO_INCREMENT,
    assinatura_cod VARBINARY(150) NOT NULL,
    id_cliente INT(11) NOT NULL,
    PRIMARY KEY (id_assinatura),
    FOREIGN KEY (id_cliente)
        REFERENCES cliente (id_cliente)
        ON DELETE NO ACTION ON UPDATE CASCADE
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
assinatura utilizada para assinar o documento e cada cliente possuem apenas uma assinatura';

CREATE TABLE documento_assinado(
    id_doc_ass INT(11) NOT NULL AUTO_INCREMENT,
    doc_ass_status VARCHAR(15) DEFAULT 'Falta',
    id_cliente INT(11) NOT NULL,
    id_documento INT(11) NOT NULL,
    PRIMARY KEY (id_doc_ass),
    FOREIGN KEY (id_cliente)
        REFERENCES cliente (id_cliente)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_documento)
        REFERENCES documento (id_documento)
        ON DELETE CASCADE ON UPDATE CASCADE
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
cada cliente tem uma assinatura em exatamente um documento por vez, mas uma assinatura pode
estar em muitos documentos e um cliente pode ter assinado mais de um documento.';

CREATE TABLE dados_cartao(
    id_cartao INT(11) NOT NULL AUTO_INCREMENT,
    cartao_name VARCHAR(150) NOT NULL,
    cartao_number VARBINARY(50) NOT NULL,
    cartao_data DATE NOT NULL,
    cartao_security_cod VARBINARY(10) NOT NULL,
    cartao_password VARBINARY(150) NOT NULL,
    id_pais INT(11) NOT NULL,
    PRIMARY KEY (id_cartao),
    FOREIGN KEY (id_pais)
        REFERENCES pais (id_pais)
        ON DELETE NO ACTION ON UPDATE CASCADE
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
dados do cartão para cada cliente usuário do serviço de assinatura';

CREATE TABLE status_pagamento(
    id_status INT(11) NOT NULL AUTO_INCREMENT,
    id_cliente INT(11) NOT NULL,
    id_cartao INT(11) NOT NULL,
    pagamento_status CHAR NOT NULL,
    PRIMARY KEY(id_status),
    FOREIGN KEY (id_cliente)
		REFERENCES cliente (id_cliente)
        ON DELETE NO ACTION ON UPDATE CASCADE,
    FOREIGN KEY (id_cartao)
		REFERENCES dados_cartao (id_cartao)
        ON DELETE NO ACTION ON UPDATE CASCADE
)   ENGINE=INNODB DEFAULT CHARACTER SET=UTF8 COLLATE = UTF8_BIN COMMENT='
controle pagamento do cliente';

