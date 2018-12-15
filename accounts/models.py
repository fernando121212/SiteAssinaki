from django.db import models

class Pais(models.Model):

    BRASIL = 'BR'
    ARGENTINA = 'AR'
    PAISES = (
        (BRASIL, 'Brasil'),
        (ARGENTINA, 'Argentina'),
    )

    name = models.CharField('Nome do país',max_length=50, choices=PAISES, default=BRASIL)
    slug = models.SlugField('Identificador', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = "Países"

class Uf(models.Model):
    BAHIA = 'BA'
    ESTADOS = (
        (BAHIA, 'Bahia'),
    )
    name = models.CharField('Nome do  estado', max_length=50, choices=ESTADOS, default=BAHIA)
    slug = models.SlugField('Identificador', max_length=150)
    pais = models.ForeignKey('Pais', verbose_name = 'País', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Cidade(models.Model):

    RIO_BRANCO = 'RBR'
    CRUZEIRO_DO_SUL = 'CZS'
    SALVADOR = 'SSA'

    CIDADES = (
        (CRUZEIRO_DO_SUL, 'Cruzeiro do Sul'),
        (RIO_BRANCO, 'Rio Branco'),
        (SALVADOR, 'Salvador'),
    )

    name = models.CharField('Nome da cidade', max_length=50, choices=CIDADES, default=SALVADOR)
    slug = models.SlugField('Identificador', max_length=150)
    uf = models.ForeignKey('Uf', verbose_name = 'Estado', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = "Cidades"

class Bairro(models.Model):
    name = models.CharField('Nome do bairro', max_length=50)
    slug = models.SlugField('Identificador', max_length=150)
    cidade = models.ForeignKey('Cidade', verbose_name = 'Cidade', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = "Bairros"

class Rua(models.Model):
    name = models.CharField('Nome da rua', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    rua_numero = models.CharField('Número', max_length=10)
    rua_complemento = models.CharField('Complemento', max_length=150)
    rua_cep = models.CharField('CEP', max_length=50)
    bairro = models.ForeignKey('Bairro', verbose_name = 'Bairro', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rua'
        verbose_name_plural = 'Ruas'

class Cliente(models.Model):

    SOLTEIRA = 'SLT'
    CASADA = 'CSD'
    SEPARADA = 'SPD'
    DIVORCIADA = 'DVD'
    VIUVA = 'VUV'
    UNIAO_ESTAVEL = 'UET'

    REGIME = (
        (SOLTEIRA, 'Solteira(o)'),
        (CASADA, 'Casada(o)'),
        (DIVORCIADA, 'Divorciada(o)'),
        (SEPARADA, 'Separada'),
        (VIUVA, 'Viúva(o)'),
        (UNIAO_ESTAVEL, 'União estável'),
    )

    name = models.CharField('Nome do cliente', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    cliente_sobrenome = models.CharField('Sobrenome', max_length=150)
    cliente_data_nascimento = models.DateField('Data',blank=False)
    cliente_estado_civil = models.CharField('Estado civil', max_length=150, choices=REGIME, default=SOLTEIRA)
    cliente_email = models.EmailField('Email', max_length=150)
    cliente_phone_fixo = models.CharField('Telefone fixo', max_length=50)
    cliente_cel_phone = models.CharField('Celular', max_length=50)
    cliente_cpf = models.CharField('CPF', max_length=11)
    rua = models.ForeignKey('Rua', verbose_name = 'Rua', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)


    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = "Clientes"

class Pessoa_juridica(models.Model):
    name = models.CharField('Nome', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    pj_razao_social = models.CharField('Razão social', max_length=150)
    pj_cnpj = models.CharField('CNPJ', max_length=14)
    pj_insc_estadual = models.CharField('Inscrição estadul', max_length=20)
    cliente = models.ForeignKey('Cliente', verbose_name = 'Cliente', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pessoa juridica'
        verbose_name_plural = "Pessoas juridicas"

class Login(models.Model):
    name = models.CharField('Login', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    login_password = models.CharField('Password', max_length=150)
    cliente = models.ForeignKey('Cliente', verbose_name = 'Cliente', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = "Logins"

class Dados_cartao(models.Model):
    name = models.CharField('Cartão', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    cartao_numero = models.CharField('Número', max_length=50)
    cartao_data = models.DateField('Vencimento em')
    cartao_security_cod = models.CharField('Código de segurança', max_length=10)
    cartao_password = models.CharField('Senha', max_length=150)
    pais = models.ForeignKey('Pais', verbose_name = 'País', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dados do cartao'
        verbose_name_plural = "Dados dos cartões"