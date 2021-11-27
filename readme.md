#ARQUIVO DE RASCUNHO DURANTE A CONSTRUÇÃO DO ASSISTENTE( APENAS PARA CONSULTA, FAVOR DESCONSIDERAR)

ORDENAR OS PASSOS PARA FACILITAR A CONSTRÇÃO 

Criar o arquivo config.json com as ações e objetos

config.json = ["nome": "james" "atitudes":[{"acao": "contar", "objeto": "arroz"}, {"acao": "incluir", "objeto": "arroz"}, {"acao": "excluir", "objeto": "arroz"}]]

[ X ] Reconhecer o comando de voz. [ função ]
[ X ] Separar as palavras de parada (usar o corpus) [ função -> palavras_filtradas ] { Olá James voce pode incluir cerveja?} result = {['ola',...]}
[ x ] Tokenizar usando nltk as palavaras filtradas [ função ] res-> {["james", "acao"(incluir),"objeto"(arroz)] }

#aqui já tem as instrução prontas para usar no algoritimo
[ x  ] algoritimo para filtrar acoes -> resposta final do assistente


def tokenizar(array palavras_filtradas):
[  ]	 fazer o algoritimo ....

resposta-> ["james", "acao"(incluir),"objeto"(arroz)]


def resposta_final(["james", "acao"(incluir),"objeto"(arroz)])
	if "james" != "james":
		

	if acao['incluir'] == "incluir":
		resposta para isso
	if

Ele é um assistente de voz para auxiliar no controle de estoques.
O Assistente será capaz de:

Ler a quantidade de itens no estoque.
Informar o estoque atual quando retirar ou adicionar itens.
Informar quando o estoque minimo for atingido.

