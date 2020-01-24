class views(): # classe view para imprimir para o menu

    def __init__(self, nova_op=None, esc_op=None):
        self.nova_op = nova_op
        self.esc_op = esc_op

    def base(self): # view para escolher opcao para dados em tabelas
        print ( """\nOpcoes disponiveis para dados em tabelas:
        
        1. Listar 
        2. Inserir 
        3. Apagar
        4. Alterar 
    
        5. Sair do programa""" )

    def escolha_tabela(self): # view para escolher a tabela
        print ( "\nEscolha a TABELA:" )
        print ("""
        1. Albuns
        2. Artistas
        3. Generos
        4. Musicas

        5. Voltar Atras
        6. Sair do Programa""" )

    def escolha_operacao(self): # view para alterar em tabela musicas
        print ( """\nPretende alterar: 
        
                1.Nome
                2.ID do Album
                3.ID do Genero
                4.Compositor
                5.Milisegundos
                6.Bytes
                7.Preco Unidade""" )

    def introducao(self): # view para inicio menu introducao
        print ( """
                                -) Base de Dados (-
        
              Aplicacao (CRUD) da base de dados 'chinook' com varias opcoes.
            Escolha a opcao que pretende de acordo com as opcoes fornecidas.
        Existe a possibilidade de criar, ler, modificar e eliminar dados das tabelas.
        As tabelas utilizadas foram: 'Albums', 'Musicas', 'Generos' e 'Artistas'.
                Programa Feito por: PAULO VIRGILIO | FRANCISCO FARIA""" )

    def apresentacao_dados_albums(self): # view modo apresentacao dados em albums
        print ( "\nFormato de apresentacao de dados." )
        print ( "(AlbumID),(Titulo Album),(ArtistID)\n" )

    def apresentacao_dados_artistas(self): # view modo apresentacao dados em artistas
        print ( "\nFormato de apresentacao de dados." )
        print ( "(ArtistID),(Nome Artista)\n" )

    def apresentacao_dados_generos(self): # view modo apresentacao dados em generos
        print ( "\nFormato de apresentacao de dados." )
        print ( "(GenreID),(Nome Genero)\n" )

    def apresentacao_dados_musicas(self): # view modo apresentacao dados em musicas
        print (" \nFormato de apresentacao de dados." )
        print ("(TrackID),(Nome Musica),(AlbumID),(GenreID),(Compositor),(MiliSegundos),(Bytes),(Preco Unidade)\n" )
