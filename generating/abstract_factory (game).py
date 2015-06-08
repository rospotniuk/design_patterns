"""
Реалізація патерну "Абстактна фабрика" для створення воїнів армій людей, ельфів та орків.
Армії включають в себе піхоту, кінноту та лучників.
Люди та ельфи воюють проти орків.
У бій можуть вступати воїни різних профілей, наприклад, лучник і вершник
"""
    # Абстрактні базові класи для різних родів військ
class Warrior(object):
    __was_attacked = 0      # Скільки разів воїн був атакований. Якщо __was_attacked = 2, воїн помирає.
    def __init__(self, name, army, fighting_arm=""):       # fighting_arm - рід військ, army - до якої армії належить
        self._name = name
        self._fighting_arm = fighting_arm
        self._army = army
    def __str__(self):
        return '{} "{}" of {} army'.format(self._fighting_arm, self._name, self._army)
    def attack(self, enemy):
        print('{} attacked {}.'.format(self, enemy))
    def is_wounded(self):       # Воїна поранили в бою
        self.__was_attacked += 1
        if self.__was_attacked == 2:
            print('{} was killed.'.format(self))
            return True

class Infantryman(Warrior):         # Піхотинець
    def __init__(self, name, army):
        Warrior.__init__(self, name, army, fighting_arm='Infantryman')

class Archer(Warrior):              # Лучник
    def __init__(self, name, army):
        Warrior.__init__(self, name, army, fighting_arm='Archer')

class Horseman(Warrior):            # Кавалерія (вершник)
    def __init__(self, name, army):
        Warrior.__init__(self, name, army, fighting_arm='Horseman')

class Wizard(Warrior):              # Чарівник
    def __init__(self, name, army):
        Warrior.__init__(self, name, army, fighting_arm='Wizard')

    # Абстрактна фабрика (описує методи створення воїнів кожного роду військ)
class AbstractWarriorFactory(object):
    def create_infantryman(self):
        raise NotImplementedError
    def create_archer(self):
        raise NotImplementedError
    def create_horseman(self):
        raise NotImplementedError
    def create_wizard(self):
        raise NotImplementedError

    # Фабрика для створення армії людей (Concrete Factory 1)
class PeopleArmyFactory(AbstractWarriorFactory):
    def create_infantryman(self, name):
        return Infantryman(name, army="People")
    def create_archer(self, name):
        return Archer(name, army="People")
    def create_horseman(self, name):
        return Horseman(name, army="People")
    def create_wizard(self, name):
        return Wizard(name, army="People")

    # Фабрика для створення армії орків (Concrete Factory 2)
class OrkArmyFactory(AbstractWarriorFactory):
    def create_infantryman(self, name):
        return Infantryman(name, army="Ork")
    def create_archer(self, name):
        return Archer(name, army="Ork")
    def create_horseman(self, name):
        return Horseman(name, army="Ork")
    def create_wizard(self, name):
        return Wizard(name, army="Ork")

    # Створення армій
    # Фабрика для створення армії ельфів (Concrete Factory 3)
class ElfArmyFactory(AbstractWarriorFactory):
    def create_infantryman(self, name):
        return Infantryman(name, army="Elf")
    def create_archer(self, name):
        return Archer(name, army="Elf")
    def create_horseman(self, name):
        return Horseman(name, army="Elf")
    def create_wizard(self, name):
        return Wizard(name, army="Elf")

    # Testing
if __name__ == "__main__":
    import random

        # Кількість воїнів у кожній армії
    people, elfs, orks = 2, 2, 3
        # Імена воїнів у арміях людей, ельфів та орків відповідно
    people_names = ['Man{}'.format(i) for i in range(1,people+1)]
    elf_names = ['Elf{}'.format(i) for i in range(1,elfs+1)]
    ork_names = ['Ork{}'.format(i) for i in range(1,orks+1)]
        # Створення армій
    def add_warriors(army, warriors_names):
        item, warriors = 0, []
        while item <= len(warriors_names):
            try:
                warriors.append(army.create_infantryman(warriors_names[item]))
                item += 1
            except: break
            try:
                warriors.append(army.create_archer(warriors_names[item]))
                item += 1
            except: break
            try:
                warriors.append(army.create_horseman(warriors_names[item]))
                item += 1
            except: break
            try:
                warriors.append(army.create_wizard(warriors_names[item]))
                item += 1
            except: break
        return warriors

    people_army = add_warriors(PeopleArmyFactory(), people_names)
    elf_army = add_warriors(ElfArmyFactory(), elf_names)
    ork_army = add_warriors(OrkArmyFactory(), ork_names)
    armies = {'People army': people_army, 'Elf army': elf_army, 'Ork army': ork_army}

        # The war
    choose = ''
    while choose != 'exit':
            # Випадковим чином обираємо воїна, який атакує, і того, хто приймає атаку
        warriors = [random.choice(people_army + elf_army), random.choice(ork_army)]
        random.shuffle(warriors)
        first_warrior, second_warrior = warriors
        first_warrior.attack(second_warrior)
        if second_warrior.is_wounded():
            for army in armies.keys():
                if second_warrior in armies[army]:
                    armies[army].pop(armies[army].index(second_warrior))
                    if not armies[army]:
                        print('{} is destroyed.'.format(army))
                        del armies[army]
                        break
        if 'Ork army' not in armies:
            print('People and elfs win!')
            break
        if len(armies) == 1:
            print('{} win!'.format(list(armies.keys())[0]))
            break

        try: choose = input()
        except (TypeError, ValueError): break
