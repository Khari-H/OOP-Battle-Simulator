from goblin import Goblin
from hero import Hero

ARENA_NAME = "Oogoly Boogoly Squad!"


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
    print(f"{lady.name} enters the arena with {lady.health} health")
    
    heroAttack = lady.attack()
    goblin.take_damage(heroAttack)

    goboAttack = goblin.attack()
    lady.take_damage(goboAttack)
    






if __name__ == "__main__":
    main()
