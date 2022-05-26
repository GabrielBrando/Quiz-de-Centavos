import random
import json


def intro():
    grid = ('\033[1;34m*\033[m' * 82)
    print(f'{grid}')
    print('{:^92}'.format('\033[1;32mBEM VINDO AO QUIZ DE CENTAVOS!\033[m'))
    print(f'{grid}')
    print(('\033[1;34m*\033[m' * 15), ('Este jogo foi projetado pelo aluno: Gabriel Brandão'),
          ('\033[1;34m*\033[m' * 14))
    print(('\033[1;34m*\033[m' * 7), ('Como forma de aprimoramento das habilidades adquiridas na cadeira'),
          ('\033[1;34m*\033[m' * 8))
    print(('\033[1;34m*\033[m' * 28), ('de Programação.\033[3m[PYTHON]!'), ('\033[1;34m*\033[m' * 28))
    print(f'{grid}')
    print(('\033[1;34m*\033[m' * 12), ('\033[1;32mRESPONDA AS QUESTÕES E TENTE PONTUAR O MÁXIMO QUE PUDER!\033[m'),
          ('\033[1;34m*\033[m' * 12))
    print(('\033[1;34m*\033[m' * 10), ('\033[1;33mPontuação:Fáceis = 50 pontos | Médias = 100 | Difíceis = 150\033[m'),
          ('\033[1;34m*\033[m' * 10))
    print(f'{grid}')


def lista_questoes():
    with open('questionario.json', 'r', encoding='utf-8') as arquivo:
        questionario = json.load(arquivo)
    return questionario["questionario"]


def lista_jogadores():
    with open('jogadores.json', 'r', encoding='utf-8') as arquivo:
        jogadores = json.load(arquivo)
        return jogadores


def add_jogadores(nome, pontos):
    jogador = lista_jogadores()
    jogador["jogadores"] += [{"nome":nome, "pontos":pontos}]
    with open('jogadores.json', 'w', encoding='utf-8') as arquivo:
        json.dump(jogador, arquivo, indent=4)


def question(id):
    questoes = lista_questoes()
    for questao in questoes:
        if questao["id"] == id:
            return questao


def ranking():
    jogares = lista_jogadores()
    print('-----------------------------RANKING-----------------------------')
    for player in jogares["jogadores"]:
        print(f'{player["nome"]} | {player["pontos"]}')

    print('-----------------------------------------------------------------')


def main():
    while True:
        intro()
        pontos = 0
        correct = 0
        nome = input('Digite seu nome: ')
        for contador in range(5):
            idx = random.randint(1, 24)
            question_random = question(idx)

            print('-----------------------------QUIZ-----------------------------')
            print(f'•\033[1;31m {question_random["question"]}\033[m \n')
            print(f'\033[1;34mDificuldade\033[m: {question_random["level"]} \n')
            print(f'[A] {question_random["A"]}')
            print(f'[B] {question_random["B"]}')
            print(f'[C] {question_random["C"]}')
            print(f'[D] {question_random["D"]}')
            print('--------------------------------------------------------------')

            user_answer = input('Escolha uma das alternativas: ')
            resp = user_answer.upper()
            if resp == question_random["answer"]:
                pontos += question_random["points"]
                correct += 1
                print('Resposta Correta [✓]')
            else:
                print(f'Resosta Incorreta [×] | A resposta correta era: {question_random["answer"]}')
        print('--------------------------------------------------------------')
        add_jogadores(nome=nome, pontos=pontos)
        print(f'Obrigado por jogar o nosso Quiz {nome}, você acertou {correct} perguntas e recebeu {pontos} pontos.')
        print('--------------------------------------------------------------')
        ranking()


main()
