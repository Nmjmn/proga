# kirjuta vooskeem programmile mis
#
# küsib kasutajalt tema vanust
# tema venna vanust
# tema õe vanust
# arvutab nende keskmise
# ütleb kasutajale nende keskmise vanuse "teie ja teie vendade-õdede keskmine vanus on see:"
# küsib kasutajalt tema ema vanust
# küsib kasutajalt tema isa vanust
# arvutab vanemate keskmise vanuse
# teavitab kasutajat vanemate keskmisest vanusest
# arvutab eelneva kahe tulemuse põhjal kogu perekonna keskmise vanuse

vanus = 0
õevanus = 0
vennavanus = 0
emavanus= 0
isavanus= 0

vanus = int(input("Kui vana teie olete?:"))
õevanus = int(input("Kui vana on teie õde?:"))
vennavanus =  int(input("Kui vana on teie vend?:"))

keskmine = float(vanus+õevanus+vennavanus)/3
print("teie ja teie vendade-õdede keskmine vanus on see:",str(keskmine))

emavanus= int(input("Kui vana on teie ema?:"))
isavanus =int(input("Kui vana on teie isa?:"))

vanemateKeskmine = float(emavanus + isavanus) / 2
print ("Teie vanemate keskmisest vanus on:",str(vanemateKeskmine))

keskmine2 = float(keskmine+vanemateKeskmine)/2
print ("Teie pere keskmine vanus on:",str(keskmine2))