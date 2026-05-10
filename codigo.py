import threading #execução simultanea no caso as threads
import time # controla o tempo e simulação de espera
import random #gera valores aleatorios

NUMERO_DE_FILOSOFOS = 5 

#criando os garfos
garfos = [threading.Lock() for i in range(NUMERO_DE_FILOSOFOS)]

#semaforo para evitar deadlock 
semaforo = threading.Semaphore(NUMERO_DE_FILOSOFOS - 1)

#funcao que representa cada filosofo 
def run(filosofo,semaforo, mutex, tempos):
    print(f"Filósofo {filosofo['nome']} chegou à mesa")

    #registra o tempo de inicio da execucao
    inicio_tempo = time.time()
    
    while True:
        print(f"Filosofo {filosofo['nome']} esta pensando")

        #espera um tempo aleatorio simulando pensamento
        time.sleep(random.uniform(1, 3))

        #avisa que parou de pesar é agora que comer
        print(f"Filosofo {filosofo['nome']} quer comer")

        semaforo.acquire() #entra no semaforo
        esquerda = filosofo["id"] 

        #define o garfo da direita para circular na mesa
        direita = (filosofo["id"] + 1) % NUMERO_DE_FILOSOFOS    

        #garfo equerda bloqueia o acesso de outros
        with mutex[esquerda]:

            #pega o garfo da direita
            with mutex[direita]:

                print(f'Filosofo{filosofo["nome"]} esta comendo')

                time.sleep(random.uniform(1,2))

        #libera o semaforo para outro filosofo tentar comer
        semaforo.release()
        break #ncerra o loop

    fim_tempo = time.time()
    tempos[filosofo["nome"]] = fim_tempo - inicio_tempo


#funcao principal
def main():
    #lista de filosofos com id é nome
    filosofos = [{"id": 0, "nome":"Socrates"},
                 {"id": 1, "nome":"Platao"},
                 {"id": 2, "nome":"Aristóteles"},
                 {"id": 3, "nome":"Descartes"},
                 {"id": 4, "nome":"Nietzsche"}]
    
    #dicionario para armazenar o tempo de cada filosofo
    tempos = {}

    #representa os garfos 
    mutex = garfos

    #lista de threads
    threads = []

    #vai criar um thread para cada filosfo
    for i in range(NUMERO_DE_FILOSOFOS):

        #cria thread usando a funcao run
        t = threading.Thread(target=run, args=(filosofos[i], semaforo, mutex, tempos))
        
        #adiciona thread na lista
        threads.append(t)

        #inicia a execução da thread
        t.start()

    
    #espera todas as threads terminar
    for i in range(len(threads)):

        #bloqueia ate a thread terminar
        threads[i].join()

    print("\n---- RESULTADO FINAL ----")

    #imprimi tempo de cada filosofo
    for nome, tempo in tempos.items():
        print(f'{nome} demorou {tempo:2f} segundos')


#executando o programa principal
if __name__ == "__main__":
    main()