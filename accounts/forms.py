from django import forms

class LoginCadastro(forms.Form):

    name_login = forms.CharField(label='Login', max_length=150)
    name_login.widget.attrs.update({'class': 'form-control'})

    login_password = forms.CharField(label='Password', max_length=150)
    login_password.widget.attrs.update({'class': 'form-control'})

class Cadastro(forms.Form):

    name_cliente = forms.CharField(label='Nome do cliente', max_length=150)
    name_cliente.widget.attrs.update({'class': 'form-control'})

    cliente_sobrenome = forms.CharField(label='Sobrenome', max_length=150)
    cliente_sobrenome.widget.attrs.update({'class': 'form-control'})

    name_login = forms.CharField(label='Login', max_length=150)
    name_login.widget.attrs.update({'class': 'form-control'})

    login_password = forms.CharField(label='Password', max_length=150)
    login_password.widget.attrs.update({'class': 'form-control'})


    cliente_data_nascimento = forms.DateField(label='Data de nascimento', input_formats=['%d/%m/%Y'])
    cliente_data_nascimento.widget.attrs.update({'class': 'form-control'})

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

    cliente_estado_civil = forms.ChoiceField(label='Estado civil', choices=REGIME)
    cliente_estado_civil.widget.attrs.update({'class': 'form-control'})

    cliente_email = forms.EmailField(label='Email', max_length=150)
    cliente_email.widget.attrs.update({'class': 'form-control'})

    cliente_phone_fixo = forms.CharField(label='Telefone fixo', max_length=50)
    cliente_phone_fixo.widget.attrs.update({'class': 'form-control'})

    cliente_cel_phone = forms.CharField(label='Celular', max_length=50)
    cliente_cel_phone.widget.attrs.update({'class': 'form-control'})

    cliente_cpf = forms.CharField(label='CPF', max_length=11)
    cliente_cpf.widget.attrs.update({'class': 'form-control'})

    BRASIL = 'BR'
    ARGENTINA = 'AR'
    PAISES = (
        (BRASIL, 'Brasil'),
        (ARGENTINA, 'Argentina'),
    )

    name_pais = forms.ChoiceField(label='Nome do país', choices=PAISES)
    name_pais.widget.attrs.update({'class' : 'form-control'})

    ACRE = 'AC'
    BAHIA = 'BA'

    ESTADOS = (
        (ACRE, 'Acre'),
        (BAHIA, 'Bahia'),
    )

    name_uf = forms.ChoiceField(label='Nome do  estado', choices=ESTADOS)
    name_uf.widget.attrs.update({'class': 'form-control'})

    rua_cep = forms.CharField(label='CEP', max_length=15)
    rua_cep.widget.attrs.update({'class': 'form-control'})

    RIO_BRANCO = 'RBR'
    CRUZEIRO_DO_SUL = 'CZS'
    SALVADOR = 'SSA'

    CIDADES = (
        (CRUZEIRO_DO_SUL, 'Cruzeiro do Sul'),
        (RIO_BRANCO, 'Rio Branco'),
        (SALVADOR, 'Salvador'),
    )

    name_cidade = forms.ChoiceField(label='Nome da cidade', choices=CIDADES)
    name_cidade.widget.attrs.update({'class': 'form-control'})

    name_bairro = forms.CharField(label='Nome do bairro', max_length=150)
    name_bairro.widget.attrs.update({'class': 'form-control'})

    name_rua = forms.CharField(label='Nome da rua', max_length=150)
    name_rua.widget.attrs.update({'class': 'form-control'})

    rua_numero = forms.CharField(label='Número', max_length=10)
    rua_numero.widget.attrs.update({'class': 'form-control'})

    rua_complemento = forms.CharField(label='Complemento', max_length=150)
    rua_complemento.widget.attrs.update({'class': 'form-control'})


    #     name_pj = forms.CharField(label='Nome', max_length=150)
    #     pj_razao_social = forms.CharField(label='Razão social', max_length=150)
    #     pj_cnpj = forms.CharField(label='CNPJ', max_length=14)
    #     pj_insc_estadual = forms.CharField(label='Inscrição estadul', max_length=20)
    #
#
#     name_cartao = forms.CharField(label='Cartão', max_length=150)
#     cartao_numero = forms.CharField(label='Número', max_length=50)
#     cartao_data = forms.DateField(label='Vencimento em')
#     cartao_security_cod = forms.CharField(label='Código de segurança', max_length=10)
#     cartao_password = forms.CharField(label='Senha', max_length=150)
#

