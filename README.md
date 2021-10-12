# Projeto_Batocera.Linux <br>

<a href="https://batocera.org/"> Batocera</a> é um sistema operacional baseado em Linux com foco em emulação de jogos retro<br>

Com exigencias minimas, é ótimo para transformar computadores antigos e parados em um "Multi Games" com jogos nostalgicos de Super Nintendo, Nintendo 64, Playstation 1, entre outros.

#Autor: Marcos Paulo da Costa<br>
#Linkedin: https://www.linkedin.com/in/marcospcostadev/<br>
#Facebook: https://www.facebook.com/marcos.nokbuk/<br>
#Instagram: https://www.instagram.com/marcos.nok/<br>
#Data de criação: 12/10/2021<br>
#Data de atualização: 12/10/2021<br>
#Versão: Batocera 32<br>
#Testado no Notebook Ideapad S145 i7-8565U 8gb RAM GeForce MX110 2GB

#Instalação do Batocera v32 em HD Externo ou Pen-Drive

#01_ Software para a gravação das Imagem do Batocera no Dispositivo<br>

	_ Balena Etcher: https://www.balena.io/etcher/

#02_ Download da Imagem do Batocera v32
		
	_ Site oficial do Batocera: https://batocera.org/download

#03_ Gravando a imagem do Batocera v32 no Dispositivo Externo

	_ Abra o Balena Etcher -> Flash From a File -> Selecione a imagem do Batocera
  _ Select Target -> Selecione o Pen Drive(tome bastante cuidado para não selecionar outro dispositivo!)
	_ Flash!

#04_ Dando boot no seu computador com o Batocera v32
	
  _ Reinicie o computador, e acesse a BIOS do computador (https://canaltech.com.br/notebook/como-acessar-a-bios-do-meu-computador/)
  _ Mude a ordem de BOOT do seu computador para o dispositivo com o Batocera v32
  _ Salve as configurações e reinicie o computador

  PS: Caso não inicie o Batocera, desative o "secure boot" na bios do seu computador.

#05_ Configurações básicas do Batocera v32

	_ OBS5: por padrão o Batocera v31 vem configurado em Inglês
	_ Alterar a linguagem: Start (Menu), System Settings, Language: Portugues Brasileiro
	_ OBS6: na versão v32 do Batocera não é necessário reinicializar o sistema
	_ Atualizando a lista de jogos: Start (Menu), Opções de Jogos, Atualizar Lista de Jogos, Sim
	_ Para sair de um jogo pressiona: Start + Select ou Esc

#06_ Partições do Batocera v32

	_ Partição BATOCERA: sistema de boot e arquivos de inicialização/binários do Batocera
	_ Partição SHARE: localização das ROMS (jogos), BIOS (PS2/PS3, etc...), Músicas, Temas, etc...
	_ Na partição SHARE no diretório: roms e onde fica localizado todos os diretórios dos
	_ consoles que o Batocera tem suporte, cada diretório tem um nome correspondente ao
	_ seu console, exemplo: snes = Super Nintendo, psx = Playstation, n64 = Nintendo 64, etc...
  _ na pasta BIOS é onde fica todos os arquivos para o funcionamento dos emuladores, por padrão ele não vem com todos, e caso você tente emular um console que precise de bios, ele vai dar um erro(PS1, PS2, etc)

#07_ Dicas de configurações dos emuladores

	_ Nintendo 64: emulador que funciona perfeitamente os jogos: LIBRETRO / PARALLEL N64
	_	Acessar Nintendo 64, Opções (Select), Opções Avançadas do Sistema, Emulador: LIBRETRO / PARALLEL N64
	_ Playstation 2: configuração do recurso de Speedhacks do PCX2-CONFIG
	_	Acessar o Menu de Jogos, F1 (Arquivos), Aplicativos, pcsx2-config
	_	Config, Video (GS), Core GS Settings, Speedhacks
	_		Enable speedhacks: ON
	_		EE Cyclerate [Not Recommended]: 3
	_		EE Cycle Skipping [Not Recommended]: 3
	_		Enable INTC Spin Detection: ON
	_		Enable Wait Loop Detection: ON
	_		Enable fast CDVD: ON
	_		mVU Flag Hack: ON
	_		MTUV (Multi-Threaded microVU1): ON
	_	System, Exit
	_ Atualização das informações das ROMS (Screen Scraper): fazer o cadastro no site: https://www.screenscraper.fr/
	_	Acessar o Menu de Jogos, Menu (Start), Scrape
	_		Banco de Dados: Screenscraper
	_		Fonte da Imagem: Screenshot
	_		Fonte da Caixa: Caixa 2D
	_		Fonte do Logotipo: Logotipo
	_		Obter Avaliações: ON
	_		Obter Vídeos: ON
	_		Obter Fanart: ON
	_		Obter parte de trás da Caixa: ON
	_		Obter Mapa: ON
	_		Obter Manual: ON
	_		Obter Configuração do Controle e Teclado: ON
	_		Usuário: usuário_screenscraper
	_		Senha: senha_screenscraper
	_	Iniciar Procura
	_		Filtro: Apenas Mídias Ausentes
	_		Sistema: Número de Itens Selecionados
	_	Iniciar (Aguardar esse processo demora dependendo da quantidade de jogos para obter as informações)
	_	Voltar, Opções de Jogos, Atualizar Listas de Jogos, Sim 

  #08_ Adicionar BIOS dos Consoles

	_ Baixe todos os arquivos da pasta BIOSaqui no GitHub em um pen drive a parte
	_	No BATOCERA, aperte f1
	_ Copie todos os arquivos para a pasta BIOS e saia(CTRL + Q)

  

