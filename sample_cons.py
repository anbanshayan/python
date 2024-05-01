class tour:
    place=""
    charges=0
    vehicle=""

    def dance():
        print("Let's dance")
    def vibe():
        print("Let's vibe with songs")

anbu=tour()
ashayan=tour()
kuga=tour()
siva=tour()

#bus, train, ship and flighr are objects of class travel

anbu.dance()
ashayan.vibe()
kuga.dance()
siva.vibe()

anbu.place="Dubai"
anbu.charges=10000
anbu.vehicle="Car"

ashayan.place="Kopay"
ashayan.charges=12000
ashayan.vehicle="Bike"

kuga.place="Abu Dhabi"
kuga.charges=10000
kuga.vehicle="Car"

siva.place="Dubai"
siva.charges=10000
siva.vehicle="Car"

print("Sivananthi is going to",siva.place,"to this vacation")
