'''
FREQUENCIA
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''


def frequencia(texto):
    freq = {}
    for pal in texto.split():
        if pal not in freq.keys():
            freq[pal] = 1
        else:
            freq[pal] += 1
    
    result = [a for a,b in sorted(freq.items(), key = lambda x: (-x[1], x[0]))]
    return result



'''
APELIDOS
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
''' 

 def apelidos(nomes):
    
    nomes.sort(key=lambda x:(len(x.split()), x))
    return nomes   




'''
FUTEBOL
Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''


def tabela(jogos):
    
    dic={}
    
    for e1,g1,e2,g2 in jogos:
        if e1 not in dic.keys():
            dic[e1] = [0,0,0]
        if e2 not in dic.keys():
            dic[e2] = [0,0,0]
        if g1==g2:
            dic[e1][0] += 1
            dic[e2][0] += 1
        elif g1>g2:
            dic[e1][0] += 3
        else:
            dic[e2][0] += 3
        
        dic[e1][1] += g1
        dic[e1][2] += g2
        dic[e2][1] += g2
        dic[e2][2] += g1
        
        res=[(x,y[0]) for x,y in sorted(dic.items(), key=lambda x: (-x[1][0], -(x[1][1]-x[1][2]), x[0]))]
            
            
    return res 



"""
ALOCA
Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

def aloca(prefs):
    proj={}
    naloc=[]
    
    for aluno,ucs in sorted(prefs.items(), key = lambda k: k[0]):
        for uc in ucs:
            if uc not in proj.keys():
                proj[uc]=aluno
                break
        if aluno not in proj.values():
                naloc.append(aluno)
            
    sorted(naloc)
    
    return naloc 


'''
CRUZAMENTOS
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    
    cruza = {}
    
    for rua in ruas:
        if rua[0] not in cruza.keys():
            cruza[rua[0]] = 1
        else:
            cruza[rua[0]] +=1
        
        if rua[-1] not in cruza.keys():
            cruza[rua[-1]] = 1
            
        elif rua[-1] != rua[0]:
            cruza[rua[-1]] +=1
            
    result = sorted(cruza.items(), key = lambda k: (k[1], k[0]))
            
    return result



  """
  HACKER
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def hacker(log):
    
    lista = {}
    
    for num, mail in log:
        if mail not in lista.keys():
            lista[mail] = num
        else:
            numf=""
            for i in range(0,16):
                if num[i] != '*':
                    numf += num[i]
                else:
                    numf += lista[mail][i]
            
            lista[mail] = numf
            
    result = [(y,x) for x,y in sorted(lista.items(), key=lambda k: (k[1].count('*'), k[0]))]        
    
    return result  



'''
ISBN
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
"Todos os nomes":"9789720047572",
'''

def isbn(livros):
    
    result = []
    
    for v,x in livros.items():
        soma=0
        soma1=0
        for i in range(0,13):
            if( i%2 == 0):
                soma += int(x[i])
                soma1 += 3 * int(x[i])
            else:
                soma += 3 * int(x[i])
                soma1 += int(x[i])
            
        if (soma % 10 != 0) and (soma1 % 10 != 0): 
            result.append(v)
        
    result.sort()
            
    return result


 '''
 ROBOT
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.
Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.
A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def robot(comandos):
    rect = []
    mx, my, Mx, My, x, y = 0,0,0,0,0,0
    dx,dy = 0,1
    for c in comandos:
        if c == 'H':
            rect.append( (mx,my,Mx,My) )
            mx, my, Mx, My, x, y, dx, dy = 0,0,0,0,0,0,0,1
        elif c == 'A':
            x += 1*dx
            y += 1*dy
            mx = min(x,mx)
            Mx = max(x,Mx)
            my = min(y,my)
            My = max(y,My)
        elif c == 'E':
            dx,dy = -dy,dx
        elif c == 'D':
            dx,dy = dy,-dx
    return rect



def intval (atual, dir, exp):
    if dir == "maxX":
        atual[0]+=1
        if exp[2] < atual[0]: exp[2] = atual[0]
    if dir == "maxY":
        atual[1]+=1
        if exp[3] < atual[1]: exp[3] = atual[1]
    if dir == "minX":
        atual[0] -= 1
        if exp[0] > atual[0]: exp[0] = atual[0]
    if dir == "minY":
        atual[1] -= 1
        if exp[1] > atual[1]: exp[1] = atual[1]


def robot(comandos):
    result = []
    dir = "maxY"
    atual=[0,0]
    exp = [0,0,0,0]
    res = []
    for x in comandos:
        if x == "H":
            result.append(exp)
            print(exp)
            atual = [0, 0]
            exp = [0,0,0,0]
            dir="maxY"
        elif x == "E" and dir == "maxY":
            dir = "minX"
        elif x == "E" and dir == "maxX":
            dir = "maxY"
        elif x == "E" and dir == "minY":
            dir = "maxX"
        elif x == "E" and dir == "minX":
            dir = "minY"
        elif x == "D" and dir == "maxY":
            dir = "maxX"
        elif x == "D" and dir == "maxX":
            dir = "minY"
        elif x == "D" and dir == "minY":
            dir = "minX"
        elif x == "D" and dir == "minX":
            dir = "maxY"
        elif x == "A":
            intval(atual ,dir, exp)
    for x in result:
        res.append(tuple(x))
    return res




"""
HORARIO
Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.
"""

def calcHoras(inscr, ucs):
    horas = 0
    
    for cadeira in inscr:
            horas += ucs[cadeira][2]
    return horas

def verifComp(inscr, ucs):
    possible = True
    verif = []
    for cadeira in inscr:
        if not possible:                #tentar max eficiencia
            break
        else:
            verif.append(cadeira)       #tentar max eficiencia
            if cadeira not in ucs.keys():
                possible = False
                break
            else:
                for cadeira2 in inscr:  #testa compatibilidade cadeira a cadeira
                    if cadeira2 not in ucs.keys():
                        possible = False
                        break
                    if cadeira2 not in verif:  #tentar max eficiencia
                        if ucs[cadeira][0] == ucs[cadeira2][0]: # Mesmo Dia
                            #UC2 acaba antes de UC ou comeca depois
                            if (ucs[cadeira2][1] + ucs[cadeira2][2] <= ucs[cadeira][1]) or (ucs[cadeira][1] + ucs[cadeira][2] <= ucs[cadeira2][1]):
                                verif.append(cadeira2)
                                continue
                            else:
                                possible = False
                                break
                                
    return possible

def horario(ucs,alunos):
    alunosValidos = []
    
    for num, inscr in alunos.items():
        if verifComp(inscr, ucs):
            alunosValidos.append((num, calcHoras(inscr, ucs)))
            
    alunosValidos.sort(key = lambda x: (-x[1],x[0]))
    return alunosValidos    



"""
FORMATA
Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.
"""

def formata(codigo):
    ind = 0
    i = 0
    l = len(codigo)
    final = ""
    newline = True
    for c in codigo:
        i += 1
        if c == ';':
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == '{':
            ind += 2
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == '}':
            final = final[:-2]
            ind -= 2
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == ' ' and newline:
            continue
        else:
            newline = False
            final += c
    
    return final


"""
Travessia em largura -> calcular o caminho mais curto
Dijkstra -> calcular o caminho mais curto em grafos pesados com pesos nao negativos
Prim -> calcular a arvore geradora minima de caminhos mais curtos, grafos pesados e nao orientados
floyd-warshall -> calcular o caminho mais curto entre todos os pares de vertices, grafo orientado e pesado

"""






"""
CONTINENTE
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.
"""

def build(fronteiras):
    adj = {}
    
    for fronteira in fronteiras:
        for pais1 in fronteira:
            if pais1 not in adj:
                adj[pais1] = set()
            for pais2 in fronteira:
                if pais1 != pais2:
                    if pais2 not in adj:
                        adj[pais2] = set()
                    adj[pais1].add(pais2)
    return adj                
    
    
def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return vis    
 
 
def maior(vizinhos):
    
    adj = build(vizinhos)
    dic = {}
    tamanho = 0
    for fronteira in vizinhos:
       for pais in fronteira:
           if pais not in dic.keys():
               dic[pais] = len(bfs(adj,pais))
               tamanho = max(dic.values())           
    return tamanho
   


'''
VIAGEM - 80%
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.



'''
def build(rotas):
    adj = {}
    
    for rota in rotas:
        for i in range(0,len(rota),2):
            if i+2 < len(rota):
                if rota[i] not in adj: 
                    adj[rota[i]] = {}
                if rota[i+2] not in adj:
                    adj[rota[i+2]] = {}
                adj[rota[i]][rota[i+2]] = rota[i+1]
                adj[rota[i+2]][rota[i]] = rota[i+1]
        
    return adj


def dijkstra(adj,o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return dist


def viagem(rotas,o,d):
    
    adj = build(rotas)
    dicc = dijkstra(adj,o)
    
    custo = dicc[d]
    return custo
    

    '''
out: {'e': {'e': 0, 'a': 19, 'r': 19, 'l': 9, 't': 23, 'c': 15, 'o': 15, 's': 10},

      'a': {'e': 19, 'a': 0, 'r': 8, 'l': 21, 't': 4, 'c': 14, 'o': 4, 's': 9}, 

      'r': {'e': 19, 'a': 8, 'r': 0, 'l': 21, 't': 12, 'c': 14, 'o': 4, 's': 9}, 

      'l': {'e': 9, 'a': 21, 'r': 21, 'l': 0, 't': 25, 'c': 7, 'o': 17, 's': 12}, 

      't': {'e': 23, 'a': 4, 'r': 12, 'l': 25, 't': 0, 'c': 18, 'o': 8, 's': 13}, 

      'c': {'e': 15, 'a': 14, 'r': 14, 'l': 7, 't': 18, 'c': 0, 'o': 10, 's': 5}, 

      'o': {'e': 15, 'a': 4, 'r': 4, 'l': 17, 't': 8, 'c': 10, 'o': 0, 's': 5}, 

      's': {'e': 10, 'a': 9, 'r': 9, 'l': 12, 't': 13, 'c': 5, 'o': 5, 's': 0}}

      resultado de aplicar dicc = fw(adj)

'''

'''
CIDADE 
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

'''
def build(ruas):
    adj = {}

    for rua in ruas:
        if rua[0] in adj.keys() and rua[-1] in adj[rua[0]].keys():
            if adj[rua[0]][rua[-1]] > len(rua):
                adj[rua[0]][rua[-1]] = len(rua)
                adj[rua[-1]][rua[0]] = len(rua)
        else:
            if rua[0] not in adj:
                adj[rua[0]] = {}
            if rua[-1] not in adj:
                adj[rua[-1]] = {}
            adj[rua[0]][rua[-1]] = len(rua)
            adj[rua[-1]][rua[0]] = len(rua)
    return adj
  

def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist 

 
def tamanho(ruas):
    
    adj = build(ruas)
    dicc = fw(adj)
    maximo = 0
    
    for x in dicc:
        for y in dicc:
            if dicc[x][y] > maximo:
                maximo = dicc[x][y]
        
    return maximo


'''
AREA - 80%
Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 
            mapa = ["..*..",
                    ".*.*.",
                    "*...*",
                    ".*.*.",
                    "..*.."]
'''




def area(p,mapa):
    
    xi,yi = p
    
    if mapa[xi][yi] == '*':
        return 0;
    else:
        vis = {(xi,yi)}
        queue = [(xi,yi)]
        while queue:
            x,y = queue.pop(0)
            for xx in [-1,0,1]:
                for yy in [-1,0,1]:
                    if abs(xx) + abs(yy) < 2:
                        if (x + xx, y + yy) not in vis:
                            if (x+xx) >= 0 and (x+xx) < len(mapa) and (y+yy) >=0 and (y+yy) < len(mapa):
                                if mapa[x+xx][y+yy] == '.':
                                    vis.add((x+xx,y+yy))
                                    queue.append((x+xx,y+yy))
                            
    
    area = len(vis)            
        
    return area
    
    
'''
LABIRINTO
Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

->

'''
def build(mapa):
    adj = {}
    altura = len(mapa)
    largura = len(mapa[0])
    
    for linha in range(0,altura):
        for coluna in range(0,largura):
            if mapa[linha][coluna] == ' ':
                if (linha,coluna) not in adj:
                    adj[(linha,coluna)] = set()
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if (abs(x) + abs(y)) == 1:  
                            if (linha+x) >=0 and (linha+x) < altura and (coluna+y) >=0 and (coluna+y) < largura:
                                if mapa[linha+x][coluna+y] == ' ':
                                    if(linha+x,coluna+y) not in adj:
                                        adj[(linha+x,coluna+y)] = set()
                                    adj[(linha,coluna)].add((linha+x,coluna+y))
                                    adj[(linha+x,coluna+y)].add((linha,coluna))
                        
    return adj

def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai

    
def caminho(mapa):
        
    o = (0,0)
    adj = build(mapa)
    d = (len(mapa) - 1, len(mapa[0]) - 1) 
    travessia = bfs(adj,d)
    caminho = ""
        
    #se aumentar x -> Sul
    #se diminuir x -> Norte
    #se aumentar y -> este
    #se diminuir y -> oeste
    while o in travessia:
        x = travessia[o][0] - o[0]
        y = travessia[o][1] - o[1]
        if x==1 and y==0:
            caminho += 'S'
        elif x==-1 and y==0:
            caminho += 'N'
        elif x==0 and y==1:
            caminho += 'E'
        elif x==0 and y==-1:
            caminho += 'O'
        o = travessia[o]    
    
    return caminho
    
    

'''
CAVALO
O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''

def saltos(o,d):
    
    saltos = 0
    x,y = o
    pai = {}
    vis = {(x,y)}
    queue = [(x,y)]
    while queue:
        (x,y) = queue.pop(0)
        if (x,y) == d:
            break
        else:
            for xx in [-2,-1,1,2]:
                for yy in [-2,-1,1,2]:
                    if abs(xx) != abs(yy):
                        if ((x+xx,y+yy)) not in vis:
                            vis.add((x+xx,y+yy))
                            pai[(x+xx,y+yy)] = (x,y)
                            queue.append((x+xx,y+yy))
    
    while d in pai:
        saltos += 1
        d = pai[d]
    
    return saltos


'''
ERDOS - 80%
O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

'''
def build(artigos):
    adj = {}
    for autores in artigos.values():
        for autor1 in autores:
            for autor2 in autores:
                if autor2 != autor1:
                    if autor1 not in adj:
                        adj[autor1] = set()
                    if autor2 not in adj:
                        adj[autor2] = set()
                    adj[autor1].add(autor2)
                    adj[autor2].add(autor1)
    return adj                


def bfs(adj,o):
    
    vis = {}
    vis[o] = 0
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis[d] = vis[v] + 1
                queue.append(d)
    return vis

def erdos(artigos,n):
    
    adj = build(artigos)
    travessia = bfs(adj, "Paul Erdos")
    
    final = [x for x,y in sorted(travessia.items(), key = lambda k: (k[1],k[0])) if y <= n]
    
    return final





"""
CRESCENTE- 90% 
Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.
 lista = [5,2,7,4,3,8]
self.assertEqual(crescente(lista),3)

"""
    
    
    
def crescente(lista):
    subsequencia = [float('inf')]
    
    for valor in lista:
        if valor >= subsequencia[-1]:
            subsequencia.append(valor)
        else:
            if len(subsequencia) == 1:
                subsequencia[-1] = valor
            elif len(subsequencia) > 1 and subsequencia[-2] <= valor:
                subsequencia[-1] = valor
                

    return len(subsequencia)
    

"""
CRESCENTE
Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.´

"""

# Programação Dinâmica - 13%
def crescente(lista):
    n = len(lista)
    if n == 0:
        return 0
    cache = [1 for x in range(n+1)]
    cache[0] = 0
    maxSub = 1

    for x in range(2, n+1):
        for y in range(x-1, 0, -1):
            if lista[x-1] >= lista[y-1]:
                cache[x] = max(cache[x], cache[y] + 1)
        
        maxSub = max(maxSub, cache[x])
    
    return maxSub



"""
ESPACA
Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.


"""

# Programação Dinâmica - 10%
def espaca(frase,palavras):
    n = len(frase)
    cache = ["" for x in range(n+1)]
    
    for x in range(n):
        for y in range(x+1, n+1):
            pal = frase[x:y]
            if pal in palavras:
                ant = cache[x]
                if x != 0 and not ant:
                    continue
                if not cache[y]:
                    cache[y] = ant + " "*(ant != "") + pal

    return cache[n]


"""
LADRAO
Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.
    
"""

# Recursiva
def ladrao(capacidade,objectos):
    if capacidade == 0 or objectos == []:
        return 0
    if objectos[-1][2] > capacidade:
        return ladrao(capacidade, objectos[:-1])
    a = objectos[-1][1] + ladrao(capacidade - objectos[-1][2], objectos[:-1])
    b = ladrao(capacidade, objectos[:-1])
    return max(a, b)

# Programação Dinâmica
def ladrao(capacidade, objetos):
    n = len(objetos)
    cache = [[0 for x in range(capacidade + 1)] for y in range(n + 1)]
    
    for i in range(n + 1):
        for peso in range(capacidade + 1):
            if i == 0 or peso == 0:
                cache[i][peso] = 0
            elif objetos[i-1][2] > peso:
                cache[i][peso] = cache[i-1][peso]
            else:
                cache[i][peso] = max( objetos[i-1][1] + cache[i-1][peso - objetos[i-1][2]] , cache[i-1][peso])

    return cache[n][peso]





"""
ROBOT
Implemente uma função que determina qual a probabilidade de um robot regressar 
ao ponto de partida num determinado número de passos. Sempre que o robot dá um 
passo tem uma determinada probabilidade de seguir para cima ('U'), baixo ('D'), 
esquerda ('L') ou direita ('R'). A função recebe o número de passos que o 
robot vai dar e um dicionário com probabilidades de se movimentar em cada uma
das direcções (as chaves são os caracteres indicados entre parêntesis).
O resultado deve ser devolvido com a precisao de 2 casas decimais.

"""
########################################
#      Programação Dinâmica - 11%      #
########################################
def probabilidade(passos,probabilidade):
    probs = {}
    
    # Movimentos possíveis vêm em pares (cima/baixo e esquerda/direita) 
    # porque tem de voltar sempre ao início
    if passos % 2 != 0:
        return 0.0
    
    limInf = -passos//3-2
    limSup = passos//3+2

    for x in range(limInf, limSup):
        for y in range(limInf, limSup):
            probs[0,x,y] = 0.0
    
    probs[0,0,0] = 1.0
    lado = ['L', 'R', 'U', 'D']
    dx = [-1,1,0, 0]
    dy = [ 0,0,1,-1]

    for p in range(1, passos+1):
        for x in range(limInf, limSup):
            for y in range(limInf, limSup):
                probs[p,x,y] = 0.0
                for k in range(4):
                    X = x + dx[k]
                    Y = y + dy[k]
                    if limInf <= X < limSup and limInf <= Y < limSup:
                        antiga = probabilidade[lado[k]]*probs[p-1,X,Y]
                        probs[p,x,y] += antiga
    
    return round(probs[passos,0,0],2)

########################################
#          Memoization - 11%           #
########################################
def aux(p, x, y, probs, cache):
    if p == 0:
        if (x,y) == (0,0):
            return 1
        else:
            return 0
    if (p,x,y) in cache:
        return cache[(p,x,y)]
    a = probs['U'] * aux(p-1, x+1, y, probs, cache)
    b = probs['D'] * aux(p-1, x-1, y, probs, cache)
    c = probs['L'] * aux(p-1, x, y-1, probs, cache)
    d = probs['R'] * aux(p-1, x, y+1, probs, cache)
    cache[(p,x,y)] = a+b+c+d
    return cache[(p,x,y)]

def probabilidade(passos,probs):
    return round(aux(passos, 0, 0, probs, {}),2) if passos % 2 == 0 else 0.0        



"""
SAQUE
Um fugitivo pretende atravessar um campo  no mínimo tempo possível (desde o 
canto superior esquerdo até ao canto inferior direito). Para tal só se poderá 
deslocar para a direita ou para baixo. No entanto, enquanto atravessa o campo 
pretende saquear ao máximo os bens deixados por fugitivos anteriores. Neste 
problema pretende-se que implemente uma função para determinar qual o máximo 
valor que o fugitivo consegue saquear enquanto atravessa o campo. 
A função recebe o mapa rectangular defindo com uma lista de strings. Nestas
strings o caracter '.' representa um espaço vazio, o caracter '#' representa 
um muro que não pode ser atravessado, e os digitos sinalizam posições onde há 
bens abandonados, sendo o valor dos mesmos igual ao digito.
Deverá devolver o valor máximo que o fugitivo consegue saquear enquanto 
atravessa o campo deslocando-se apenas para a direita e para baixo. Assuma que 
é sempre possível atravessar o campo dessa forma.

"""

# Programação Dinâmica
def saque(mapa):
    n = len(mapa)
    m = len(mapa[0])
    cache = [[0 for x in range(m + 1)] for x in range(n + 1)]
    
    for y in range(n + 1):
        for x in range(m + 1):
            if x == 0 or y == 0:
                cache[y][x] = 0
            elif mapa[y-1][x-1] == '#':
                cache[y][x] = -1
            elif mapa[y-1][x-1] != '.':
                cache[y][x] = int(mapa[y-1][x-1]) + max(cache[y-1][x], cache[y-1][x-1], cache[y][x-1])
            else:
                cache[y][x] = max(cache[y-1][x], cache[y-1][x-1], cache[y][x-1])
            
    return cache[n][m]


"""
SOMA
Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

"""

# Algoritmo de Kadane (Não percebo a necessidade da sugestão do stor de usar uma função para os prefixos)
# Programação Dinâmica
def maxsoma(lista):
    maxSum = lista[0]
    cache = [maxSum]
    i = 1
    n = len(lista)
    
    for i in range(1,n):
        cache.append(max(cache[i-1] + lista[i], lista[i]))
        maxSum = max(maxSum, cache[i])
        
    return maxSum


"""
VALIDAS
Um exemplo de um problema que pode ser resolvido de forma eficiente com 
programação dinâmica consiste em determinar, dada uma sequência arbitrária de 
números não negativos, se existe uma sub-sequência (não necessariamente contígua) 
cuja soma é um determinado valor. Implemente uma função que dado um valor e uma
listas de listas de números não negativos, devolva a lista com as listas com uma
sub-sequência cuja soma é o valor dado.

"""

def temSoma(soma, lista):
    print(lista)
    n = len(lista)
    cache = [[False for x in range(soma+1)] for x in range(n+1)]
    
    for i in range(n+1):
        cache[i][0] = True
    
    for i in range(1, n+1):
        for s in range(1, soma+1):
            if s < lista[i-1]:
                cache[i][s] = cache[i-1][s]
            else:
                cache[i][s] = cache[i-1][s] 
                if not cache[i][s]:
                    cache[i][s] = cache[i-1][s-lista[i-1]]
                    if cache[i][s]:
                        cache[i][s] = cache[i][s-lista[i-1]]

    return cache[n][soma]

def validas(soma,listas):
    return list(filter(lambda x: temSoma(soma, x), listas))



"""
VENDEDOR
Um vendedor ambulante tem que decidir que produtos levará na sua próxima viagem.
Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção, 
tem que escolher a melhor combinação de produtos a transportar dentro desse limite 
que lhe permitirá ter a máxima receita.

Implemente uma função que, dado o limite de peso que o vendedor pode transportar, 
e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua 
disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
que poderá obter se vender todos os produtos que escolher transportar, e a lista
de produtos que deverá levar para obter essa receita (incluindo repetições, 
caso se justifique), ordenada alfabeticamente.

Cada produto consiste num triplo com o nome, o valor, e o peso.

Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade 
aos produtos que aparecem primeiro na lista de entrada.

"""

# Programação Dinâmica
def vendedor(capacidade,produtos):
    n = len(produtos)
    cache = [[(0,[]) for x in range(capacidade + 1)] for y in range(n + 1)]
    
    for i in range(n + 1):
        for peso in range(capacidade + 1):
            if i == 0 or peso == 0:
                cache[i][peso] = 0,[]
            elif peso < produtos[i-1][2]:
                cache[i][peso] = cache[i-1][peso]
            else:
                a = cache[i-1][peso]
                b = cache[i][peso-produtos[i-1][2]]
                c = cache[i-1][peso-produtos[i-1][2]]
                b = b[0] + produtos[i-1][1], b[1] + [produtos[i-1][0]]
                c = c[0] + produtos[i-1][1], c[1] + [produtos[i-1][0]]
                
                cache[i][peso] = max(a,b,c,key = lambda x: x[0])
    
    cache[n][capacidade][1].sort()
    return cache[n][capacidade]

# Memoization - 11.25%
def vendedor(capacidade,produtos):
    cache = {}
    result = aux(capacidade, produtos, cache)
    result[1].sort()
    return result

def aux(capacidade, produtos, cache):
    if capacidade not in cache:
        if capacidade == 0 or produtos == []:
            cache[capacidade] = 0,[]
        elif capacidade < produtos[0][2]:
            cache[capacidade] = aux(capacidade, produtos[1:], cache)
        else:
            b = aux(capacidade - produtos[0][2], produtos, cache)
            c = aux(capacidade - produtos[0][2], produtos[1:], cache)
            a = aux(capacidade, produtos[1:], cache)
            b = b[0] + produtos[0][1], b[1] + [produtos[0][0]]
            c = c[0] + produtos[0][1], c[1] + [produtos[0][0]]
    
            cache[capacidade] = max(b, c, a, key=lambda x: x[0])
    return cache[capacidade]

# Recursiva - 9%
def vendedor(capacidade,produtos):
    result = aux(capacidade, produtos)
    result[1].sort()
    return result
    
def aux(capacidade, produtos):
    if capacidade == 0 or produtos == []:
        return 0,[]
    if capacidade < produtos[0][2]:
        return aux(capacidade, produtos[1:])
        
    a = aux(capacidade, produtos[1:])
    b = aux(capacidade - produtos[0][2], produtos)
    c = aux(capacidade - produtos[0][2], produtos[1:])
    b = b[0] + produtos[0][1], b[1] + [produtos[0][0]]
    c = c[0] + produtos[0][1], c[1] + [produtos[0][0]]
    
    return max(c, b, a, key=lambda x: x[0])

