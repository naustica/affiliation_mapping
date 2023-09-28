#!/usr/bin/python

import pandas as pd
import sys

filename = sys.argv[1]
new_filename = sys.argv[2]

df = pd.DataFrame()

if '.xlsx' in filename:
    df = pd.read_excel(filename)
elif '.csv' in filename:
    df = pd.read_csv(filename)
else:
    raise ValueError("Extension must be .xlsx or .csv")

# Fakultät für Agrarwissenschaften
agrar = ['phytopathol', 'anim', 'trop\w* plant',
         'crop', 'palynol', 'soil', 'plant',
         'plant sci', 'agr', 'farming', 'witzenhausen', 'rural', 'tier[aä]r']
# Fakultät für Biologie und Psychologie
biol = ['microbiol', 'biosci', 'biomol',
        'psychol', 'zool', 'anthropol', 'neurosci', 'biol',
        'biodivers', 'mikrobiol',
        'behav\w* ecol', 'blumenbach', 'albrecht[-\s]von', 'veget']
# Fakultät für Chemie
chem = ['chem', 'organische und biomolekulare', 'tammann']
# Fakultät für Forstwissenschaften und Waldökologie
forst = ['forest', 'wood', 'bioclimatol', 'wald(?!weg)', 'wildlife', 'sust\w* land', 'silvicult']
# Fakultät für Geowissenschaften und Geographie
geo = ['geo(?:l|g|wiss|biol|sci|chem|gra)+', 'landscape ecol', 'mineral']
# Fakultät für Mathematik und Informatik
math = ['comput', 'informat', 'comp\w* sci', 'math', 'comp.* sec.*', 'dig\w* hum']
# Fakultät für Physik
phys = ['phys*(?![a-z])', 'physi[ck]', 'friedrich[-\s]hund', 'hund p', 'astrophys', 'complex systems']
# Juristische Fakultät
jur = ['law', 'polit', 'jur', 'derecho']
# Sozialwissenschaftliche Fakultät
soz = ['soc\w* sci', 'sozialw', 'erziehungsw', 'demokr', 'so[cz]iol']
# Wirtschaftswissenschaftliche Fakultät
bwl = ['econ', 'volkswirt', 'wirtsch', 'asian business', 'financ',
       'sieben 3', 'stat', '(?!agri)busin', 'stat\w* lear',
       '[ck]onsum', 'logist']
# Philosophische Fakultät
phil = ['histor', 'musicol', 'roman', '[eä]gyptol',
        'moritz[-\s]stern', 'philo', 'archä', 'kultur[aw]',
        'germanis', 'german st', 'geschi', 'asienk', 's[kc]and', 'lingu', 'sprachw']
# Theologische Fakultät
theo = ['theol', 'kirchen', 'religio']
# Universitätsmedizin
med = ['umg', 'oncol', 'med', 'cardiol', 'clin', 'pneumol', 'klini',
       'multiscale bioimaging', 'cardiovasc',
       'urol', 'gastroenter', 'surg', 'physio', 'psychia',
       'dent', 'pathol', 'radiol', 'adv.* imag', 'heilkunde',
       '\w*klin', 'robert[-\s]koch', 'hosp', 'otorhinolaryngol', 'otolaryngol',
       'immu', 'pharma[ck]ol', 'ophthal', 'rheuma']
# Centre for Modern Indian Studies (CeMIS)
cemis = ['indian', 'cemis']
# SUB
sub = ['sub(?![a-z])', 'library']
# Courant Forschungszentrum "Armut, Ungleichheit und Wachstum in Entwicklungsländern"
courfz_armut = ['poverty']
# Lichtenberg-Kolleg
licht = ['lichtenberg']
# GWDG
gwdg = ['datenverarbeitung', 'gwdg']
# Max-Planck-Einrichtungen
planck = ['icasec', 'dynam\w* [ck]ompl', 'nonlin', 'energy', 'max[-\s]planck']
# Leibniz Deutsches Primatenzentrum
dpz = ['primate']
# Center for Integrated Breeding Research (CiBreed)
cibreed = ['int\w* breeding']
# Campus-Institut Data Science (CIDAS)
cidas = ['cidas', 'inst\w* data sci']
# Zentrum für Statistik
ctrstat = ['cent.* stat']
# Drittmittelprojekte
drittm = ['coll\w* res', 'sfb', 'sonderforsch']

df_adress = df[['item_id', 'doi', 'family_name', 'given_name', 'address_full']].copy()

df_adress.loc[df_adress['address_full'].str.contains('|'.join(drittm), case=False, regex=True),
              ['fakultaet']] = 'Drittmittelprojekte' # am Anfang, sodass bei Mehrfachangabe Zuordnung zu Fak.
df_adress.loc[df_adress['address_full'].str.contains('|'.join(dpz), case=False, regex=True),
              ['fakultaet']] = 'Deutsches Primatenzentrum' # am Anfang, sodass bei Mehrfachangabe Zuordnung zu Fak.
df_adress.loc[df_adress['address_full'].str.contains('|'.join(cibreed), case=False, regex=True),
              ['fakultaet']] = 'Center for Integrated Breeding Research' # am Anfang, sodass bei Mehrfachangabe Zuordnung zu Fak.
df_adress.loc[df_adress['address_full'].str.contains('|'.join(agrar), case=False, regex=True),
              ['fakultaet']] = 'Fakultät für Agrarwissenschaften'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(biol), case=False, regex=True),
              ['fakultaet']] = 'Fakultät für Biologie und Psychologie'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(chem), case=False, regex=True),
              ['fakultaet']] = 'Fakultät für Chemie'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(forst), case=False, regex=True),
              ['fakultaet']] = 'Fakultät für Forstwissenschaften und Waldökologie'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(phys), case=False, regex=True),
              ['fakultaet']] = 'Fakultät für Physik'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(theo), case=False, regex=True),
              ['fakultaet']] = 'Theologische Fakultät'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(phil), case=False, regex=True),
              ['fakultaet']] = 'Philosophische Fakultät'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(jur), case=False, regex=True),
              ['fakultaet']] = 'Juristische Fakultät'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(soz), case=False, regex=True),
              ['fakultaet']] = 'Sozialwissenschaftliche Fakultät'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(bwl), case=False, regex=True),
              ['fakultaet']] = 'Wirtschaftswissenschaftliche Fakultät'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(math), case=False, regex=True),
              ['fakultaet']] = 'Fakultät für Mathematik und Informatik'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(geo), case=False, regex=True),
              ['fakultaet']] = 'Fakultät für Geowissenschaften und Geographie'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(cemis), case=False, regex=True),
              ['fakultaet']] = 'Centre for Modern Indian Studies (CeMIS)'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(courfz_armut), case=False, regex=True),
              ['fakultaet']] = 'Courant Forschungszentrum "Armut, Ungleichheit und Wachstum in Entwicklungsländern"'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(licht), case=False, regex=True),
              ['fakultaet']] = 'Lichtenberg-Kolleg'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(gwdg), case=False, regex=True),
              ['fakultaet']] = 'Gesellschaft für wiss. Datenverarbeitung mbH Göttingen'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(sub), case=False, regex=True),
              ['fakultaet']] = 'Nds. Staats- und Universitätsbibliothek'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(cidas), case=False, regex=True),
              ['fakultaet']] = 'Campus-Institut Data Science (CIDAS)'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(ctrstat), case=False, regex=True),
              ['fakultaet']] = 'Zentrum für Statistik'
df_adress.loc[df_adress['address_full'].str.contains('|'.join(planck), case=False, regex=True),
              ['fakultaet']] = 'Max-Planck-Einrichtungen' # nach phys!
df_adress.loc[df_adress['address_full'].str.contains('|'.join(med), case=False, regex=True),
              ['fakultaet']] = 'Universitätsmedizin' # unbedingt am Ende!


df_adress.to_csv(new_filename, index=False)
