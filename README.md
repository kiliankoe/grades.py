### Noten Fetcher für die HTW Dresden

Als erstes in der ```noten.sh``` die erste Zeile ändern und euer persönliches cwd eintragen.

Wichtig: Es wird Python 3 benötigt. 

Folgende Befehle nacheinander ausführen:

```
python3 -m venv venv
source venv/bin/activate
pip install requests
deactivate
```

Danach in der Daten ```auth``` s-Nummer und RZLogin eingeben und speichern. (Datei muss angelegt werden!) 
Dann kann mittels ```./noten.sh``` nachgeschaut werden, ob es neue Noten gibt. (Am besten einen Cronjob anlegen)

Damit die Push Notifications an das iPhone geschickt werden können, braucht ihr noch einen Account bei https://www.pushbullet.com . Dort dann auf eher Bild rechts oben klicken und unter Account Settings den Access Token kopieren und in der noten.py am Anfang austauschen.
