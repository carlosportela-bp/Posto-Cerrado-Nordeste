# aqui fica a "memoria" do sistema, td começa vazio (menos as constantes)

# tipos de combustivel que o posto trabalha - isso n muda, por isso tupla
TIPOS_COMBUSTIVEL = ("gasolina comum", "gasolina aditivada", "etanol", "diesel s10")

# listas onde vão os registros (cada registro é um dict)
clientes = []
combustiveis = []
bombas = []
frentistas = []

# set pra n deixar cadastrar o mesmo cpf 2x
cpfs_cadastrados = set()

# contador de id dos clientes (vai subindo a cada cadastro)
proximo_id = 1