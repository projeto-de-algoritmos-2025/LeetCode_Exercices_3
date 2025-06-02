# LeetCode_Exercices_3

## Lista de Exercícios - LeetCode (Algoritmos Ambiciosos)

**Número da Lista**: 3  
**Conteúdo da Disciplina**: Algoritmos Ambiciosos

## Alunos

| Matrícula   | Aluno                        |
| ----------- | --------------------------- |
| 20/2063462  | Samuel Alves Silva          |
| 20/0024949  | Matheus Ferreira Diogo      |

---

## Sobre

Resolução de questões do LeetCode (2 difíceis e 2 médias) pelos integrantes do grupo com o objetivo de demonstrar o conhecimento adquirido nesse módulo (Algoritmos Ambiciosos) da disciplina.

---

## Exercícios Resolvidos

### [134. Gas Station (Média)](https://leetcode.com/problems/gas-station/description/?envType=problem-list-v2&envId=greedy)  
Arquivo: [`134_GasStation.py`](./134_GasStation.py)  
Problema clássico de circuito em grafo, onde é necessário determinar se é possível completar um circuito de postos de gasolina. Utiliza abordagem de soma acumulada e reinício de ponto de partida.

![134_GasStation](/assets/134PNG.PNG)

---

### [135. Candy (Difícil)](https://leetcode.com/problems/candy/)  
Arquivo: [`135_Candy.py`](./135_Candy.py)  
Distribuição ótima de doces para crianças em fila, garantindo que crianças com notas maiores recebam mais doces que seus vizinhos. Solução com duas passagens (esquerda-direita e direita-esquerda).

![135_Candy](/assets/135.PNG)

---

### [321. Create Maximum Number (Difícil)](https://leetcode.com/problems/create-maximum-number/)  
Arquivo: [`321_CreateMaximumNumber.py`](./321_CreateMaximumNumber.py)  
Dado dois arrays, o objetivo é criar o maior número possível de tamanho k, mantendo a ordem relativa dos elementos de cada array. Utiliza técnicas de subsequência máxima e merge.

![321_CreateMaximumNumber](/assets/321.PNG)

---

### [324. Wiggle Sort II (Média)](https://leetcode.com/problems/wiggle-sort-ii/)  
Arquivo: [`324_wiggle.py`](./324_wiggle.py)  
Ordenação dos elementos de forma a garantir a propriedade wiggle (nums[0] < nums[1] > nums[2] < nums[3] ...). Utiliza seleção de mediana e mapeamento de índices para rearranjar in-place.

![324_wiggle](/assets/324PNG.PNG)

---

## Como Executar

**Linguagem**: Python

Execute cada arquivo separadamente para testar os exemplos:

```sh
python [134_GasStation.py](http://_vscodecontentref_/0)
python [135_Candy.py](http://_vscodecontentref_/1)
python [321_CreateMaximumNumber.py](http://_vscodecontentref_/2)
python [324_wiggle.py](http://_vscodecontentref_/3)