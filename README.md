# Melhorando_cod_com_IA
apenas um exercício de melhorar o código com IA 
<img width="724" height="352" alt="image" src="https://github.com/user-attachments/assets/1ea94b2a-552d-4c33-9a21-0c15a130c009" />
<img width="684" height="264" alt="image" src="https://github.com/user-attachments/assets/cbd667e7-79f4-452c-8adf-c051a3ec9d64" />
<img width="683" height="281" alt="image" src="https://github.com/user-attachments/assets/7713090f-cfba-4e10-96f6-16b7e5c919d4" />




## sugestões de melhorias que a IA propós 
- Tratamento de erros

calcular_media, encontrar_maximo e encontrar_minimo vão lançar exceções se a lista estiver vazia. Vale adicionar uma verificação no início de cada função.

- Desempenho

ordenar_lista usa bubble sort O(n²), que é lento para listas grandes. Pode ser substituído pelo sorted() nativo do Python, que usa Timsort O(n log n).
calcular_media reinventa a roda — sum() + len() ou statistics.mean() são mais idiomáticos e eficientes.
encontrar_maximo e encontrar_minimo têm equivalentes nativos: max() e min().

- Organização e boas práticas

O bloco principal deveria estar dentro de if __name__ == "__main__": para permitir que o módulo seja importado sem executar o código automaticamente.
As funções poderiam ter docstrings explicando parâmetros e retorno.
Adicionar anotações de tipo (type hints) melhora a legibilidade e o suporte de IDEs.

Funcionalidades extras que fariam sentido

Uma função calcular_mediana e calcular_moda complementariam bem o conjunto estatístico atual.
Permitir que o usuário informe tamanho e limite via input ou argumentos de linha de comando tornaria o script mais flexível.

## explicando a justificativa 

- if __name__ == "__main__"
Sem essa proteção, ao importar o arquivo em outro script o código principal seria executado automaticamente, o que é um comportamento inesperado. Com ela, o bloco só roda quando o arquivo é executado diretamente.

- Input do usuário para tamanho e limite
Os valores estavam fixos no código, o que obrigava editar o arquivo a cada uso. Com input(), o script se torna reutilizável sem precisar mexer no código-fonte. Os valores padrão (or 10 e or 100) preservam a praticidade para quem só quer testar rapidamente.

- statistics.mean no lugar do loop manual
O loop reinventava algo que a biblioteca padrão já faz de forma otimizada e testada. statistics.mean também lida melhor com precisão numérica em listas de floats do que uma soma manual.

- max() e min() no lugar dos loops de máximo e mínimo
Os loops manuais percorriam a lista inteira comparando elemento por elemento — exatamente o que max() e min() já fazem internamente, de forma nativa e mais eficiente. Não havia motivo para reimplementar.

- sorted() no lugar do bubble sort
O bubble sort tem complexidade O(n²), ou seja, dobrar o tamanho da lista quadruplica o tempo de execução. O sorted() usa Timsort, com complexidade O(n log n), muito mais eficiente para listas grandes. Além disso, sorted() retorna uma nova lista sem modificar a original, evitando efeitos colaterais indesejados.

- Retorno None para listas vazias
As funções originais travavam com exceção ao receber uma lista vazia (ZeroDivisionError na média, IndexError nas demais). Retornar None sinaliza de forma controlada que não há resultado possível, permitindo que quem chama a função trate o caso sem precisar capturar exceções inesperadas.

- Type hints e docstrings
Type hints deixam explícito o que cada função espera receber e o que retorna, o que melhora o suporte de IDEs (autocomplete, alertas de tipo) e facilita a leitura do código. As docstrings cumprem papel de documentação inline, tornando desnecessário recorrer a um arquivo externo para entender o que cada função faz.

- calcular_mediana e calcular_moda
A média sozinha pode ser enganosa — uma lista com valores muito discrepantes distorce o resultado. A mediana complementa mostrando o valor central real, e a moda indica o valor mais frequente. Juntas, as três métricas dão uma visão estatística muito mais completa do conjunto de dados.


## comparando 
Aqui estão os resultados reais medidos na máquina. Os destaques:
- Ordenação — a diferença mais expressiva
O bubble sort do código original escala de forma quadrática O(n²). Com 10.000 elementos, ele levou quase 3 segundos, enquanto o sorted() fez o mesmo em 1,4ms — uma diferença de 2.091×. Quanto maior a lista, maior o abismo.
- Média, máximo e mínimo — praticamente empatados
Para listas pequenas, o loop manual é até ligeiramente mais rápido que statistics.mean, porque a função nativa carrega overhead de verificação interna. A diferença é da ordem de décimos de milissegundo e irrelevante na prática. O ganho aqui é de legibilidade e segurança, não de velocidade bruta.
- Total geral
Com 10.000 elementos, o código original gasta ~2,95 segundos no total, contra ~4ms do otimizado — 689× mais rápido. Esse ganho é quase todo atribuído à substituição do bubble sort.
Conclusão: para listas pequenas (≤100 elementos) as versões são equivalentes em velocidade. Para volumes maiores, o código otimizado é ordens de magnitude mais eficiente.
