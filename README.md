# Rota Inteligente: Otimização de Entregas com Algoritmos de IA

Projeto acadêmico da disciplina Artificial Intelligence Fundamentals para a empresa fictícia Sabor Express.

## Objetivo
Representar a cidade como um grafo ponderado, encontrar uma rota de menor custo com A*, comparar com BFS e agrupar pedidos próximos com K-Means.

## Execução
Requer Python 3. No terminal, execute:

```bash
python src/main.py
```

O resultado será salvo em `docs/resultado.txt`.

## Estrutura
- `src/main.py`: implementação dos algoritmos.
- `data/pedidos.csv`: dados fictícios dos pedidos.
- `docs/resultado.txt`: saída do programa.

## Limitações
O mapa e os pesos são fictícios, não há trânsito em tempo real e o projeto não resolve completamente o roteamento de múltiplos veículos.
