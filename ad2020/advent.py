class player():
    def __init__(self):
        self.hp=100
        self.attack=0
        self.defence=0

    def reset(self):
        self.hp = 100
        self.attack = 0
        self.defence = 0
class monster():
    def __init__(self,hp,attack,defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence

        self.full_hp=hp

    def reset(self):
        self.hp = self.full_hp

class item():
    def __init__(self,name,cost,damage,armor):
        self.name=name
        self.cost=cost
        self.damage=damage
        self.armor=armor



def kup_itemy(min_cost,p,m):
    for w in weapons:
        p.reset()
        m.reset()
        cost=0
        p.attack+=w.damage
        cost+=w.cost
        if sim_fight(p,m):
            if cost>min_cost:
                min_cost=cost
        for a in armor:
            p.reset()
            m.reset()
            cost = 0
            p.attack += w.damage
            cost += w.cost
            p.defence+=a.armor
            cost+=a.cost
            if sim_fight(p, m):
                if cost > min_cost:
                    min_cost = cost
            for r in rings:
                p.reset()
                m.reset()
                cost = 0
                p.attack += w.damage
                cost += w.cost
                p.defence += a.armor
                cost += a.cost
                p.attack += r.damage
                p.defence += r.armor
                cost += r.cost
                if sim_fight(p, m):
                    if cost > min_cost:
                        min_cost = cost
                for r2 in rings:
                    if r2.name!= r.name:
                        p.reset()
                        m.reset()
                        cost = 0
                        p.attack += w.damage
                        cost += w.cost
                        p.defence += a.armor
                        cost += a.cost
                        p.attack += r.damage
                        p.defence += r.armor
                        cost += r.cost
                        p.attack += r2.damage
                        p.defence += r2.armor
                        cost += r2.cost
                        if sim_fight(p, m):
                            if cost > min_cost:
                                min_cost = cost
    for w in weapons:
        p.reset()
        m.reset()
        cost=0
        p.attack+=w.damage
        cost+=w.cost
        for r in rings:
            p.reset()
            m.reset()
            cost = 0
            p.attack += w.damage
            cost += w.cost
            p.defence+=r.armor
            p.attack+=r.damage
            cost+=r.cost
            if sim_fight(p, m):
                if cost > min_cost:
                    min_cost = cost
            for r2 in rings:
                if r2.name != r.name:
                    p.reset()
                    m.reset()
                    cost = 0
                    p.attack += w.damage
                    cost += w.cost
                    p.attack += r.damage
                    p.defence += r.armor
                    cost += r.cost
                    p.attack += r2.damage
                    p.defence += r2.armor
                    cost += r2.cost
                    if sim_fight(p, m):
                        if cost > min_cost:
                            min_cost = cost


    print(min_cost)

def sim_fight(p,m):
    nr_tury=1
    while p.hp>0 and m.hp>0:
        print("Tura "+str(nr_tury))
        if m.defence>p.attack:
            m.hp-=1
            print("The player deals "+str(1)+" damage; the boss goes down to "+str(m.hp)+" hit points." )
        else:
            m.hp=m.hp-p.attack+m.defence
            print("The player deals " + str(p.attack)+"-"+str(m.defence)+"=" +str(p.attack-m.defence)+ " damage; the boss goes down to " + str(m.hp) + " hit points.")
        if m.hp<=0:
            break
        elif p.defence>m.attack:
            p.hp-=1
            print("The boss deals " + str(1) + " damage; the player goes down to " + str(p.hp) + " hit points.")
        else:
            p.hp = p.hp - m.attack + p.defence
            print(
                "The boss deals " + str(m.attack) + "-" + str(p.defence) + "=" + str(m.attack - p.defence) + " damage; the player goes down to " + str(p.hp) + " hit points.")
        nr_tury+=1
    if p.hp<=0:
        print("Potwór wygrał")
        return True
    else:
        print("Gracz wygrał")
        return False
weapons=[
item("dagger",8,4,0),
item("shortsword",10,5,0),
item("warhammer",25,6,0),
item("longsword",40,7,0),
item("greataxe",74,8,0)
]
armor=[
item("leather",13,0,1),
item("chainmail",31,0,2),
item("chainmail",53,0,3),
item("chainmail",75,0,4),
item("chainmail",102,0,5)
]
rings=[
item("damage+1",25,1,0),
item("damage +2",50,2,0),
item("damage +3",100,3,0),
item("defense +1",20,0,1),
item("defense +2",40,0,2),
item("defense +3",80,0,3)
]
hp=0
attack=0
defence=0
min_cost=0
f=open("adventinput", "r")
for x in f:
    if "Hit Points:" in x:
        hp = x.split()
        hp="".join(hp[2:3])
        hp=int(hp)
    elif "Damage:" in x:
        attack = x.split()
        attack="".join(attack[1:2])
        attack=int(attack)
    elif "Armor:" in x:
        defence = x.split()
        defence="".join(defence[1:2])
        defence=int(defence)
p=player()
m=monster(hp,attack,defence)
kup_itemy(min_cost,p,m)