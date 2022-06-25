'''
Git e Github
Configuração inicial git:
git config --global user.name "nome"
git config --global user.email "email@com.br"
git config --list - testa as configurações

git config --global --unset user.name "nome" # descadastra o nome e email das configurações

cls no cmd / clear no git: Limpa a tela

Comandos basicos:
1-) dir ou ls: É usado para listar as pastas e arquivos que contem no diretorio.
ls -a: mostra arquivos ocultos

2-) cd : é usado para acessar pastas e diretorios.
ex: cd /d/pasta/pasta\ com\ espaco/
        OBS: usa-se barra invertida para
        acessar pastas com mais de uma palavra.

cd / volta para a base do diretorio git
cd pasta - entra na pasta contida no diretorio
cd /unidade - entra na unidade escolhida (disco rigido, pendrive, etc)
cd /unidade/pasta - entra na pasta especifica
cd .. - volta um nivel da pasta local
        ex:  /d/artigos/pastas/nome
        cd.. - vai para /d/artigos/pastas
        cd.. - vai para /d/artigos
OBS: No cdm basta digitar diretorio. Ex. d: e: c:

3-) mkdir: é usado para criar pasta no diretorio
ex: mkdir nome da pasta  # Dica: Evitar usar nomes grandes de pastas

4-) echo >: usado para escrever na tela a palavra digitada apos o comando
echo nome.extensão - cria arquivo na extensao
Ex no cmd: echo hello > hello.txt

5-) del + nome do arquivo no cmd: Apaga apenas arquivos dentro da pasta.
    obs: se estiver fora da pasta, del nome da pasta apaga todos os arquivos dentro dela
rmdir + nome da pasta /S /Q: apaga a pasta com tudo dentro
# no git: rm -rf nome da pasta: apaga a pasta com arquivos dentro
rm nome do arquivo: apaga o arquivo dentro da pasta

6-) git add *: pega tudo que foi modificado e adiciona ao staged
git add .: manda tudo
git add nome do arquivo, envia somente o arquivo modificado

7-) git commit -m "texto do commit" serve para informar a
modificação feita no arquivo

8-) git status: monitora o que está acontecendo nos arquivos

# Configurando repositorio no github e sincronizando.
git remote add origin + link do repositorio no github #para

git remot -v # mostra a lista com o endereço para onde serao enviadas as alterações
dos repositorios cadastrados

git push origin master # vai mandar o repositorio local para o repositorio na nuvem

git pull origin master # Vai puxar o repositorio na nuvem para o local

git clone + link # para clonar o repositorio completo
'''