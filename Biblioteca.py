class Livro: #classe Livro
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  #True = pode emprestar; False = já emprestado
    
    def Emprestar(self):
        # Tenta emprestar o livro. Se estiver disponível, marca como indisponível e retorna True;        
        if self.disponivel:
            self.disponivel = False
            return True
        return False
    
    def Devolver(self):
        # Devolve o livro
        self.disponivel = True

    def exibirInfo(self):
        # Mostra as informações do livro + status de disponibilidade
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f'{self.titulo} do autor {self.autor} está {status}')

    def __str__(self):
        # método mágico para mostrar o nome do livro 
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"'{self.titulo}' — {self.autor} ({status})"


class Usuario: # Classe Usuário 
    def __init__(self, nome):
        self.nome = nome
        self.livrosEmprestados = []  # lista de objetos Livro

    def emprestarLivro(self, livro):
        
        if livro.Emprestar():  # Tenta emprestar o livro recebido como parâmetro
            self.livrosEmprestados.append(livro)
            print(f'{livro.titulo} emprestado com sucesso para {self.nome}')
        else:
            print(f'{livro.titulo} já está emprestado!')

    def devolverLivro(self, livro):
       
        if livro in self.livrosEmprestados: # Devolve o livro, se estiver com este usuário
            livro.Devolver()   
            self.livrosEmprestados.remove(livro)
            print(f'{livro.titulo} devolvido com sucesso!')
        else:
            print(f'{self.nome} não está com {livro.titulo}!')

    def listarLivros(self):
        # Lista os livros atualmente emprestados por este usuário
        if not self.livrosEmprestados:
            print('Nenhum livro emprestado no momento!')
        else:
            for livro in self.livrosEmprestados:
                print(f'O usuário {self.nome} está com o livro {livro.titulo}')  


class Biblioteca: #classe Biblioteca
    def __init__(self):
        self.acervo = []  # lista de objetos Livro

    def adicionarLivro(self, livro):
        # Adiciona o livro ao acervo e
        self.acervo.append(livro)        
        print(f'{livro} adicionado ao acervo!')
    
    def listarAcervo(self):
        # Lista o acervo mostrando a info de cada livro
        if not self.acervo:
            print('O acervo está vazio!')
        else:
            for livro in self.acervo:
                livro.exibirInfo()

    def buscarLivro(self, titulo):
        # Busca por título         
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower(): #transforma o digitado em minusculo
                return livro
        return None  # se não encontrar, retorna None


class LivroInfantil(Livro): #classe que herda atributos de Livro
    def __init__(self, titulo, autor, faixaEtaria):
        super().__init__(titulo, autor)        # Chama o construtor da superclasse
        self.faixaEtaria = faixaEtaria

    def exibirInfo(self):        
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f'{self.titulo} escrito por {self.autor} | Faixa Etária: {self.faixaEtaria} | {status}')

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"'{self.titulo}' — {self.autor} ({status}, {self.faixaEtaria})"



# Simulação de Sistema 

#Criação do objeto biblioteca
biblioteca = Biblioteca()

# Criação de Livros 
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")
livro_infantil1 = LivroInfantil("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "A partir de 7 anos")

# Adição dos livros ao acervo
biblioteca.adicionarLivro(livro1)
biblioteca.adicionarLivro(livro2)
biblioteca.adicionarLivro(livro_infantil1)

# Listagem do acervo
biblioteca.listarAcervo()

# Criação de usuários
usuario1 = Usuario('Sávio')
usuario2 = Usuario('Ana')

# Empréstimos
usuario1.emprestarLivro(livro1)
usuario2.emprestarLivro(livro_infantil1)

# Tentar emprestar de novo o mesmo livro
usuario1.emprestarLivro(livro1)

# Listagens por usuário
usuario1.listarLivros()
usuario2.listarLivros()

# Acervo após empréstimos
biblioteca.listarAcervo()

# Devolução
usuario1.devolverLivro(livro1)

# Listagem do usuário após devolver
usuario1.listarLivros()

# Acervo final
biblioteca.listarAcervo()
