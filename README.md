### Noten Fetcher für die HTW Dresden

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
