**PROJETO COM GIT/GITHUB**

O script em linguagem Python do projeto da base climática foi desenvolvido em um diretório local, dentro do qual iniciou-se um repositório git local com o comando:

> git init 

Em seguida, documentou-se a primeira versão do projeto através de um commit. Inicialmente, adicionou-se a modificação do arquivo do script (*pratica6.py*) à localização temporária (*Staging Area*) com o comando:

> git add pratica6.py

E, por fim, fez-se o commit no repositório git local com uma descrição apropriada da alteração realizada:

> git commit - m "Script Python com API e captura multimídia"

Para enviar a versão atual do repostório local ao repositório remoto associado aos servidores do GitHub, criou-se um novo repositório nomeado 'Projeto---Base-Climatica---SEL0337' no GitHub e adicionou-se o endereço HTTP deste repositório remoto ao git local com o comando:

> git remote add origin https://github.com/txaviers/Projeto---Base-Climatica---SEL0337

Para verificar que o repositório remoto, designado *origin*, foi corretamente adicionado, lista-se os repositório remotos existentes com:

> git remote -v

Confirmada a execução do procedimento anterior, faz-se a atualização da *branch* master do repositório remoto com 

> git push origin master

