"""Programa para registar as matriculas e o tempo(segundos) de utilização de um estacionamento.
O programa deve ler uma linha com as matriculas separadas por , e os tempos em segundos separados por ,
 
p.ex.:
    00-00-oo, AB-CD-33, 33-44-ZY   (strings)
    120, 535, 10333                (segundos)
No máximo o programa deve permitir 10 matriculas/tempos"""
 
 
import numpy as np
MAX_LUGARES=10
matriculas=np.zeros(MAX_LUGARES,dtype="U8")
tempo=np.zeros(MAX_LUGARES)

 
#ler os dados
def LerDados(matriculas,tempos):
    todas_matriculas=input("Introduza as matriculas separadas por , (virgulas): ")
    todos_tempos=input("Introduza os tempos de estacionamento separados por , (virgulas): ")
    #separar os dados e inserir nos array
    matriculas_separadas=todas_matriculas.split(",")
    tempos_separados=todos_tempos.split(",")
    #verificar se as listas têm o mesmo tamanho
    if len(matriculas_separadas) != len(tempos_separados):
        print("O nº de matrículas deve ser igual ao nº de tempos")
        return
    #verificar se o array tem espaço oara tidos elementos
    if len(matriculas_separadas) > MAX_LUGARES:
        print("Introduziu matriculas a mais,só pode inserir",MAX_LUGARES)
        return
    for i in range(len(matriculas_separadas)):
        #guardar matricula
        matriculas[i]=matriculas_separadas.strip()
        #guardar os tempos
        tempos[i]=int(tempos_separados[i].strip())
    # calcular e mostrar a matricula do carro que esteve mais tempo no estacionamento
    def MaiorTempoDeEstacionamento(matriculas,tempos):
        p_maior=0
        for p in MAX_LUGARES:
            if matriculas[p]=="":
                break
            if tempos[p]>tempos[p_maior]:
                p_maior=p
        print(f"O tempo maior de estacionamento foi de {tempos[p_maior]} corresponde matricula{matriculas[p_maior]}")

    #calcular a média dos tempos de estacionamento
    def MédiaTempos(tempos):
        soma=0
        preenchidos=0
        for p in range(len(tempos)):
            if tempos[p]==0:
                break
            soma=soma+tempos[p]
            preenchidos=preenchidos+1
        media = soma/preenchidos
        return media

    #mostrar as matriculas dos carros que estiveram mais tempo no estacionamento do que a média
    def ListaSuperiorMedia(matriculas,tempos):
        media=MédiaTempos(tempos)
        for p in range(MAX_LUGARES):
            if tempos[p]==0:
                break
            if tempos[p] > media:
                print(f"{matriculas[p]} este {tempos[p]} que é superior à média")
    
    #verificar se existem algum carro que esteve no estacionamento mais do que uma vez
    def Listarrepetidos(matriculas,tempos):
        for m in matriculas:
            contar=0
            if m=="":
                break
            for m2 in matriculas:
                if m ==m2:
                    contar=contar+1
            if contar > 1:
                print(f"a matricula {m} esteve estacionada {contar} vezes")
        

    #permitir a pesquisa de uma matricula inserir atraves do utilizador e mostrar dessa matricula caso existam
    #Mostrar a lista das matriculas ordenadas pelos tempos de estacionamento (maior para o menor)
    #Mostrar os tempos de esracionamento convertido