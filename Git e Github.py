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

-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Git Básico
Se você já teve alguma experiência com programação, com certeza já criou alguma pasta _old, _backup ou algo parecido. Provavelmente você queria fazer uma alteração e estava "guardando" a versão anterior do seu código por precaução.

Não é assim que trabalham as melhores pessoas desenvolvedoras de software. Normalmente se usa alguma ferramenta de controle de versão para alterar o código e criar novas versões, sem a necessidade de fazer cópias manuais.

Existem várias ferramentas de controle de versão, tais como:

Git
Subversion
Mercurial
Merant PVCS
Visual Source Safe
Todas têm suas vantagens e desvantagens e não vamos discutir sobre elas. Aqui, vamos falar especialmente do Git, o controle de versão usado para controlar a versão do código do Kernel do Linux e criado por Linus Torvalds, criador do Linux. O Git também é usado pelo Github. Mas chega de enrolação, vamos ao que interessa!

Instalação
Você já deve ter instalado o Git no desafio anterior – Adicionando sua chave de segurança. Se já instalou, pule para o tópico Taxonomia de um comando Git (aqui embaixo). Se ainda não instalou, isso pode ser feito com o comando abaixo caso esteja usando Ubuntu (ou outra distribuição de Linux que use apt-get como gerenciador de pacotes):

$ apt-get install git
Para instalação no Mac e no Windows, você pode conferir este link:

Primeiros passos instalando Git
É importante manter o Git atualizado e você pode conferir a versão instalada no seu computador usando o comando git --version no Terminal.

Taxonomia de um comando Git
Sempre que falarmos de um comando, a estrutura será a seguinte:

git
nome do comando git que queremos executar, exemplo: git config;
opções, exemplo: git config --global;
argumentos, exemplo: git config user.email, para mostrar o e-mail definido.
Se quiser ver todas as configurações definidas na sua máquina, use o comando:

$ git config --list
ou

$ git config --global --list
Obtendo Ajuda
Com o Git também é muito fácil obter ajuda:

$ git help # mostra help geral
$ git help config # mostra help específico para o comando citado
Se precisar de ajuda para um comando específico, basta dar git help <comando>.

Iniciando um repositório
Na sua pasta HOME, em ~/workspace, crie um diretório, meu_projeto.

$ cd ~/workspace
$ mkdir meu_projeto
Neste diretório, vamos dar o comando git init, para dizer ao Git que queremos que ele comece a "olhar" para os arquivos nessa pasta:

$ cd meu_projeto
$ git init
$ ls -a
. .. .git
Como pode ver, o Git criou um arquivo .git. Esse diretório tem tudo que o Git precisa para trabalhar e indica que esse diretório está sendo controlado pelo Git.

Dependendo da versão do Git que você estiver usando é possível que apareça a seguinte mensagem depois de rodar o comando git init:

$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
No momento em que o comando de inicialização acima é rodado em um diretório, o Git por padrão precisa dar um nome para a ramificação principal em que o histórico de versões será armazenado. Originalmente o nome dado a essa ramificação era master. Atualmente, considerando o significado histórico do termo atrelado a escravidão, a comunidade tem dado preferência para a outros termos, como main, por exemplo. A mensagem mostra como podemos renomear a ramificação e como configurar o nome padrão, para que seja sempre utilizado esse nome ao inicializar o Git em um diretório. Você pode conferir o nome atual rodando o comando:

$ git branch --show-current
master
Vamos seguir a recomendação adotada pela comunidade e trocar o nome para main rodando o comando:

$ git branch -m main
$ git branch --show-current
main
Se o nome padrão já estiver configurado como main no seu computador, não é necessário fazer essa alteração. No momento, o que você precisa saber é que a ramificação principal será chamada de main e é lá que será armazenado o histórico de modificações de código do diretório em que estamos trabalhando.

Adicionando e comitando
Vejamos como o Git controla a versão dos arquivos do seu projeto! Primeiro, vamos criar um arquivo README.md e ver o que o Git nos diz com o comando git status:

$ touch README.md
$ git status
On branch main

Initial commit

Untracked files:
        README.md

nothing added to commit but untracked files present
Ele avisa que há arquivos não controlados (untracked), em outras palavras, arquivos que o Git ainda não faz controle. Vamos adicionar a área de seleção do Git:

$ git add README.md
$ git status

On branch main

Initial commit

Changes to be committed:
        new file:   README.md
Agora ele nos diz que há mudanças a serem comitadas (gravadas), sendo assim vamos comitar!

$ git commit -m "Meu primeiro commit"
$ git status
On branch main
nothing to commit, working directory clean
Pronto, fizemos nosso primeiro commit no Git! O comando git commit grava nossas modificações e a opção -m permite que o Git receba uma mensagem descritiva para nosso commit. Sem mensagem, o Git reclama!

Visualizando commits
Para ver o commit, podemos usar o comando git log:

$ git log
commit 405ef53eec6995d6be608d5b419774eed321adcf
Author: Seu nome <email@gmail.com>
Date:   Mon Apr  4 17:58:17 2015 -0300

    Meu primeiro commit
Digite q para sair do log.

Mais sobre adicionar e comitar
Muito simples até agora, né? Vamos mostrar o poder do controle de versão!

Abra o arquivo README.md e faça algumas alterações.

$ code README.md
Esse comando só funciona se você tem o VS Code instalado, mas você pode usar qualquer editor de código ou texto. E se esse comando não funcionar, você pode abrir o editor normalmente como faria com qualquer programa de computador.

Altere o arquivo e salve, volte ao terminal e dê o comando:

$ git status
On branch main
Changes not staged for commit:
        modified:   README.md

no changes added to commit
Veja que interessante: o Git diz que há mudanças que ainda não foram selecionadas para commit, sendo assim vamos adicioná-las.

$ git add README.md
$ git status
On branch main
Changes to be committed:
        modified:   README.md
E agora está no "jeito" para commit.

$ git commit -m "Altera o README.md"
Se você esquecer o -m, o Git vai abrir o editor definido em git config core.editor, no meu caso o vim. Vamos alterar para o nano:

$ git config core.editor
core.editor=vim
$ git config core.editor "nano"
Altere mais uma vez o arquivo README.md e grave com o comando:

$ git add README.md
$ git commit
Isso vai abrir o editor nano. Escreva sua mensagem no commit e salve com Ctrl+X e depois Y para confirmar.

Faça o desafio:

Leia o Git Essencial - Gravando Alterações no Repositório
Com base na documentação acima, crie um arquivo .gitignore e defina que o arquivo me_ignore.txt seja ignorado;
Dê o comando git status;
Crie o arquivo me_ignore.txt e novamente git status;
Veja se o arquivo me_ignore.txt não aparece;
Finalize o desafio quando estiver tudo pronto!


'''