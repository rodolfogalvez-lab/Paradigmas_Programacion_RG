'''
Implementación sin clases.
Cada pokemon se guarda en un diccionario y su comportamiento
se maneja con funciones que reciben ese diccionario.
'''


# "Constructor": crea y devuelve un pokemon
def crear_pokemon(param_nombre: str, param_tipo: str, param_hp: int, param_ad: int) -> dict:
    pokemon = {
        'nombre': param_nombre.capitalize(),
        'tipo': param_tipo,
        'hp': param_hp,
        'ad': param_ad
    }
    return pokemon


# Equivalente a __repr__
def info_pokemon(pokemon: dict) -> str:
    info_text = f'\n{pokemon["nombre"].capitalize()} | HP: {pokemon["hp"]}'
    return info_text


# Equivalente al método damage
def damage(pokemon: dict, hp_lost: int):
    pokemon['hp'] = pokemon['hp'] - hp_lost


# Equivalente al método attack
def attack(atacante: dict, rival: dict):

    if atacante['tipo'] == 'electrico':
        ataque = 'Impactrueno'
    elif atacante['tipo'] == 'planta':
        ataque = 'Hoja navaja'
    elif atacante['tipo'] == 'fuego':
        ataque = 'Llamarada'
    else:
        ataque = 'Cañon de agua'

    damage(rival, atacante['ad'])

    print(f'\n({atacante["nombre"]}) Ataca con {ataque} | -{atacante["ad"]}')