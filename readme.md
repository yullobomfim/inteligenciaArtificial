#ARQUIVO DE RASCUNHO PARA PRODUZIR O ASSISTENTE

config.json = 

1- reconhecer o comando de voz

2- separar as palavras de parada
3- tokenizar usando o nltk as palavras de parada

PASSOS

config.json = ["nome": "james" "atitudes":[{"acao": "contar", "objeto": "arroz"}, {"acao": "incluir", "objeto": "arroz"}, {"acao": "excluir", "objeto": "arroz"}]]

[ x ] Reconhecer o comando de voz. [ função ]
[   ] Separar as palavras de parada (usar o corpus) [ função -> palavras_filtradas ] {ola James tudo bem com você e a Amanda como está?} result = {['ola',...]}

[   ] Tokenizar usando nltk as palavaras filtradas [ função ] res-> {["james", "acao"(incluir),"objeto"(arros)] }

#aqui você já tem as instrução prontas para usar no algoritimo
[   ] algoritimo para filtrar acoes -> resposta final do assistente


def tokenizar(array palavras_filtradas):
	algoritimo ....

resposta-> ["james", "acao"(incluir),"objeto"(arros)]


def resposta_final(["james", "acao"(incluir),"objeto"(arros)])
	if "james" != "james":
		aqui foi diferete para programa

	if acao['incluir'] == "incluir":
		resposta para isso
	if