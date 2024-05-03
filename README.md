**SCRAPER VÝSLEDKŮ VOLEB DO PSP ČR ve dnech 20.10. - 21.10.2017**

Pomocí tohoto programu "volby2017.py" je možné extrahovat výsledky parlamentních voleb do PSP konaných v roce 2017, a to pro vybraný okres z URL adresy - jako příklad funkcionality kódu byl zvolen okres Frýdek-Místek, pro který jsou data dostupná z této adresy: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102. Soubor "volby2017.py" se spouští z příkazového řádku a je nutné zadat 2 argumenty <"URL_adresa"> <"vystupni_soubor.csv">, přičemž pro zápis těchto argumentů je nutné použít uvozovky - ukázka průběhu: 

C:\Users\Příjmení\Desktop\ENGETO složka\PROJEKTY\projekt_3\projekt_3_web-scraping> python volby2017.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102" "okres_frydek-mistek.csv"

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598011&xvyber=8102

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598020&xvyber=8102

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=511633&xvyber=8102

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598038&xvyber=8102

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598046&xvyber=8102

                                     (… dalších 62 záznamů…)

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=554928&xvyber=8102

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=552488&xvyber=8102

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=552682&xvyber=8102

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=552691&xvyber=8102

ZÍSKÁVÁM DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=568163&xvyber=8102

                                    (… celkem 72 záznamů…)

UKLÁDÁM DATA DO SOUBORU: okres_frydek-mistek.csv
KONEC SCRAPOVÁNÍ - UKONČUJI BĚH PROGRAMU: volby2017.py

Doprovodné soubory: - "requirements.txt" s pročištěným seznamem knihoven; - "okres_frydek-mistek.csv" s vygenerovanými výsledky voleb.

Struktura výstupního csv souboru - ukázka pro první tři obce:
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Česká národní fronta,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
598011,Baška,3 093,2 065,2 053,"8,52 %","0,04 %","0,04 %","6,03 %","0,04 %","2,38 %","9,35 %","1,02 %","0,58 %","1,02 %","0,04 %","0,00 %","10,52 %","0,00 %","0,00 %","2,14 %","32,39 %","0,09 %","0,43 %","9,44 %","0,04 %","0,77 %","0,34 %","0,14 %","14,27 %","0,24 %"
598020,Bílá,285,178,178,"10,67 %","0,00 %","0,00 %","7,86 %","0,00 %","5,61 %","11,79 %","1,68 %","0,56 %","0,00 %","0,56 %","0,00 %","6,74 %","0,56 %","0,00 %","1,68 %","29,21 %","0,00 %","0,00 %","8,42 %","0,00 %","1,68 %","0,00 %","0,00 %","12,92 %","0,00 %"
511633,Bocanovice,358,197,197,"10,15 %","0,00 %","0,00 %","16,24 %","0,00 %","1,52 %","6,59 %","1,52 %","0,50 %","0,00 %","0,00 %","0,00 %","9,13 %","0,00 %","0,50 %","0,50 %","22,84 %","0,00 %","0,00 %","21,82 %","0,00 %","0,00 %","0,00 %","0,00 %","8,62 %","0,00 %"
