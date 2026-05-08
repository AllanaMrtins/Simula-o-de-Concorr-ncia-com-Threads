import threading #execução simultanea no caso as threads
import time # controla o tempo e simulação de espera
import random #gera valores aleatorios

NUMERO_DE_FILOSOFOS = 5 #qtd de filosfos na mesa

#criando os garfos que sao os recursos compartilhados
garfos = [threading.Lock() for i in range(NUMERO_DE_FILOSOFOS)]

#semaforo para evitar deadlock 
semaforo = threading.Semaphore(NUMERO_DE_FILOSOFOS - 1)

#funncao que representa cada filosofo 
def run(filosofo,semaforo, mutex, tempos):
    print(f'Filósofo {filosofo['nome']} chegou à mesa')

    #registra o tempo de inicio da execucao
    inicio_tempo = time()
    
    while True:
        #nao usa recursos compartilhados
        print(f'Filosofo {filosofo["nome"]} esta pensando')

        #espera um tempo aleatorio simulando pensamento
        time.sleep(random.uniform(1, 3))

        #avisa que quer comer
        print(f'Filosofo {filosofo["nome"]} quer comer')

        semaforo.acquire() #entra no semaforo
        esquerda = filosofo["id"] #define garfo da esquerda

        #define o garfo da direita para circular na mesa
        direita = (filosofo["id"] + 1) % NUMERO_DE_FILOSOFOS    

        #garfo equerda bloquia bloquaia o acesso de outros
        with mutex[esquerda]:

            #pega o garfo da direita
            with mutex[direita]:

                #filosofo comendo agora
                print(f'Filosofo{filosofo["nome"]} esta comendo')

                time.sleep(random(1,2))

        #libera o semaforo para outro filosofo tentar comer
        semaforo.release()
        break #ncerra o loop

    fim_tempo = time.time()
    tempos[filosofo["nome"]] = fim_tempo - inicio_tempo
