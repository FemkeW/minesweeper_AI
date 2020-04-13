import pyautogui, random
geenBommen = []
bommen = []
grenzen_veld = None
eerste_keer = True

def regels(w, y):
        global bommen, geenBommen
        for x in y:
                vlaggenOmGetal = list(pyautogui.locateAllOnScreen('vlag.png', region=(x[0]-30, x[1]-30, 90, 90)))
                legeTegelsOmGetal = list(pyautogui.locateAllOnScreen('tegel.png', region=(x[0]-30, x[1]-30, 90, 90)))

                #als het aantal vlaggen om een tegel gelijk is aan het getal van de tegel, zijn de resterende tegels om het getal geen bommen
                if len(vlaggenOmGetal) == int(w) and len(legeTegelsOmGetal) > 0:
                        for x in legeTegelsOmGetal:
                                if x not in geenBommen:
                                        geenBommen.append(x)

                #als het aantal onaangeklikte tegels om een tegel gelijk is aan het getal van de tegel min het aantal vlaggen dat al om de tegel staat, zijn de resterende tegels om het getal bommen
                if len(legeTegelsOmGetal) == (int(w) - len(vlaggenOmGetal)):
                        for x in legeTegelsOmGetal:
                                if x not in bommen:
                                        bommen.append(x)

def clickRandom(): #wordt uitgevoerd als de lijsten bommen en geenBommen leeg zijn
        global grenzen_veld
        tegels = list(pyautogui.locateAllOnScreen('tegel.png',  region = (grenzen_veld[0], grenzen_veld[1], grenzen_veld[2], grenzen_veld[3])))
        newGame = list(pyautogui.locateOnScreen('Newgame.png'))
        random_tegel = random.choice(tegels)
        pyautogui.moveTo(x=random_tegel[0], y=random_tegel[1])
        pyautogui.click()
        play()

def whatToClick():
        global bommen, geenBommen
        if not bommen and not geenBommen:
                clickRandom()
        else:
                for x in bommen:
                        pyautogui.moveTo(x=x[0], y=x[1])
                        pyautogui.click(button='right') #met de rechtermuisknop selecteer je een vlag (markeer je een tegel als bom)
                        bommen = [] #de lijsten bommen en geenBommen worden geleegd als alles is aangeklikt

                for y in geenBommen:
                        pyautogui.moveTo(x=y[0], y=y[1])
                        pyautogui.click() #met de linkermuisknop klik je een tegel aan om te onthullen wat daaronder zit (als dat een bom blijkt te zijn, ben je af)
                        geenBommen = []
                play()

def play(): #het detecteren van tegels en welke er aan moeten worden geklikt
        global eerste_keer, grenzen_veld
        if eerste_keer: #de eerste beurt wordt vastgesteld waar op het scherm het speelveld zich bevindt, zodat het programma steeds daar zoekt in plaats van het hele scherm af te moeten gaan
            veld = list(pyautogui.locateAllOnScreen('tegel.png'))
            grenzen_veld = [veld[0][0], veld[0][1], veld[-1][0]-veld[0][0]+30, veld[-1][1]-veld[0][1]+30]
            print(grenzen_veld)
            eerste_keer = False
            clickRandom() #de eerste keer is er nog niks bekend en moet je sowieso willekeurig iets aanklikken
        #de onderstaande regels code detecteren eerst bijvoorbeeld alle enen, tweeën... enzovoorts en passen daarna daarop de regels toe om te kijken of er tegels al bommen of geen bommen kunnen worden vastgesteld
        #als er van dat bepaalde getal geen blijken te zijn, worden de regels daarvan niet uitgevoerd, maar gaat het programma tegels aanklikken volgens de regels
        #dit gaat ervan uit dat in de meeste gevallen bij een bepaald getal de getallen daaronder ook allemaal aanwezig zijn in het veld
        #dit zal niet altijd opgaan, maar op deze manier werkt het programma een stuk sneller, want het bespaart een hoop nutteloos zoeken naar getallen die er niet zijn
        enen = list(pyautogui.locateAllOnScreen('1.png', region = (grenzen_veld[0], grenzen_veld[1], grenzen_veld[2], grenzen_veld[3])))
        if not enen:
                clickRandom()
        regels(1, enen)
        tweeën = list(pyautogui.locateAllOnScreen('2.png', region = (grenzen_veld[0], grenzen_veld[1], grenzen_veld[2], grenzen_veld[3])))
        if not tweeën:
                whatToClick()
        regels(2, tweeën)
        drieën = list(pyautogui.locateAllOnScreen('3.png', region = (grenzen_veld[0], grenzen_veld[1], grenzen_veld[2], grenzen_veld[3])))
        if not drieën:
                whatToClick()
        regels(3, drieën)
        vieren = list(pyautogui.locateAllOnScreen('4.png', region = (grenzen_veld[0], grenzen_veld[1], grenzen_veld[2], grenzen_veld[3])))
        if not vieren:
        		whatToClick()
        regels(4, vieren)
        vijven = list(pyautogui.locateAllOnScreen('5.png', region = (grenzen_veld[0], grenzen_veld[1], grenzen_veld[2], grenzen_veld[3])))
        if not vijven:
        		whatToClick()
        regels(5, vijven)
        zessen = list(pyautogui.locateAllOnScreen('6.png', region = (grenzen_veld[0], grenzen_veld[1], grenzen_veld[2], grenzen_veld[3])))
        if not zessen:
        		whatToClick()
        regels(6, zessen)
        zevens = list(pyautogui.locateAllOnScreen('7.png', region = (grenzen_veld[0], grenzen_veld[1], grenzen_veld[2], grenzen_veld[3])))
        if not zevens:
        		whatToClick()
        regels(7, zevens)
        achten = list(pyautogui.locateAllOnScreen('8.png', region = (grenzen_veld[0], grenzen_veld[1], grenzen_veld[2], grenzen_veld[3])))
        if not achten:
        		whatToClick()
        regels(8, achten)
        whatToClick()

#het programma begint met spelen nadat je op 'g' hebt geklikt
bleh = input()
if bleh == 'g':
        play()
