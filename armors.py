class Armor: #dfgdfb
    def __init__(self, name, fire_protection, kick_protection, lighting_protection, tear_protection,
                 radioactive_defence, acid_protection, boom_protection, bullet_protection,
                 weight, pnv, artefacts_conteiners, carryable_weight, wear):
        self.name = name  # Имя
        self.fire_protection = fire_protection  # защита от огня
        self.kick_protection = kick_protection  # защита от ударов
        self.lighting_protection = lighting_protection  # защита от электричества
        self.tear_protection = tear_protection  # защита от разрывов
        self.radioactive_defence = radioactive_defence  # защита от радиации
        self.acid_protection = acid_protection  # защита от кислоты
        self.boom_protection = boom_protection  # защита от взрывов
        self.bullet_protection = bullet_protection  # защита от пуль
        self.weight = weight  # Вес брони
        self.pnv = pnv  # ПНВ
        self.artefacts_containers = artefacts_conteiners  # контейнеры для артефактов
        self.carryable_weight = carryable_weight  # переносимый вес
        self.wear = wear  # износ


leather_jacket = Armor("Кожаная куртка", 10, 10, 10, 10, 0, 10, 10, 10, 3, 0, 0, 30, 0)
bandit_jacket = Armor("Бандитская куртка", 10, 10, 10, 15, 0, 10, 10, 15, 3, 0, 0, 30, 0)
mercenary_jumpsuit = Armor("Комбинезон наёмника", 30, 20, 30, 30, 3020, 20, 25, 20, 5, 0, 0, 40, 0)
jumpsuit_zarya = Armor("Комбинезон Заря", 50, 50, 50, 40, 50, 50, 30, 30, 5, 1, 2, 40, 0, )
dolg_jumpsuit = Armor("ПС3-9д \"Броня долга\"", 50, 50, 50, 50, 50, 50, 40, 40, 5, 1, 1, 40, 0)
light_freedom_jumpsuit = Armor("Комбинезон \"Ветер Сободы\"", 30, 50, 50, 30, 50, 50, 25, 30, 3, 0, 1, 35, 0)
guardian_freedom_jumpsuit = Armor("Комбинезон \"Страж свободы\"", 50, 60, 50, 50, 50, 50, 45, 40, 6, 1, 2, 40, 0)
monolith_jumpsuit = Armor("Комбинезон Монолита", 50, 50, 60, 40, 50, 50, 40, 40, 5, 1, 2, 40, 0)
ssp_99_ekolog = Armor("ССП-99 Эколог", 90, 50, 90, 15, 90, 90, 40, 20, 4, 1, 5, 30, 0)
ssp_99_m = Armor("ССП-99М", 90, 50, 90, 50, 90, 90, 60, 40, 7, 1, 5, 40, 0)
ps3_9md = Armor("ПС3-9Мд", 80, 50, 90, 50, 90, 70, 50, 40, 9, 1, 2, 40, 0)
seva = Armor("Сева", 80, 50, 90, 50, 90, 70, 50, 40, 9, 1, 2, 40, 0)
berill5m = Armor("Берилл-5м", 30, 20, 30, 40, 30, 30, 40, 45, 7, 1, 2, 60, 0)
army_armor = Armor("Армейский бронекостюм", 60, 80, 70, 70, 70, 50, 70, 55, 12, 1, 3, 70, 0)
exoskeleton = Armor("Экзоскелет", 50, 90, 50, 80, 30, 50, 80, 60, 15, 1, 2, 100, 0)
