# RegisterDynIpUpdater
Questo progetto utilizza il framework Python Selenium per automatizzare l'aggiornamento del DNS sul sito Register.it. Il codice si connette al sito Web, effettua il login con le credenziali fornite e accede alla sezione di gestione del DNS per modificare i record esistenti.

Questo progetto è utile per coloro che devono effettuare frequenti modifiche al loro DNS e vogliono automatizzare il processo per risparmiare tempo. Il codice è ben documentato e facile da seguire, rendendolo accessibile anche a utenti con conoscenze limitate di programmazione.

Per utilizzare questo progetto, sarà necessario installare Selenium e alcune dipendenze, oltre a disporre di un account Register.it attivo e di credenziali valide

Il programma riconoscerà in automatico quando l'ip è cambiato, la prima volta che verrà eseguito si eseguirà senza fare nessun controllo. 

ALLERTA SPOILER
NON SONO UN PROGRAMMATORE - SE AVETE SUGGERIMENTI SUL MIGLIORAMENTO DEL CODICE CONTRIBUITE :)
## Progetto di aggiornamento DNS con Python Selenium
Questo progetto utilizza il framework Python Selenium per automatizzare l'aggiornamento del DNS sul sito Register.it.
### Requisiti
* Un account Register.it attivo e credenziali valide
* Python 3.x installato sul sistema
* Pip3 installato sul sistema
* Browser Web compatibile con Selenium (es. Google Chrome o Mozilla Firefox)
### Installazione
1. Clona questo repository sul tuo sistema
```
git clone https://github.com/lorenzotarchi/RegisterDynIpUpdater.git
```
2. Installa le dipendenze necessarie con pip3
```
pip3 install -r requirements.txt
```
3. Scarica il driver per il browser Web [Chromedriver](https://chromedriver.chromium.org/) e posizionalo nella cartella del progetto.

### Utilizzo
Prima di utilizzare il programma dovremo andare a modificare il file, inserendo io campi corretti, il file dovra essere modificato alle seguenti line
* 24 per Email register.it
* 25 per Password register.it
* 34 per Nome dominio *
#### Utenti windows
Una volta modificato il file avvieremo il programma con python3 :
```
python3 regi-DnsUpdater-Windows.py
```
#### Utenti Linux
Per gli utenti linux il programma si avviera in modalita nascosta se si vuol vedere il browser modificare la linea 73 mettendo visible=100.
```
python3 regi-DnsUpdater-Linux.py
```
### Automatizzare il propgramma
Comandi per automatizzare il tutto in background.
#### Utenti Linux
Ogni 30 minuti esegue lo script.

Anche in questo caso dovranno essere modificate le path del file e del file "RegisterDynIpUpdater.log"
```
crontab -e

*/30 * * * * export DISPLAY=:0 && export PATH=$PATH:/usr/local/bin && /usr/bin/python3 /home/PC/regi-DnsUpdater-Linux.py >> /home/PC/RegisterDynIpUpdater.log 2>&1
```
#### Utenti Windows
Per gli utenti Windows sarà necessario aprire il programma "Utilità di pianificazione (Windows Task Scheduler)" e configurare una nuova attività.
Potrebbe essere utile a questo punto disabilitare la visualizzazione della scheda chrome del programma aggiungendo un comando sotto la linea 14

```
chrome_options.add_argument('headless')
```
