class Midia:
    def __init__(self, nome, ano_lancamento, genero):
        self._nome = nome.title()
        self._ano_lancamento = ano_lancamento
        self._genero = genero.title()

    def atualizar(self, nome=None, ano_lancamento=None, genero=None):
        if nome:
            self._nome = nome.title()
        if ano_lancamento:
            self._ano_lancamento = ano_lancamento
        if genero:
            self._genero = genero.title()

    def __str__(self):
        return f"{self._nome} | {self._genero} | {self._ano_lancamento}"

class Filme(Midia):
    def __init__(self, nome, ano_lancamento, genero, duracao):
        super().__init__(nome, ano_lancamento, genero)
        self._duracao = duracao

    def atualizar(self, nome=None, ano_lancamento=None, genero=None, duracao=None):
        super().atualizar(nome, ano_lancamento, genero)
        if duracao:
            self._duracao = duracao

    def __str__(self):
        return f"{super().__str__()} | Duração: {self._duracao} min"

class Serie(Midia):
    def __init__(self, nome, ano_lancamento, genero, temporadas):
        super().__init__(nome, ano_lancamento, genero)
        self._temporadas = temporadas

    def atualizar(self, nome=None, ano_lancamento=None, genero=None, temporadas=None):
        super().atualizar(nome, ano_lancamento, genero)
        if temporadas:
            self._temporadas = temporadas

    def __str__(self):
         return f"{super().__str__()} | Temporadas: {self._temporadas}"