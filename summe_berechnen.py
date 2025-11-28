
# -*- coding: utf-8 -*-
"""
Erstellt am Donnerstag, 27.11.2025 um 17:34

@author: Quarky

"""

# das ist ein einzeliger Kommentar und wird nicht vom Python-Programm ausgefuehrt 
# er dient nur zur Dokumentation und Erklaerung


'''
FUNKTION 1:

Funktionsdefinition mit zwei Parametern zahl1 und zahl2 (auch Eingabewerte genannt)
Diese Funktion berechnet die Summe aus zahl1 und zahl2, schreibt die 
Ergebniszahl in die Variable "ergebnis" und gibt dieses Ergebnis als 
Funktionsausgabe zurück. Auf diese Weise kann das Ergebnis in einer anderen
Funktion weiterverarbeitet werden. 
''' 
def summe(zahl1, zahl2):

    # Berechnungsvorschrift fuer die Summe der beiden uebergebenen Zahlen
    ergebnis = zahl1 + zahl2

    # Anweisung, um eine Ausgabe auf dem Bildschirm zu erzeugen
    #print("Die Summe von ", zahl1, " und ", zahl2 , "ist gleich ", ergebnis, "\n")

    # Ausgabewert der Funktion
    return ergebnis




'''
FUNKTION 2: 

Funktionsdefinition ohne Parameter und ohne Rueckgabewert

Diese Funktion berechnet die Summe der Zahlen 1 bis 9 mit 5 in einer Schleife
also 1 + 5 = 6, 2 + 5 = 7 und so weiter
Die Zahlen 1, 10 und 5 kann man beliebig selbst veraendern.
'''
def berechne_summen():

    # eine Schleife, die 1 bis 9 Mal ausgefuehrt wird
    for x in range(1, 10):

        # Funktionsaufruf 
        summe(x, 5)



'''
HAUPTFUNKTION

Das ist die Hauptfunktion, der sogenannte Einstiegspunkt in das Python-Programm.
normalerweise werden alle anderen Funktionen aus dieser Main-Funktion aufgerufen
''' 
def main():

    a = 2
    b = 6

    # Funktionsaufruf, der die Summe aus a und b (2+6) berechnet und der 
    # Variablen "ergebnis" zuweist, also in dieser Variablen speichert
    ergebnis = summe(a, b)
    print("Summe von ", a, " und ", b, " ist ", ergebnis, "\n")

    
    # Funktionsaufruf der zweiten oben definierten Funktion
    berechne_summen()



if __name__ == "__main__":
    main()
