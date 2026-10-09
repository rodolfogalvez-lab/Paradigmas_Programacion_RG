# "Constructor": crea y devuelve un pokemon
def crear_pokemon(param_nombre, param_tipo, param_hp, param_ad):
    pokemon = {
        'nombre': param_nombre.capitalize(),
        'tipo': param_tipo,
        'hp': param_hp,
        'ad': param_ad
    }
    return pokemon


# Equivalente a __repr__
def info_pokemon(pokemon):
    info_text = f'\n{pokemon["nombre"].capitalize()} | HP: {pokemon["hp"]}'
    return info_text


# Equivalente al método damage
def damage(pokemon, hp_lost):
    pokemon['hp'] = pokemon['hp'] - hp_lost


# Equivalente al método attack
def attack(atacante, rival):

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
