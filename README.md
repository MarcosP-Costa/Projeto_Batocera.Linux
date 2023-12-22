# Projeto_Batocera.Linux <br>

<a href="https://batocera.org/" target="_blank"> Batocera</a> é um sistema operacional baseado em Linux com foco em emulação de jogos retro<br>

Com exigencias minimas, é ótimo para transformar computadores antigos e parados em um "Multi Games" com jogos nostalgicos de Super Nintendo, Nintendo 64, Playstation 1, entre outros.

#Autor: Marcos Paulo da Costa<br>
#Linkedin: https://www.linkedin.com/in/marcospcostadev/<br>
#Facebook: https://www.facebook.com/marcos.nokbuk/<br>
#Instagram: https://www.instagram.com/marcos.nok/<br>
#Data de criação: 12/10/2021<br>
#Data de atualização: 29/11/2023<br>
#Versão: Batocera 38<br>
#Testado no Notebook Ideapad S145 i7-8565U 8gb RAM GeForce MX110 2GB

#Instalação do Batocera v38 em HD Externo ou Pen-Drive

#01_ Software para a gravação das Imagem do Batocera no Dispositivo<br>

	- Balena Etcher: https://www.balena.io/etcher/

#02_ Download da Imagem do Batocera v38
		
	- Site oficial do Batocera: https://batocera.org/download

#03_ Gravando a imagem do Batocera v38 no Dispositivo Externo

	- Abra o Balena Etcher -> Flash From a File -> Selecione a imagem do Batocera
        - Select Target -> Selecione o Pen Drive(tome bastante cuidado para não selecionar outro dispositivo!)
	- Flash!

#04_ Dando boot no seu computador com o Batocera v38
	
        - Reinicie o computador, e acesse a BIOS do computador (https://canaltech.com.br/notebook/como-acessar-a-bios-do-meu-computador/)
        - Mude a ordem de BOOT do seu computador para o dispositivo com o Batocera v38
        - Salve as configurações e reinicie o computador

         PS: Caso não inicie o Batocera, desative o "secure boot" na bios do seu computador.

#05_ Configurações básicas do Batocera v38

	- OBS5: por padrão o Batocera  vem configurado em Inglês
	- Alterar a linguagem: Start (Menu), System Settings, Language: Portugues Brasileiro
	- OBS6: na versão v38 em diante do Batocera não é necessário reinicializar o sistema
	- Atualizando a lista de jogos: Start (Menu), Opções de Jogos, Atualizar Lista de Jogos, Sim
	- Para sair de um jogo pressiona: Start + Select ou Esc

#06_ Partições do Batocera v38

	- Partição BATOCERA: sistema de boot e arquivos de inicialização/binários do Batocera
	- Partição SHARE: localização das ROMS (jogos), BIOS (PS2/PS3, etc...), Músicas, Temas, etc...
	- Na partição SHARE no diretório: roms e onde fica localizado todos os diretórios dos
	- consoles que o Batocera tem suporte, cada diretório tem um nome correspondente ao
	- seu console, exemplo: snes = Super Nintendo, psx = Playstation, n64 = Nintendo 64, etc...
        - Na pasta BIOS é onde fica todos os arquivos para o funcionamento dos emuladores, por padrão ele não vem com todos
	- Caso você tente emular um console que precise de bios, ele vai dar um erro(PS1, PS2, etc)

#07_ Dicas de configurações dos emuladores

	- 	Nintendo 64: emulador que funciona perfeitamente os jogos: LIBRETRO / PARALLEL N64
	-	Acessar Nintendo 64, Opções (Select), Opções Avançadas do Sistema, Emulador: LIBRETRO / PARALLEL N64
	- 	Playstation 2: configuração do recurso de Speedhacks do PCX2-CONFIG
	-	Acessar o Menu de Jogos, F1 (Arquivos), Aplicativos, pcsx2-config
	-	Config, Video (GS), Core GS Settings, Speedhacks
	-		Enable speedhacks: ON
	-		EE Cyclerate [Not Recommended]: 3
	-		EE Cycle Skipping [Not Recommended]: 3
	-		Enable INTC Spin Detection: ON
	-		Enable Wait Loop Detection: ON
	-		Enable fast CDVD: ON
	-		mVU Flag Hack: ON
	-		MTUV (Multi-Threaded microVU1): ON
	-		System, Exit
	-		 Atualização das informações das ROMS (Screen Scraper): fazer o cadastro no site: https://www.screenscraper.fr/
	-		Acessar o Menu de Jogos, Menu (Start), Scrape
	-		Banco de Dados: Screenscraper
	-		Fonte da Imagem: Screenshot
	-		Fonte da Caixa: Caixa 2D
	-		Fonte do Logotipo: Logotipo
	-		Obter Avaliações: ON
	-		Obter Vídeos: ON
	-		Obter Fanart: ON
	-		Obter parte de trás da Caixa: ON
	-		Obter Mapa: ON
	-		Obter Manual: ON
	-		Obter Configuração do Controle e Teclado: ON
	-		Usuário: usuário_screenscraper
	-		Senha: senha_screenscraper
	-	Iniciar Procura
	-		Filtro: Apenas Mídias Ausentes
	-		Sistema: Número de Itens Selecionados
	-	Iniciar (Aguardar esse processo demora dependendo da quantidade de jogos para obter as informações)
	-	Voltar, Opções de Jogos, Atualizar Listas de Jogos, Sim 

  #08_ Adicionar BIOS dos Consoles

	- Baixe e extraia todos os arquivos do link abaixo em um pen drive a parte
	- No BATOCERA, aperte f1
	- Copie todos os arquivos para a pasta BIOS e saia(CTRL + Q)
	
   <a href="https://drive.google.com/drive/folders/1kVid_kH7dFGuQOzpLznMt4JDzQI6yiFK?usp=sharing"> Link com as BIOS </a>

  


