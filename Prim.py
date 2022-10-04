import heapq
import random

#Ler o número de vértices e arestas
n, m = input().split()
n = int(n)
m = int(m)

#Declara um vetor vazio
H = []

#Criar listas de vizinhança, para cada nó terá uma lista
# de vizinhos com os custos das arestas para os vizinhos
n_out = [[]*n for i in range(n)]

#Ler as arestas do Grafo com o peso

for j in range(m):
    #Lê a aresta que liga "a" e "b" com um custo "c"
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    #Na lista de vizinos de "A", coloca o "B" com areta com peso "C"
    n_out[a].append((b,c))
    #Na lista de vizinos de "B", coloca o "A" com areta com peso "C"
    n_out[b].append((a,c))

#Escolher um vértice aleatoriamente, usando o método randint
#da biblioteca random
#Selecionar um inteiro qualquer entre 0 e a qtd de vértices - 1
raiz = random.randint(0,n-1)

#Colocar no Heap as arestas que conectam a raiz a outro vértice
#Para cada vizinho da raiz coloca no heap com o peso
for (x,c) in n_out[raiz]:
    heapq.heappush(H, (c, raiz, x))

# Número de arestas na árvore no início é 0
n_edges = 0
#Custo total (soma dos pesos) no início é 0
custo_tot = 0
#O vértice que já foi selecionado é "marcado"
marcados = [raiz]
# A Arovore geradora ainda não possui nenhuma aresta
arv_ger_min = []


#Agora começa as interações
while n_edges < n-1:
    #Vai no heap e pega a aresta mais barata
    #Mas toma cuidado para não pegar 2 vértices já marcados
    # Arestas que conectam vértices marcados não podem ser selecionadas
    # Não criar ciclos
    while True:
        (c, a, b) = heapq.heappop(H)
        # Se o vértice B não estiver em marcados, para e seleciona esta aresta.
        if b not in marcados:
            break
    marcados.append(b)
    #Como a aresta foi selecionada, o custo dela é somado ao total
    custo_tot += c
    #Acrescenta a aresta na árvore geradora mínima
    arv_ger_min.append((a,b))
    #Soma 1 no número de arestas da árvore geradora
    n_edges +=1

    #Colocar no heap as próximas arestas que estarão disponíveis na interação
    #Para todo vizinho x do B, que foi o último vertice marcado
    for (x,c) in n_out [b]:
        #Verifica se o vizinho não está marcado
        if x not in marcados:
            #Se não estiver marcado, acrescenta a aresta no heap
            #Com isso só vertices não marcados com vizinhos marcados estarão
            #Disponíveis na próxima execução
            heapq.heappush(H, (c, b, x))

print(custo_tot)
print(arv_ger_min)