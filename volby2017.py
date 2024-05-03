"""
Třetí projekt do Engeto Online Python Akademie.

Author: Petr Podolinský
Email: podolinsky.petr@gmail.com
Discord: Petr P. (podolinsky.petr)

SCRAPER VÝSLEDKŮ VOLEB DO PSP ČR ve dnech 20.10. - 21.10.2017
====================================================================
Pomocí tohoto programu je možné extrahovat výsledky parlamentních
voleb do PSP konaných v roce 2017, a to pro vybraný okres z
URL adresy - např. pro okres Frýdek-Místek:
https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102

Knihovny použité v kódu jsou uložené v souboru requirements.txt.

Soubor volby2017.py se spouští z příkazového řádku a je nutné
zadat 2 argumenty <"URL_adresa"> <"vystupni_soubor.csv">.

Struktura výstupního csv souboru (názvy sloupců):
Kód obce / Název obce / Voliči v seznamu / Vydané obálky /
Platné hlasy / dílčí sloupce s počty hlasů (%) pro jednotlivé
kandidující strany.
"""

import bs4
import csv
import requests
import sys


def get_command_line_arguments():
    """Získání argumentů z příkazové řádky."""
    if len(sys.argv) != 3:
        print('Zadán nesprávný počet argumentů. Ke spuštění je nutné zadat: '
              'python volby2017.py "URL_adresa" "vystupni_soubor.csv"')
        quit()
    return sys.argv[1], sys.argv[2]


def get_parsed_html(url):
    """Získání parsovaného HTML ze zadané adresy."""
    response = requests.get(url).text
    print("ZÍSKÁVÁM DATA Z URL:", url)
    return bs4.BeautifulSoup(response, 'html.parser')


def get_villages_data(html):
    """Získání dat o jednotlivých obcích."""
    villages = []
    ids = []
    links = []
    villages_search = html.find_all("td", "overflow_name")
    ids_search = html.find_all("td", "cislo")
    links_search = html.find_all("td", "cislo", "href")
    for village, id, link in zip(villages_search, ids_search, links_search):
        villages.append(village.text)
        ids.append(id.text)
        links.append(
            f"https://volby.cz/pls/ps2017nss/{link.find('a')['href']}"
            )
    return villages, ids, links


def get_parties(html):
    """Získání seznamu kandidujících stran."""
    parties = []
    party_search = html.find_all("td", "overflow_name")
    for party in party_search:
        parties.append(party.text)
    return parties


def get_voters_sum(html):
    """Získání informací o voličích."""
    voters = [
        v.text.replace('\xa0', ' ') for v in html.find_all("td", headers="sa2")
        ]
    attendance = [
        a.text.replace('\xa0', ' ') for a in html.find_all("td", headers="sa3")
        ]
    valid_ones = [
        c.text.replace('\xa0', ' ') for c in html.find_all("td", headers="sa6")
        ]
    return voters, attendance, valid_ones


def get_votes(html):
    """Získání volebních výsledků."""
    votes = []
    for row in html.find_all("tr")[1:]:
        row_votes = [
            v.text.strip() + ' %' for v in row.find_all(
                "td", class_="cislo", headers=["t1sb4", "t2sb4"]
                )
            ]
        votes.append(row_votes)
    return votes


def write_to_csv(file, header, rows):
    """Zápis dat do CSV souboru."""
    with open(file, 'w', newline='') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(header)
        f_writer.writerows(rows)


def election2017(link, file):
    """Hlavní funkce pro zpracování volebních dat."""
    try:
        html = get_parsed_html(link)
        villages, ids, village_links = get_villages_data(html)
        voters, attendance, valid_ones = [], [], []
        for village_link in village_links:
            village_html = get_parsed_html(village_link)
            v, a, vo = get_voters_sum(village_html)
            voters.extend(v)
            attendance.extend(a)
            valid_ones.extend(vo)
        header = [
            'Kód obce', 'Název obce',
            'Voliči v seznamu',
            'Vydané obálky', 'Platné hlasy'
            ]
        parties = get_parties(get_parsed_html(village_links[0]))
        header.extend(parties)
        rows = []
        for village, id, v, a, vo, v_link in zip(
            villages, ids, voters, attendance,
            valid_ones, village_links
                ):
            row = [id, village, v, a, vo]
            votes = get_votes(get_parsed_html(v_link))
            for vote in votes:
                row.extend(vote)
            rows.append(row)
        print("UKLÁDÁM DATA DO SOUBORU:", file)
        write_to_csv(file, header, rows)
        print("KONEC SCRAPOVÁNÍ - UKONČUJI BĚH PROGRAMU:", sys.argv[0])
    except IndexError:
        print("Nastala chyba. Možná máte špatný odkaz nebo \
              některý z argumentů není zapsán v uvozovkách."
              )
        quit()


if __name__ == '__main__':
    address, file_name = get_command_line_arguments()
    election2017(address, file_name)
