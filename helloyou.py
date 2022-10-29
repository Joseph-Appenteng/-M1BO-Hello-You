import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
yes = ["Y", "y", "yes", "ja", "Ja"]
no = ["N", "n", "no", "nee", "Nee"]


required = ("Gebruik alleen A of B")
only = ("Ja of nee>>>")

def intro():
 print("Je bent een 19-jarige burger van Syrië genaamd Ahmad en je woont samen met je 15-jarige broer genaamd Mostafa in Syrië. "
 "Helaas stierven uw ouders tijdens de voortdurende burgeroorlog tussen demonstranten die ontevreden waren over de hoge niveaus "
 "van werkloosheid, wijdverspreide corruptie en gebrek aan politieke vrijheid, maar de Syrische regering gebruikt geweld om "
 "demonstraties te onderdrukken, waarbij ze uitgebreid gebruik maakt van politie, leger en "
 "paramilitaire troepen. Jullie deden allebei hard om een huis te krijgen en probeerden te overleven. "
 "Je kreeg een huis en had wat eten bij jullie. Helaas duurde dat niet lang omdat de burgeroorlog "
 "erger werd op het punt dat onschuldige mensen werden gedood door het leger. Jij en je broer "
 "besluiten om veilig in je huis te blijven en niet naar buiten te gaan. Voor een tijdje moeten jullie "
 "buiten en wat boodschappen halen, want elk eten in huis is klaar. Jij en jij broer maken bespraken "
 "over wie naar buiten moet om boodschappen te doen omdat het voor jullie beiden niet veilig is. "
 "Omdat je de oudere broer bent, bepaal je of jullie allebei naar buiten gaan voor de boodschappen "
 "of alleen jij omdat je je jongere broer niet in gevaar wilt brengen. Kies of je allebei of alleen naar "
 "buiten gaat voor de boodschappen...? ")

 time.sleep(2)
 print(""" A. Alleen.
 B. Jullie beiden.""")
 choice =  input(">>> ")

 if choice in answer_A:
    option_alleen()
 elif choice in answer_B:
    option_beiden()
 else:
  print(required)
  intro()

def option_alleen():
 print("Je besluit dat je zelf gaat omdat het te riskant zou zijn voor jou en broer en je het je niet kunt "
 "veroorloven om een van je liefdesliefde opnieuw te verliezen. Dus je zegt tegen je broer dat hij thuis "
 "moet blijven en nergens heen moet gaan. Naar buiten gaan is te riskant om zonder wapen te gaan, "
 "dus je besluit of je met het pistool die je uit de kledingkast van je ouders hebt gehaald of dat je "
 "ongewapend naar buiten gaat en het pistool voor je broer achterlaat. ")

 time.sleep(2)
 print(""" A. Ga ongewapend naar buiten.
 B. Ga naar buiten met een geweer.""")
 choice =  input(">>> ")

 if choice in answer_A:
    option_ongewapend()
 elif choice in answer_B:
    option_geweer()
 else:
  print(required)
  option_alleen()

def option_beiden():
 print("Je besluit om met je broer naar buiten te gaan omdat hij buiten behulpzaam kan zijn als jullie gevaar "
 "lopen. Jullie namen alles dat jullie nodig hebben mee naar buiten, inclusief het pistool. Helaas zijn "
 "er geen open winkels in de buurt van uw huis waar het veiliger en handiger is. Dus jullie besluiten "
 "om verder te lopen en hopelijk een open winkel te vinden om de boodschappen te halen. Gelukkig "
 "komen jullie een winkel tegen. Jij en je broer haasten zich naar binnen en krijgen alles wat jullie "
 "nodig hadden. Nadat jullie alles hebben gekregen wat jullie allemaal nodig hebben, heb je niet "
 "genoeg geld voor de hele boodschappen omdat je tijdens de oorlog al lang niet meer hebt gewerkt "
 "en je broer geen geld heeft omdat hij 15 is en niet werkt. Dus, wat doe je... ")

 time.sleep(2)
 print(""" A. Probeer met de boodschappen te rennen zonder te betalen.
 B. Betaal voor de boodschappen die al uw geld zich kan veroorloven.""")
 choice =  input(">>> ")

 if choice in answer_A:
    option_steal()
 elif choice in answer_B:
    option_pay()
 else:
  print(required)
  option_beiden()

def option_ongewapend():
 print("Je gaat ongewapend naar buiten in de hoop dat het pistool dat je bij Mostafa hebt achtergelaten "
 "hem kan helpen als er iets ergs gebeurt. Helaas zijn er twee jonge aanvallers die van de oorlog "
 "hebben geprofiteerd om vooral mensen te beroven die alleen buiten lopen. Zodra je ze tegenkomt, "
 "vertellen ze je om al het geld dat je bij je hebt in te leveren en aan hen te geven. Wat doe je in dit "
 "moment......? ")
 
 time.sleep(2)
 print(""" A. Ren zo snel mogelijk terug naar je huis.
 B. Probeer ze te bestrijden.""")
 choice =  input(">>> ")

 if choice in answer_A:
    option_run()
 elif choice in answer_B:
    option_bestrijden()
 else:
  print(required)
  option_ongewapend()

def option_geweer():
 print("Je gaat alleen maar gewapend naar buiten. Helaas zijn er twee jonge aanvallers die van de oorlog "
 "hebben geprofiteerd om vooral mensen te beroven die alleen buiten lopen. Zodra je ze tegenkomt, "
 "vertellen ze je om al het geld dat je bij je hebt in te leveren en aan hen te geven. Wat voor werk doe "
 "je......? ")
 
 time.sleep(2)
 print(""" A. Trek je pistool en hopen dat ze in paniek weglopen.
 B. Ren zo snel mogelijk terug naar je huis.""")
 choice =  input(">>> ")

 if choice in answer_A:
    option_pistool()
 elif choice in answer_B:
    option_rennen()
 else:
  print(required)
  option_geweer()

def option_steal():
 print("Jij en Mostafa beslissen met de boodschappen weg rennen zonder te betalen. Zoals verwacht, jaagt "
 "de eigenaar van de winkel jullie op en haalt jullie in. Hij kwam voorbereid en trok een pistool naar "
 "jou en Mostafa. Wat doe je nu...? ")

 time.sleep(2)
 print(""" A. Trek je pistool uit om hem af te schrikken.
 B. Geef de boodschappen op.""")
 choice =  input(">>> ")

 if choice in answer_A:
    option_threat()
 elif choice in answer_B:
    option_opgeven()
 else:
  print(required)
  option_steal()

def option_boat():
 print("Voor een tijdje de oorlog erger wordt, militairen beginnen te infiltreren in huizen van mensen. "
 "Gelukkig kwam je er tijdens het luisteren naar de radio achter dat vluchtelingen met bootjes naar "
 "Europa gaan om een veilige plek te vinden om te wonen. Dus jij en Mostafa kwamen met een plan "
 "om naar de kust te gaan waar de vluchtelingen veilig kampeerden en hopelijk op een boot naar een "
 "van de landen in Europa te stappen. Jij en je broer pakten alles in en begonnen aan de Reis. Jullie "
 "slaagden erin de kust te bereiken waar de vluchtelingen kampeerden. Daar waren drie boten, maar "
 "men was al aan het varen. De eerste was overbelasting met jongeren, terwijl de tweede vol zat met "
 "gezinnen. Welke boot kiezen jij en Mostafa ...? ")

 time.sleep(2)
 print(""" A. De derde boot.
 B. De tweede boot.""")
 choice =  input(">>> ")

 if choice in answer_A:
    option_derde()
 elif choice in answer_B:
    option_tweede()
 else:
  print(required)
  option_boat()

def option_pay():
 print("Je betaalt voor de boodschappen die je je kon veroorloven, en jullie gaan veilig thuis.")
 option_boat()

def option_pistool():
 print("Zodra je je pistool tevoorschijn haalde, werden ze bang en begonnen ze weg te vluchten. Je gaat "
 "boodschappen doen en je betaalde voor de boodschappen die je je kon veroorloven omdat je geen "
 "problemen wilde en je veilig thuiskwam. ")
 option_boat()

def option_rennen():
 print("Je besloot zo snel mogelijk naar je huis te rennen, maar ze probeerden je ook te achtervolgen. "
 "Gelukkig haastte je je terug naar huis en deed je snel de deur dicht. You riep dat je een pistool hebt, "
 "dus ze moeten je huis verlaten. Nu zie je ze weglopen van angst. Je gaat dan de volgende dag met je "
 "broer naar buiten voor de boodschappen die nu goed uitgerust zijn inclusief het geweer. Je betaalt "
 "voor de boodschappen die je je kon veroorloven omdat je geen problemen wilde en jullie veilig "
 "thuiskwamen. ")
 option_boat()

def option_bestrijden():
 print("Je probeert ze te bestrijden , maar helaas had een van de jongens een mes en stak je maag en ze "
 "renden weg met je geld. Je begint te bloeden , maar niemand was er om je te helpen. Je bent "
 "overleden door bloedverlies! ")
 time.sleep(2)
 only1()
def only1():
 print("Wil je nog een keer proberen?")
 choice = input("Ja of Nee>>>")

 if choice in yes:
  intro()
 elif choice in no:
  print("Bedankt voor deelname")
 else:
  print(only)
  only1()

def option_run():
 print("Je besloot zo snel mogelijk naar je huis te rennen, maar de aanvallers probeerden je ook te "
 "achtervolgen. Gelukkig ben je naar huis gekomen en je doet snel de deur dicht. Je krijgt nu het "
 "pistool van je broer en je riep dat je nu een pistool hebt, dus ze moeten je huis verlaten. Nu zie je ze "
 "weglopen van angst. Je gaat de volgende dag met je broer naar buiten voor de boodscahappen die "
 "nu goed uitgerust zijn inclusief het geweer. Je betaalt voor de boodschappen die je je kon "
 "veroorloven omdat je geen problemen wilde en jullie veilig thuiskwamen. ")
 option_boat()

def option_threat():
 print("Zodra je je pistool trok, raakte de eigenaar in paniek en schoot hij je broer neer. Je schoot de man "
 "neer en ging snel naar beneden om je broer vast te houden terwijl hij bloed verloor. Je schreeuwde "
 "om hulp, maar geen antwoord. Je legde toen je broer te ruste, betuigde je respect en probeerde "
 "verder te gaan. Een tijdje wordt de oorlog erger, militairen beginnen nu te infiltreren in huizen van "
 "mensen. Gelukkig kwam je er tijdens het luisteren naar de radio achter dat vluchtelingen met "
 "bootjes naar Europa gaan om een veilige plek te vinden en om te wonen. Dus je kwam met een plan "
 "om naar de kust te gaan waar de vluchtelingen veilig kampeerden en hopelijk op een boot naar een "
 "van de landen in Europa te stappen. Je pakte alles in en begon aan de reis. Je wist de kust te "
 "bereiken waar de vluchtelingen kampeerden. Daar waren drie boten, maar men was al aan het "
 "varen. De tweede boot was overbelasting met jongeren, terwijl de derde vol gezinnen zat. Welke "
 "boot kies je....? ")

 time.sleep(2)
 print(""" A. De tweede boot.
 B. De derde boot.""")
 choice =  input(">>> ")

 if choice in answer_A:
    option_tweede1()
 elif choice in answer_B:
    option_derde1()
 else:
  print(required)
  option_threat()

def option_opgeven():
 print("Je hebt de boodschappen opgegeven om verder problemen te voorkomen en jij en je broer "
 "proberen een andere winkel voor boodschappen te vinden. Gelukkig komen jullie een nieuwe "
 "winkel tegen en deze keer betaal je voor de boodschappen die je geld zich kan veroorloven. Jij en "
 "Mostafa komen veilig thuis. ")
 option_boat()

def option_derde():
 print("Jij en Mostafa besluiten op de derde boot te stappen, maar je moet wachten tot de tweede boot "
 "vaart. Na een kort moment zag je de tweede boot beginnen te zinken. Een deel van de vluchtelingen "
 "zwom terug voor de laatste boot. Ze kregen hulp van enkele vluchtelingen op de laatste boot. Aan "
 "de andere kant verdronk helaas de hoeveelheid vluchteling die besloot naar de reeds gevaren eerste "
 "boot te zwemmen omdat de boot te ver weg was. De boot gaat eindelijk varen. Er was gelukkig eten "
 "op de boot, dus jij en Mostafa waren er zeker van dat jullie het zouden overleven. Na de lange reis "
 "kwamen jullie eindelijk aan op de bestemming. Jij en Mostafa stappen uit de boot en jullie zijn "
 "erachter gekomen dat jullie in Nederland zijn. Jullie zijn toen naar het asielcentrum gebracht waar "
 "jullie nu een tijdje zullen wonen. Jij en Mostafa hebben de psycholoog leren kennen en jullie beiden "
 "hebben vrede gehad met al dat trauma. Jij en je broer kregen ook de hulp die jullie nodig hadden. "
 "Jij en Mostafa zijn als broers naar Amsterdam verhuisd en leven gelukkig na. ")
 time.sleep(2)
 good()
def good():
 print("Gefeliciteerd! Je hebt het Goede Einde.")
 print("Wil je nog een keer proberen?")
 choice = input("Ja of Nee>>>")

 if choice in yes:
  intro()
 elif choice in no:
  print("Bedankt voor deelname")
 else:
  print(only)
  good()

def option_tweede():
 print("Jij en Mostafa besluiten op de tweede boat te stappen maar helaas op nog geen lange afstand van "
 "de wal begon de boot te zinken door de overbelasting van de boot. Alle vluchtelingen op de boot "
 "begonnen terug te zwemmen naar de kust of naar de reeds gevaren derde boot. Door de drukte van "
 "de vluchtelingen in het water kon je niet vinden waar je broer naartoe ging. Je begon terug te "
 "zwemmen naar de kust voor de laatste boot. Je kreeg hulp van enkele vluchtelingen in de laatste "
 "boot. Je begon in paniek te roepen om je broer, maar geen antwoord. De boot gaat eindelijk varen. "
 "Er was gelukkig eten op de boot, dus je wist zeker dat je het zou overleven. Tijdens de reis kwam je "
 "erachter dat je broer geholpen werd van de andere boot, maar die boot ging naar Duitsland in plaats "
 "van waar je naartoe ging. Na de lange reis kwam je aan op de bestemming. Je stapt uit de boot en je "
 "komt erachter dat je in Nederland bent. Je bent toen naar het asielcentrum gebracht waar je nu een "
 "tijdje gaat wonen. Je maakte kennis met de psycholoog en je geest werd gerustgesteld door al dat "
 "trauma. Alles ging goed zoals je wilde en je begon eindelijk je leven in Amsterdam te leiden, "
 "wetende dat je op een dag naar Duitsland zult gaan om je lang verloren broer te vinden. ")
 time.sleep(2)
 bruh()
def bruh():
 print("Je hebt het Normaal einde!")
 print("Wil je nog een keer proberen?")
 choice = input("Ja of Nee>>>")

 if choice in yes:
  intro()
 elif choice in no:
  print("Bedankt voor deelname")
 else:
  print(only)
  bruh()

def option_tweede1():
 print("Je besluit op de tweede boot te stappen maar helaas op nog geen lange afstand van de wal begint "
 "de boot te zinken door de overbelasting van de boot. Steedsweer begonnen vluchtelingen naar de "
 "kust of naar de reeds bevaren derde boot. Wat doe jij....? ")

 time.sleep(2)
 print(""" A. Swim terug naar de kust voor de laatste boot.
 B. Probeer te zwemmen om de reeds gevaren boot in te halen.""")
 choice =  input(">>> ")

 if choice in answer_A:
    option_nice()
 elif choice in answer_B:
    option_dead()
 else:
  print(required)
  option_tweede1()

def option_derde1():
 print("Je besluit op de derde boot te stappen, maar je moet wachten tot de tweede boot gaat varen. Even "
 "later zag je de tweede boot beginnen te zinken. Een deel van de vluchtelingen zwom terug voor de "
 "laatste boot. Ze kregen hulp van enkele vluchtelingen op de laatste boot. Aan de andere kant "
 "verdronk helaas de hoeveelheid vluchtelingen die besloot naar de reeds gevaren eerste boot te "
 "zwemmen omdat de boot te ver weg was. De boot gaat eindelijk varen. Er lag gelukkig eten op de "
 "boot, dus je wist zeker dat je het zou overleven. Na de lange reis ben je op de plaats van "
 "bestemming. Je stapt uit de boot en je gaat er achter komen dat je in Nederland bent. Je bent toen "
 "naar het asielcentrum gebracht waar je nu een tijdje gaat wonen. Je gaa tnaar de psycholoog en je "
 "geest werd gerustgesteld door al dat trauma. Je hebt ook de hulp gekregen die je nodig hebt. Alles "
 "ging goed zoals je wilde, maar diep van binnen haat je jezelf omdat je je broer niet kunt redden. ")
 time.sleep(2)
 ok()
def ok():
 print("Je hebt het slechte einde")
 print("Wil je nog een keer proberen?")
 choice = input("Ja of Nee>>>")

 if choice in yes:
  intro()
 elif choice in no:
  print("Bedankt voor deelname")
 else:
  print(only)
  ok()

def option_nice():
 print("Je begon terug te zwemmen naar de kust voor de laatste boot. Je kreeg hulp van enkele "
 "vluchtelingen in de laatste boot. De boot gaat eindelijk varen. Er was gelukkig eten op de boot, dus "
 "je wist zeker dat je het zou overleven. Na de lange reis kwam je aan op de bestemming. Je stapt uit "
 "de boot en je komt erachter dat je in Nederland bent. Je bent toen naar het asielcentrum gebracht "
 "waar je nu een tijdje gaat wonen. Je maakte kennis met de psycholoog en je geest werd "
 "gerustgesteld door al dat trauma. Je kreeg ook de hulp die je nodig had. Alles ging goed zoals je "
 "wilde, maar diep van binnen haat je jezelf omdat je je broer niet kunt redden. ")
 time.sleep(2)
 ok()

def option_dead():
 print("Je probreet te zwemmen om de reeds gevaren boot in te halen, maar helaas had je geen "
 "uithoudingsvermogen meer omdat die boot zo ver weg was. Je begon te verdrinken en je stierf!. ")
 time.sleep(2)
 bad()
def bad():
 print("Je bent dood!")
 print("Wil je nog een keer proberen?")
 choice = input("Ja of Nee>>>")

 if choice in yes:
  intro()
 elif choice in no:
  print("Bedankt voor deelname")
 else:
  print(only)
  bad()
intro()