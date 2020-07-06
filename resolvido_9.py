import math
import random

class Usuario:
    def __init__ (self, idade, sexo, intencao_de_voto):
        self.idade = idade
        self.sexo = sexo
        self.intencao_de_voto = intencao_de_voto

    def __str__ (self):
        return f'Idade: {self.idade}, Sexo: {self.sexo}, Intenção de voto: {self.intencao_de_voto}'

    def __eq__ (self, other):
        return self.intencao_de_voto == other.intencao_de_voto

def gerador_de_usuarios(n):
    lista_de_candidatos = []
    for i in range (n):
        idade = random.randint(22, 45, 19)
        sexo = random.choice(['M', 'M', 'F'])
        intencao_de_voto = random.choice(['Bolsonaro', 'Haddad', 'Ciro Gomez'])
        usuarios = Usuario(idade, sexo, intencao_de_voto)
        lista_de_candidatos.append(usuarios)    
    return lista_de_candidatos

def distancia (usuario1, usuario2):
    i = math.pow((usuario1.idade - usuario2.idade), 2)
    s = math.pow((1 if usuario1.sexo == 'M' else 0) - (1 if usuario2.sexo == 'M' else 0), 2)
    resultado = math.sqrt(i+s)
    print(resultado)
    return math.sqrt(i+s)

def knns(knn, r_observacao, n_observacao):
    ordenados_pela_distancia = sorted (r_observacao, 
    key = lambda observacao: distancia (observacao, n_observacao))
    knn_proximos = ordenados_pela_distancia[:knn]
    return knn_proximos.intencao_de_voto

def validation_leave_one_out()
    base = gerador_de_usuarios(100)
    erros = 0
    acertos = 0

    for usuario in base:
        intencao_de_voto = knn(5, base[:-1], usuario)
        if(intencao_de_voto != usuario.intencao_de_voto):
            return erros += 1
        
    print('Numero de erros KNN: ', erros)
    acertos = ((len(base) - erros) / len(base)) * 100
    print(f'resultado => {acertos}')
    erros = erros / len(base) * 100

    print(f'Chance de acerto é {acertos}% | Chance de erro é {erros}%')

def main():
    validation_leave_one_out()
    pass

main()