from django import forms

class Pais(forms.Form):
    name = forms.CharField(label='Nome do país'),


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = "Países"

class Uf(forms.Form):
    name = forms.CharField(label='Nome do  estado', max_length=50)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Cidade(forms.Form):
    name = forms.CharField(label='Nome da cidade', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = "Cidades"

class Bairro(forms.Form):
    name = forms.CharField(label='Nome do bairro', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = "Bairros"

class Rua(forms.Form):
    name = forms.CharField(label='Nome da rua', max_length=150)
    rua_numero = forms.CharField(label='Número', max_length=10)
    rua_complemento = forms.CharField(label='Complemento', max_length=150)
    rua_cep = forms.CharField(label='CEP', max_length=50)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rua'
        verbose_name_plural = 'Ruas'

class Cliente(forms.Form):
    name = forms.CharField(label='Nome do cliente', max_length=150)

    cliente_sobrnome = forms.CharField(label='Sobrnome', max_length=150)
    cliente_data_nascimento = forms.DateField(label='Data')
    cliente_estado_civil = forms.CharField(label='Estado civil', max_length=150)
    cliente_email = forms.EmailField(label='Email', max_length=150)
    cliente_phone_fixo = forms.CharField(label='Telefone fixo', max_length=50)
    cliente_cel_phone = forms.CharField(label='Celular', max_length=50)
    cliente_cpf = forms.CharField(label='CPF', max_length=11)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = "Clientes"
#
# class Pessoa_juridica(forms.Form):
#     name = forms.CharField('Nome', max_length=150)
#     slug = forms.SlugField('Identificador', max_length=150)
#     pj_razao_social = forms.CharField('Razão social', max_length=150)
#     pj_cnpj = forms.CharField('CNPJ', max_length=14)
#     pj_insc_estadual = forms.CharField('Inscrição estadul', max_length=20)
#     cliente = forms.ForeignKey('Cliente', verbose_name = 'Cliente', on_delete=forms.DO_NOTHING)
#
#     created = forms.DateTimeField('Criado em', auto_now_add=True)
#     modified = forms.DateTimeField('Modificado em', auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Pessoa juridica'
#         verbose_name_plural = "Pessoas juridicas"
#
# class Login(forms.Form):
#     name = forms.CharField('Login', max_length=150)
#     slug = forms.SlugField('Identificador', max_length=150)
#     login_password = forms.CharField('Password', max_length=150)
#     cliente = forms.ForeignKey('Cliente', verbose_name = 'Cliente', on_delete=forms.DO_NOTHING)
#
#     created = forms.DateTimeField('Criado em', auto_now_add=True)
#     modified = forms.DateTimeField('Modificado em', auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Login'
#         verbose_name_plural = "Logins"
#
# class Dados_cartao(forms.Form):
#     name = forms.CharField('Cartão', max_length=150)
#     slug = forms.SlugField('Identificador', max_length=150)
#     cartao_numero = forms.CharField('Número', max_length=50)
#     cartao_data = forms.DateField('Vencimento em')
#     cartao_security_cod = forms.CharField('Código de segurança', max_length=10)
#     cartao_password = forms.CharField('Senha', max_length=150)
#     pais = forms.ForeignKey('Pais', verbose_name = 'País', on_delete=forms.DO_NOTHING)
#
#     created = forms.DateTimeField('Criado em', auto_now_add=True)
#     modified = forms.DateTimeField('Modificado em', auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Dados do cartao'
#         verbose_name_plural = "Dados dos cartões"
