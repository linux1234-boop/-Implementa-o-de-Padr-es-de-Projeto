#Decorator#
O Decorator é um padrão de projeto estrutural que permite que você acople novos comportamentos para objetos ao colocá-los dentro de invólucros de objetos que contém os comportamentos.

#Problema (Decorator)#
Imagine que você foi contratado para criar um sistema de vendas para uma cafeteria local de sucesso. No início, o cardápio era simples: apenas Cafe e Cha. Você criou uma classe base Bebida e duas subclasses. Tudo funcionava perfeitamente.
Dias depois, o gerente decide inovar e introduz os adicionais: Leite, Chocolate, Chantilly e Canela.
Se você tentasse resolver isso usando a herança tradicional, começaria a cair em uma armadilha mortal de design. Para permitir que o cliente personalize seu pedido, você teria que criar uma classe para cada combinação possível:

*CafeComLeite

*CafeComChocolate

*CafeComLeiteEChocolate

*CafeComLeiteChantillyECanela

*ChaComLeite

...e a lista não para de crescer.

                  [ Bebida ]
                 /          \
         [ Cafe ]            [ Cha ]
        /        \
[CafeComLeite]  [CafeComChocolate]
      |
[CafeComLeiteEChocolate]  <--Explosão de subclasses

Sempre que a cafeteria inventar um novo adicional (como Caramelo),
você terá que criar dezenas de novas classes combinadas.
Pior: se o preço do Leite subir, você precisará alterar o preço em todas as classes que usam leite. O seu código se tornou rígido, monstruoso e impossível de manter.

#Solução#

O padrão Decorator sugere que você abandone a herança direta para criar combinações e passe a usar a Composição (uma abordagem onde um objeto tem um outro objeto, em vez de ser um objeto).
Transformando os adicionais em Envoltórios (Wrappers). Um envoltório é um objeto que possui a mesma interface do objeto original (Bebida), mas carrega uma referência secreta para ele dentro de si.

Quando o cliente pede um Café com Leite e Chocolate, o sistema faz o seguinte:
1-Instancia o objeto base: pedido = Cafe()
2-Envolve o café com o leite: pedido = ComLeite(pedido)
3-Envolve o resultado com o chocolate: pedido = ComChocolate(pedido)

 ┌──────────────────────────────────────────────┐
 │ ComChocolate                                 │
 │   ┌────────────────────────────────────────┐ │
 │   │ ComLeite                               │ │
 │   │   ┌──────────────────────────────────┐ │ │
 │   │   │ Cafe                             │ │ │
 │   │   │   - descricao: "Cafe"            │ │ │
 │   │   │   - custo: R$ 5.00               │ │ │
 │   │   └──────────────────────────────────┘ │ │
 │   │   - adiciona "+ Leite" e + R$ 2.00     │ │
 │   └────────────────────────────────────────┘ │
 │   - adiciona "+ Chocolate" e + R$ 3.00       │
 └──────────────────────────────────────────────┘
Quando você chama pedido.custo(), o objeto exterior (ComChocolate) chama o custo do objeto que está dentro dele (ComLeite), que por sua vez chama o custo do Cafe.
O cálculo viaja de dentro para fora acumulando os valores: $5.00 + 2.00 + 3.00 = 10.00$.
Dessa forma, o seu código fica completamente protegido. Quer adicionar um novo ingrediente?
Basta criar uma única classe nova herdando de DecoradorBebida. As bebidas base nem sabem que os adicionais existem.



#Saida Esperada#
=== Cafeteria ===
Escolha o drink base:
1 - Cafe       (R$ 5.00)
2 - Cha        (R$ 4.00)
3 - Cappuccino (R$ 7.00)
4 - Suco       (R$ 6.00)

Drink: 1
Drink escolhido: Cafe (R$ 5.00)

Agora escolha os adicionais:
1 - Leite               (+ R$ 2.00)
2 - Chocolate           (+ R$ 3.00)
3 - Chantilly           (+ R$ 2.50)
4 - Caramelo            (+ R$ 1.50)
5 - Canela              (+ R$ 0.00)
6 - Sem Acucar          ( R$ 0.00)
0 - Finalizar pedido

Pedido atual: Cafe
Total parcial: R$ 5.00
Adicional: 6
Adicionado: Sem Acucar (R$0.00)

Pedido atual: Cafe (Sem Acucar)
Total parcial: R$ 5.00
Adicional: 2
Adicionado: Chocolate

Pedido atual: Cafe (Sem Acucar) + Chocolate
Total parcial: R$ 8.00
Adicional: 0

=== Pedido Final ===
Descricao: Cafe (Sem Acucar) + Chocolate
Total:     R$ 8.00
