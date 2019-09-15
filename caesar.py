# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from string import ascii_uppercase


buchstaben = ascii_uppercase


def beautify(botschaft):
    ''' Bereitet eine Botschaft für die Verschlüsselung vor '''
    return botschaft.upper()

def brute_force(botschaft, buchstaben=buchstaben):
    ''' Versucht eine verschlüsselte Botschaft mittels
    Brute-Force-Methode (Methode der rohen Gewalt) zu entschlüsseln,
    d. h. hier: Alle Möglichkeiten werden ausprobiert.
    
    Funktion zur Veranschaulichung!'''
    for i in range(1, 26):
        print("{:2d}".format(i), decode(botschaft, i, buchstaben))

def decode(geheim_botschaft, verschiebung, buchstaben=buchstaben):
    ''' Entschlüsselt eine Geheimbotschaft. '''
    verschiebung = -verschiebung
    return encode(geheim_botschaft, verschiebung, buchstaben)

def encode(botschaft, verschiebung, buchstaben=buchstaben, beautify_flag=True):
    ''' Verschlüsselt eine Botschaft. '''
    geheim_botschaft = []
    if beautify_flag:
        botschaft = beautify(botschaft)
    for zeichen in botschaft:
        if zeichen not in buchstaben:
            geheim_botschaft.append(zeichen)
        else:
            position = buchstaben.index(zeichen) + verschiebung
            if position >= len(buchstaben):
                position -= len(buchstaben)
            geheim_botschaft.append(buchstaben[position])
    return "".join(geheim_botschaft)


if __name__ == "__main__":

    botschaft = "Der Lehrer denkt nach."
    verschiebung = 2

    print("Originale Nachricht: ", botschaft)

    # Verschlüsseln    
    geheim_botschaft = encode(botschaft, verschiebung)
    print("Codierte Nachricht:  ", geheim_botschaft)

    # Entschlüsseln
    print("Decodierte Nachricht:", decode(geheim_botschaft, verschiebung))

    # Angriff mittels Brute-Force-Methode,
    # d. h. alle Möglichkeiten werden ausgetestet
    print("-" * 70)
    print("Beispiel für einen Brute-Force-Angriff")
    print("-" * 70)
    brute_force(geheim_botschaft, buchstaben)
