[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/l0EqxU9O)
# Trabajo Práctico 8


## Ejercicio 1 - Tuplas

Azara y Rui son compañeros de equipo que compiten en una búsqueda del tesoro con temática de piratas.
Uno tiene una lista de tesoros con coordenadas del mapa, el otro una lista de nombres de ubicaciones con coordenadas del mapa.


<br>
<table>
<tr><th>Azara's List</th><th></th><th>Rui's List</th></tr>
<tr><td>

| Treasure                    | Coordinates |
| --------------------------- | ----------- |
| Amethyst Octopus            | 1F          |
| Angry Monkey Figurine       | 5B          |
| Antique Glass Fishnet Float | 3D          |
| Brass Spyglass              | 4B          |
| Carved Wooden Elephant      | 8C          |
| Crystal Crab                | 6A          |
| Glass Starfish              | 6D          |
| Model Ship in Large Bottle  | 8A          |
| Pirate Flag                 | 7F          |
| Robot Parrot                | 1C          |
| Scrimshawed Whale Tooth     | 2A          |
| Silver Seahorse             | 4E          |
| Vintage Pirate Hat          | 7E          |

</td><td></td><td>

| Location Name                         | Coordinates | Quadrant  |
| ------------------------------------- | ----------- | --------- |
| Seaside Cottages                      | ("1", "C")  | Blue      |
| Aqua Lagoon (Island of Mystery)       | ("1", "F")  | Yellow    |
| Deserted Docks                        | ("2", "A")  | Blue      |
| Spiky Rocks                           | ("3", "D")  | Yellow    |
| Abandoned Lighthouse                  | ("4", "B")  | Blue      |
| Hidden Spring (Island of Mystery)     | ("4", "E")  | Yellow    |
| Stormy Breakwater                     | ("5", "B")  | Purple    |
| Old Schooner                          | ("6", "A")  | Purple    |
| Tangled Seaweed Patch                 | ("6", "D")  | Orange    |
| Quiet Inlet (Island of Mystery)       | ("7", "E")  | Orange    |
| Windswept Hilltop (Island of Mystery) | ("7", "F")  | Orange    |
| Harbor Managers Office                | ("8", "A")  | Purple    |
| Foggy Seacave                         | ("8", "C")  | Purple    |

</td></tr>
</table>

<br>


Pero las cosas están un poco desorganizadas: las coordenadas de Azara parecen estar formateadas y ordenadas de manera diferente a las de Rui, y tienen que seguir mirando de una lista a la otra para averiguar qué tesoros corresponden a qué ubicaciones.
Como son principiantes en Python, han acudido a ti en busca de ayuda para escribir un pequeño programa (en realidad, un conjunto de funciones) para organizar mejor la información de su búsqueda.


### 1.1. Extraer coordenadas
Implementa la función `get_coordinate()` que toma un par `(tesoro, coordenada)` de la lista de Azara y devuelve solo la coordenada del mapa extraída.

```python
>>> get_coordinate(('Scrimshawed Whale Tooth', '2A'))
2A
```
### 1.2. Formatear coordenadas
Implementa la función `convert_coordinate()` que toma una coordenada en el formato `"2A"` y devuelve un par en el formato `("2", "A")`.

```python
>>> convert_coordinate("2A")
("2", "A")
```

### 1.3. Combinar registros

Implementa la función `create_record()` que toma un par `(tesoro, coordenada)` de la lista de Azara 
y un registro `(ubicación, coordenada, cuadrante)` de la lista de Rui,
y devuelve `(tesoro, coordenada, ubicación, coordenada, cuadrante)` si las coordenadas coinciden.
Si las coordenadas no coinciden, devuelve la cadena "no coincide".
Reformatea la coordenada según sea necesario para una comparación precisa.

```python
>>> create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')

>>> create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue'))
"not a match"
```


## Ejercicio 2 - Sets

Tú y tus socios comerciales operan una pequeña empresa de catering. Acaban de acordar organizar un evento para un club de cocina local que presenta platos "favoritos del club". El club no tiene experiencia en la organización de eventos grandes y necesita ayuda con la organización, compra, preparación y servicio. Han decidido escribir algunos pequeños scripts en Python para acelerar todo el proceso de planificación.

### 2.1. Limpiar los ingredientes repetidos del plato
Las recetas del evento se agregaron desde diversas fuentes y parece que los ingredientes tienen entradas duplicadas (o más) -- ¡no quieres terminar comprando elementos en exceso!
Antes de que pueda comenzar la compra y la cocina, la lista de ingredientes de cada plato necesita ser "limpiada".

Implementa la función `clean_ingredients` que tome el nombre de un plato y una lista de ingredientes.

Esta función debería devolver una tupla con el nombre del plato como primer elemento, seguido por el conjunto depurado de ingredientes.

```python
>>> clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])

>>> ('Punjabi-Style Chole', {'garam masala', 'bay leaves', 'ground turmeric', 'ginger', 'garlic paste', 'peppercorns', 'ginger paste', 'red chili powder', 'cardamom', 'chickpeas', 'cumin powder', 'vegetable oil', 'tomatoes', 'coriander powder', 'onions', 'cilantro', 'cloves'})
```


### 2.2 Clasificar Cócteles y Mocktails
El evento incluirá tanto cócteles como "mocktails" - bebidas mezcladas sin alcohol.
Necesitas asegurarte de que las bebidas "mocktail" sean verdaderamente no alcohólicas y que los cócteles realmente incluyan alcohol.

Implementa la función `check_drinks` que tome el nombre de una bebida y una lista de ingredientes.
La función debería devolver el nombre de la bebida seguido de "Mocktail" si la bebida no tiene ingredientes alcohólicos, y el nombre de la bebida seguido de "Cocktail" si la bebida incluye alcohol.
Para los propósitos de este ejercicio, los cócteles solo incluirán alcoholes del set ALCOHOLS en sets_categories_data.py:

```python
>>> from sets_categories_data import ALCOHOLS 

>>> check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'])
...
'Honeydew Cucumber Mocktail'

>>> check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda'])
...
'Shirley Tonic Cocktail'
```
