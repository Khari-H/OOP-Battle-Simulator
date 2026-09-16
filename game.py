from goblin import Goblin
from hero import Hero


ARENA_NAME = " THE OOGOLY BOOGOLY ARENAAAA!"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

    if hero.is_alive():
        print(f"{hero.name} wins")
    else:
        print(f"{enemy.name} wins")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Mr. Sparkles")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Mrs. Sparkles")

    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")
    print("Aye yoo where everybody at??.")

    lady = Hero("Lady Butterfingers")
    print(f"{lady.name} enters the arena")
    
    heroAttack = lady.attack()
    goblin.take_damage(heroAttack)
    

    battle(lady, goblin)




if __name__ == "__main__":
    main()
