volume = int(input("Gib hier dein Volume ein"))
if volume < 20:
    print("Das ist etwas leise.")
elif 20 <= volume < 40:
    print("Das ist gut für Hintergrund-Musik.")
elif 40 <= volume < 60:
    print("Perfekt, ich kann alle Details hören.")
elif 60 <= volume < 80:
    print("Gut für Partys.")
elif 80 <= volume < 100:
    print("Etwas laut!")
else:
    print("Mir tun die Ohren weh! :(")
