### Noten Fetcher für die HTW Dresden

`auth_example.json` duplizieren und in `auth.json` umbenennen. Dort Login (sNummer) und Passwort eintragen. Falls
Push-Notifications verschickt werden sollen müssen die Daten für entweder Pushover oder Pushbullet auch eingetragen
werden.

Es empfiehlt sich ein virtualenv (`$ python3 -m venv venv`) anzulegen und in diesem (`$ source venv/bin/activate`) die
nötigen dependencies zu installieren (`$ pip install -r requirements.txt`).

![screenshot](https://cloud.githubusercontent.com/assets/2625584/21504443/57b799c0-cc5f-11e6-9f34-454a1bf2b55d.png)

Startet man das Skript mit `-p` oder `--push` wird die Tabelle aller Noten nicht ausgegeben, aber für das Tool noch
unbekannte (sprich neue) Noten werden an den Pushprovider weitergereicht. Ist demnach ideal für einen Cronjob.

```
*/15 * * * * /pfad/zum/verzeichnis/noten.sh > /dev/null 2>&1
```
