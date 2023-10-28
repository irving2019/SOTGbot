from locations import *
from person import *
from armors import *
from guns import *


class Groups:
    def __init__(self, name, friends, neutrals, enemies, outfit, location, armor, guns):
        self.name = name
        self.friends = friends
        self.neutrals = neutrals
        self.enemies = enemies
        self.outfit = outfit
        self.location = location
        self.guns = guns


# Группировки:
Single_Group = "Вольные сталкеры"
Military_Group = "Военные"
Freedom_Group = "Свобода"
Duty_Group = "Долг"
Monolit_Group = "Монолит"
Clear_sky_Group = "Чистое небо"
Sin_Group = "Грех"
Bandit_Group = "Бандиты"
Renegade_Group = "Ренегаты"
Awarenes_Group = "Осознание"
Scientist_Group = "Учёные"
Mercenaries_Group = "Наёмники"
Zombie_Group = "Зомби"
Mutant_Group = "Мутанты"
Merchant_Group = "Торговцы"
