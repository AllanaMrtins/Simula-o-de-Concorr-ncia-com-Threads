<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1> Problema dos Filósofos Jantando — Simulação de Concorrência com Threads</h1>
    <p>
        <strong>Simulação do clássico problema de concorrência “Filósofos Jantando” utilizando threads, semáforos e locks em Python.</strong>
    </p>
    <hr>
    <h2> Sobre o Projeto</h2>
    <p>Este projeto foi desenvolvido com foco em praticar conceitos de:</p>
    <ul>
        <li>Concorrência com Threads</li>
        <li>Sincronização de processos</li>
        <li>Uso de Semáforos</li>
        <li>Uso de Locks (Mutex)</li>
        <li>Controle de acesso a recursos compartilhados</li>
        <li>Simulação de problemas clássicos de IPC</li>
    </ul>
    <p>
        O sistema simula filósofos sentados em uma mesa que precisam compartilhar recursos limitados (garfos) para comer.
    </p>
    <hr>
    <h2> Funcionamento do Sistema</h2>
    <p>Cada filósofo representa uma <strong>thread independente</strong>, alternando entre:</p>
    <ul>
        <li> Pensar</li>
        <li> Comer</li>
    </ul>
    <p>
        Para comer, ele precisa de <strong>dois garfos (recursos compartilhados)</strong>.
        Para evitar conflitos, são usados semáforos e locks.
    </p>
    <hr>
    <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li>Python</li>
        <li>threading</li>
        <li>time</li>
        <li>random</li>
    </ul>
    <hr>
    <h2>📂 Estrutura do Projeto</h2>
    <pre>
filosofos-jantando/
│
├── codigo.py
└── README.html
    </pre>
    <hr>
    <h2>Como Executar</h2>
    <h3> 1 - Instale o Python</h3>
    <p><a href="https://www.python.org/">https://www.python.org/</a></p>
    <h3> 2️ - Execute o projeto</h3>
    <pre>
python main.py
    </pre>
    <hr>
    <h2> Conceitos Trabalhados</h2>
    <ul>
        <li>Threads</li>
        <li>Concorrência</li>
        <li>Sincronização</li>
        <li>Semáforos</li>
        <li>Mutex (Locks)</li>
        <li>Deadlock</li>
        <li>Race Condition</li>
    </ul>
    <hr>
    <h2>Descrição do Problema</h2>
    <p>
        Filósofos estão sentados em uma mesa circular, e entre cada um há um garfo.
        Para comer, precisam pegar dois garfos ao mesmo tempo.
        O desafio é evitar que todos fiquem esperando indefinidamente (deadlock).
    </p>
    <hr>
    <h2>Exemplo de Saída</h2>
    <pre>
Filósofo Sócrates está pensando 
Filósofo Platão quer comer 
Filósofo Aristóteles está comendo 
    </pre>
    <hr>
    <h2>Autores</h2>
    <ul>
        <li>Allana Camily de Sousa Martins</li>
        <li>Janiele de Jesus Barbosa</li>
        <li>Jose Henrique dos Santos Reis</li>
        <li>Lucas Gonçalves de Jesus Pereira</li>
    </ul>
    <hr>
    <h2>Aprendizados</h2>
    <ul>
        <li>Programação concorrente</li>
        <li>Uso de threads</li>
        <li>Sincronização de processos</li>
        <li>Controle de recursos compartilhados</li>
        <li>Prevenção de deadlock</li>
    </ul>
    <hr>
    <h2>Licença</h2>
    <p>Projeto de caráter acadêmico e educacional.</p>

</body>
</html>
