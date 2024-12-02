class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp = actual_damage
        print(f"{self.name}이 (가) {actual_damage}의 피해를 입었습니다. 남은 HP: {self.hp}")
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name}이(가) 사망했습니다.")

    def is_alive(self):
        return self.hp >0

    def __str__(self):
        return (f"Name: {self.name}, HP: {self.hp}, Attack: {self.attack}, Denfense: {self.defense}")

class Hero(Character):
    def __init__(self, name, hp, attack, defense, role):
        super(). __init__ (name, hp, attack, defense)
        self.role = role
        self.exp = 0

    def gain_exp(self, amount):
        """경험치를 얻습니다."""
        self.exp += amount
        print(f"{self.name}이(가) {amount}의 경험치를 얻었습니다. 총 경험치: {self.exp}")

    def special_attack(self):
        """특수 공격 실행"""
        special_damage = self.attack *2
        print(f"{self.name}이(가) 특수 공격을 실행합니다! {special_damage}의 데미지!")
        return  special_damage

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Role: {self.role}, EXP: {self.exp}"

class Monster(Character):
    def __init__(self, name, hp, attack, denfense, species):
        super(). __init__ (name, hp, attack, denfense)
        self.species = species

    def special_ability(self):
        return self.attack * 1.5

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Species: {self.species}"

class Battle:
    @staticmethod
    def fight(hero, monster):
        print(f"전투 시작! {hero.name}이(가) {monster.name}(와) 싸웁니다.")
        print("영웅 선공!")

        turn = 0
        while hero.is_alive() and monster.is_alive():
            print(f"==턴 {turn}==")

            damage = monster.take_damage(hero.attack)
            print(f"{hero.name}이(가) {monster.name}에게 {damage}의 데미지를 입힙니다.")
            if not monster.is_alive():
                print("몬스터 죽음")
                hero.gain_exp(10)
                print(f"{hero.name}가 경험치 10 획득!")
                return
            damage = monster.take_damage(hero.attack)
            print(f"{monster.name}이(가) {hero.name}에게 {damage}의 데미지를 입힙니다.")
            if not hero.is_alive():
                print(f"히어로 죽음")
                return