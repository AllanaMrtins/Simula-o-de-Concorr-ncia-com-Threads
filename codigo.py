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
    inicio_time = time()
    
    while True:
        #nao usa recursos compartilhados
        print(f'Filosofo {filosofo["nome"]} esta pensando')

        #espera um tempo aleatorio simulando pensamento
        time.sleep(random.uniform(1, 3))

        #avisa que quer comer
        print(f'Filosofo {filosofo["nome"]} quer comer')


