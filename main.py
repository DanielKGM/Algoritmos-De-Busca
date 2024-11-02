def a_estrela(no_inicial, no_final, grafo, heuristica):
    heuristica[no_inicial] = 0
    heuristica[no_final] = 0
    nos_abertos = set(no_inicial)
    nos_fechados = set()
    custo_ate_inicial = {}
    aponta_para_vizinho = {}
    caminho = []

    custo_ate_inicial[no_inicial] = 0
    aponta_para_vizinho[no_inicial] = no_inicial

    while len(nos_abertos) > 0:
        n = None

        for v in nos_abertos:
            if n == None or custo_ate_inicial[v] + heuristica[v] < custo_ate_inicial[n] + heuristica[n]:
                n = v 

        if n == None:
                print('O caminho não existe!')
                break
        elif n == no_final:
                while aponta_para_vizinho[n] != n:
                    caminho.append(n)
                    n = aponta_para_vizinho[n]
                
                caminho.append(no_inicial)
                caminho.reverse()
                print(f'Caminho: {caminho}')
                return caminho
        else:
            for(m, distancia_de_n) in grafo[n]:
                if m not in nos_abertos and m not in nos_fechados:
                    nos_abertos.add(m)
                    custo_ate_inicial[m] = custo_ate_inicial[n] + distancia_de_n
                    aponta_para_vizinho[m] = n
                elif custo_ate_inicial[m] > custo_ate_inicial[n] + distancia_de_n:
                    aponta_para_vizinho[m] = n
                    
                    if m in nos_fechados:
                        nos_fechados.remove(m)
                        nos_abertos.add(m)
        nos_abertos.remove(n)
        nos_fechados.add(n)

    print('Caminho não existente!')
    return None

def get_heuristica():
    return {
    'A': 75,
    'B': 60,
    'C': 50,
    'D': 55,
    'E': 45,
    'F': 70,
    'G': 65,
    'H': 55,
    'I': 40,
    'J': 85,
    'K': 80,
    'L': 70,
    'M': 60,
    'N': 50,
    'O': 45,
    'P': 35,
    'Q': 30
    }

def get_grafo():
    return {
        'A': [('B', 40), ('C', 20), ('D', 30)],
        'B': [('F', 30), ('E', 15)],
        'C': [('B', 10), ('F', 20), ('G', 20)],
        'D': [('H', 10), ('C', 30)],
        'E': [('I', 10)],
        'F': [('J', 20)],
        'G': [('J', 15), ('K', 20)],
        'H': [('G', 25), ('L', 20)],
        'I': [('M', 40)],
        'J': [('I', 10), ('M', 15), ('O', 15)],
        'K': [('O', 2)],
        'L': [('K', 25), ('O', 10)],
        'M': [('N', 15)],
        'N': [('P', 2)],
        'O': [('N', 8), ('P', 10)],
        'P': []
    }

if __name__ == "__main__":
    a_estrela(input('Nó inicial: '),input('Nó final: '),get_grafo(),get_heuristica())