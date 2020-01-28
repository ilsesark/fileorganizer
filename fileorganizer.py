#!/usr/bin/python3

import shutil
import os
from datetime import datetime
import time



def tarkista_ajanhetki():
    '''
    tarkista tämänhetkinen aika
    :return: aika muotoa %H:%M
    '''
    ajankohta = datetime.now()
    aika = ajankohta.strftime("%H:%M")

    return aika


def siirra_tiedostot(lahde, kohde):
    '''
    Siirtää yhden tiedoston (lahde) toiseen kansioon (kohde)
    :param lahde kertoo siirrettävän tiedoston tiedostopolun
    :param kohde kertoo kohdekansion tiedostopolun
    '''

    shutil.move(lahde, kohde)


def maaraaKansionNimi(vnu, knu):
    '''
    Luo uuden merkkijonon annetun vuoden ja kuukauden perusteella
    :format 2019_12_joulukuu
    :return kansion nimi
    '''
    # d = datetime.today()
    kuukaudet = ["tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu",
                 "syyskuu", "lokakuu", "marraskuu", "joulukuu"]
    vuosi = vnu
    kuukaudenNumero = knu
    kuukaudenNimi = kuukaudet[int(knu) - 1]
    return "{v}_{kNu}_{kNi}".format(v=vuosi, kNu=kuukaudenNumero, kNi=kuukaudenNimi)


def leikkaa(n):
    '''Leikkaa annetusta merkkijonosta vuoden ja kuukauden
    :return vuosi
    :return kuukausi
    '''
    paivamaara = n.split("_")[1]
    vuosi = paivamaara[:4]
    kuukausi = paivamaara[4:6]
    return vuosi, kuukausi


def main(lahde, kohde):

    # listataan lahteen kaikki tiedostot
    tiedostot = os.listdir(lahde)

    # vaihdetaan tämän hetkinen kansio kohdekansioksi
    os.chdir(kohde)

    # käydään läpi kaikki lahdekansion tiedostot
    for x in tiedostot:

        # tulostetaan käsiteltävän tiedoston nimi
        print("Olaan kohteessa {}".format(x))

        tiedostonnimi = x

        # määritellään tiedoston nimen perusteella sen kohdekansio
        vuosi, kuukausi = leikkaa(tiedostonnimi)
        kansionNimi = (maaraaKansionNimi(vuosi, kuukausi))

        # siirrä tiedostoNimi -tiedosto kansioon kansionNimi

        # jos tiedostolle ei ole vielä olemassa oikean nimistä kansiota, luodaan sellainen
        if not os.path.exists(kansionNimi):
            os.mkdir(kansionNimi)

        # siirretään käsiteltävä tiedosto oikeaan kansioon
        uusiKohde = kohde + "/" + kansionNimi
        siirra_tiedostot(lahde + "/" + tiedostonnimi, uusiKohde)


if __name__ == '__main__':
    '''Läpi käytävät lähdekansiot sekä vastaavat kohdekansiot'''

    lahteet = ["/media/ELEMENTS/FI9900P_00626E9235BE/record",
               "/media/ELEMENTS/FI9900P_00626E944B61/record",
               "/media/ELEMENTS/FI9900P_00626E944B51/record",
               "/media/ELEMENTS/FI9900P_00626E9235BE/snap",
               "/media/ELEMENTS/FI9900P_00626E944B61/snap",
               "/media/ELEMENTS/FI9900P_00626E944B51/snap"]

    kohteet = ["/media/ELEMENTS/ARKISTO/ETUOVI/record",
               "/media/ELEMENTS/ARKISTO/TAKAOVI/record",
               "/media/ELEMENTS/ARKISTO/VARASTO/record",
               "/media/ELEMENTS/ARKISTO/ETUOVI/snap",
               "/media/ELEMENTS/ARKISTO/TAKAOVI/snap",
               "/media/ELEMENTS/ARKISTO/VARASTO/snap"]

    # käydään läpi tiedostot ohjelman käynnistyessä
    for indeksi in range(0, len(lahteet)):
        main(lahteet[indeksi], kohteet[indeksi])

    # siirretään tiedostot kerran päivässä keskiyön jälkeen
    while True:
        if tarkista_ajanhetki() == "00:01":
            for indeksi in range(0, len(lahteet)):
                main(lahteet[indeksi], kohteet[indeksi])
        else:
            time.sleep(60)





