import time # importing time module
import pyautogui # importing pyautogui


pyautogui.FAILSAFE = True


def sichere_abfrage (text, datentyp, bedingung = None): 
    #       bedingung = None
    #       Erklärung:  Wenn keine bedingung übergeben> OHNE None> Fehlermeldung
    #                   Wenn keine bedingung übergeben> MIT None> Fehlermeldung wird nicht ausgegeben, da None bei if-Abfragen als False gewertet wird, dadurch wird die if-Abfrage übersprungen
    #                   Wenn bedingung übergeben> bedingung ist eine Funktion> "PLATZHALTER" Nonen wird zu True da eine Funktion vorhanden ist> if-Abfrage> bedinung> true
    """
    Fragt den Benutzer nach einer Eingabe und überprüft, ob sie dem angegebenen Datentyp entspricht.
    bedingung = None ist durch das None schon festgelegt, dadurch muss es nicht als Übergabeparameter angegeben werden, wenn keine Bedingung benötigt wird.


    Übergabeparameter:
    text: float
    datentyp: type
    bedingung: function (optional)


    Rückgabewert:
    Gibt die gültige Eingabe des Benutzers zurück, die dem angegebenen Datentyp entspricht und optional die Bedingung erfüllt.


    Beispiel:
    age = sichere_abfrage("Geben Sie Ihr Alter ein: ", int, lambda x: x > 0)
    In diesem Beispiel wird der Benutzer aufgefordert, sein Alter einzugeben. Die Funktion überprüft, ob die Eingabe eine positive ganze Zahl ist.
    """

    while True:
        try:
            eingabe = datentyp(input(text))

            if bedingung and not bedingung(eingabe):
                #               "and" da für "or" die if-Abfrage immer true wäre, sobald eine Bedingung übergeben wird, unabhängig von Ausgabe bedingung(eingabe)
                # Erklärung:    bedingung führt keine Arbeit aus sondern schaut ob bei bedinung ein Werkzeug vorhanden ist, wenn ja = True wenn None = False

                # Fall:         bedingung nicht übergeben > bedingung ist None > None wird bei if-Abfragen als False gewertet > if-Abfrage wird übersprungen
                # Fall:         bedingung übergeben > bedingung ist eine Funktion > wenn die Funktion mit der Eingabe als Argument False zurückgibt,
                #               wird die Fehlermeldung ausgegeben und die Schleife von vorne gestartet
                # Fall:         bedingung übergeben > bedingung ist eine Funktion > wenn die Funktion mit der Eingabe als Argument True zurückgibt,
                #               wird die eingabe zurückgegeben und die Schleife verlassen
                print("Ungültige Eingabe (Bedingung nicht erfüllt).")
                continue

            return eingabe
        

        except ValueError:
            print(f"Fehler: Das war kein gültiger {datentyp.__name__}. Bitte erneut versuchen.")
            


try:

    T = sichere_abfrage("How many seconds do you want to wait before sending each message?\nEnter 0.1 for the quickest sending!\n", float, lambda x: x>0) # Desired Time before sending each messages
    text = input("Type the message you want to send as text BOMBING! :  \n") # Desired Text
    printing = sichere_abfrage("How many times do you want to send the message?\n", int, lambda x: x>0) # How many messages the user want to send
    counter_switch = str(input("Do you want to use the counter? (y/n)\n")).lower() # Counter switch to decide whether to include the counter in the message or not


    i = 0
    antwort = pyautogui.confirm(text="Confirm here to start the script", title="Answer", buttons=["OK", "Cancel"])
    if antwort == "OK":
        for i in range(0, printing):
            time.sleep(T) # will wait T times before sending each automated message
            if counter_switch == "y":
                pyautogui.typewrite(f"{i+1} ") # will write the counter number
            pyautogui.typewrite(text) # will write the text the user want
            pyautogui.press('enter') # will work as the 'Enter' button


    else:
        print("Script stopped by the user.")


except pyautogui.FailSafeException:
    print("\nNOT-AUS: Programm durch Bewegung in die Ecke gestoppt.")