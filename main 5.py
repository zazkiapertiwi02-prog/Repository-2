class Hero:
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

        Hero.jumlah += 1

    def siapa(self):
        return f"{self.name} memiliki power {self.power}"

    def healthUp(self, up):
        self.health += up

    def getHealth(self):
        return self.health


# Membuat objek hero
hero1 = Hero("Sniper", 100, 10, 5)
hero2 = Hero("Axe", 200, 15, 0)

# Menampilkan informasi hero
print(hero1.siapa())
print(hero2.siapa())

# Mengubah armor Sniper
hero1.armor = 10
print(f"Armor {hero1.name} = {hero1.armor}")

# Menampilkan jumlah hero
print(f"Jumlah hero = {Hero.jumlah}")

# Menambah health Sniper
hero1.healthUp(20)

# Menampilkan health setelah ditambah
print(f"Health {hero1.name} = {hero1.getHealth()}")
print(f"Health {hero2.name} = {hero2.getHealth()}")


# Contoh method dengan parameter dan return
def serang(self, target):
    return f"{self.name} menyerang {target}"
