---
type: Table
title: "Asmens — Asmenų pajamų ir gyvenimo sąlygų statistinio tyrimo rezultatai"
description: "Spinta table datasets/gov/lsd/pajamu_ir_gyvenimo_salygos/Asmens (82 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/pajamu_ir_gyvenimo_salygos/Asmens"
tags: [gov, lsd, asmens, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/799/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/pajamu_ir_gyvenimo_salygos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Asmens — Asmenų pajamų ir gyvenimo sąlygų statistinio tyrimo rezultatai

- **Model:** `datasets/gov/lsd/pajamu_ir_gyvenimo_salygos/Asmens`[^manifest]
- **Dataset:** [Lietuvos statistikos departamento namų ūkių bei pavienių asmenų pajamų ir gyvenimo sąlygų...](../pajamu_ir_gyvenimo_salygos.md) (`datasets/gov/lsd/pajamu_ir_gyvenimo_salygos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/pajamu_ir_gyvenimo_salygos/Asmens` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `pb030`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pb030` | `string` | — | `4` | `open` | — | Asmens ID | Statistinio tyrimo subjekto (asmens) unikalus identifikatorius |
| `hb030` | `ref` | [NamuUkis](NamuUkis.md) (`level=4 UUID`: `hb030._id`) | `4` | `open` | — | Namų ūkio ID | Statistinio tyrimo subjekto (namų ūkio) unikalus identifikatorius |
| `rb050` | `number` | — | `3` | `open` | — | Asmens kalibruotasis svoris | — |
| `age` | `integer` | — | `4` | `open` | — | Amžius, sukakęs praeitų metų gruodžio 31 d. | — |
| `rb090` | `string` | — | `4` | `open` | — | Lytis | — |
| `rb220` | `string` | — | `4` | `open` | — | Tėvo (įtėvio, patėvio, globėjo) ID | Statistinio tyrimo subjekto (asmens) tėvo unikalus identifikatorius |
| `rb230` | `string` | — | `4` | `open` | — | Motinos (įmotės, pamotės, globėjos) ID | Statistinio tyrimo subjekto (asmens) motinos unikalus identifikatorius |
| `rb240` | `string` | — | `4` | `open` | — | Sutuoktinio/sugyventinio ID | Statistinio tyrimo subjekto (asmens) sutuoktinio/sugyventinio unikalus identifikatorius |
| `rl010` | `integer` | — | `4` | `open` | — | Valandų, praleistų vaikų lopšelyje ar darželyje, skaičius per savaitę | — |
| `rl020` | `integer` | — | `4` | `open` | — | Valandų, praleistų bendrojo ugdymo mokykloje, skaičius per savaitę | — |
| `rl030` | `integer` | — | `4` | `open` | — | Valandų, praleistų pailgintos dienos grupėje mokykloje, savaitiniame vaikų darželyje, skaičius per savaitę | — |
| `rl040` | `integer` | — | `4` | `open` | — | Valandų, praleistų vaikų dienos ar vaikų užimtumo centre, skaičius per savaitę | — |
| `rl050` | `integer` | — | `4` | `open` | — | Valandų skaičius per savaitę, kai vaiką prižiūri mokama auklė | — |
| `rl060` | `integer` | — | `4` | `open` | — | Valandų skaičius per savaitę, kai vaiką neatlygtinai prižiūri seneliai, kiti šeimos nariai (ne tėvai), giminaičiai, draugai, kaimynai | — |
| `pb190` | `string` | — | `4` | `open` | — | Santuokinė padėtis | — |
| `pb200` | `string` | — | `4` | `open` | — | Sąjunga asmenų susitarimu | — |
| `pe010` | `string` | — | `4` | `open` | — | Ar šiuo metu mokotės? | — |
| `pe020` | `string` | — | `4` | `open` | — | Kur mokotės? (ISCED lygis) | — |
| `pe030` | `date` | `Y` | `4` | `open` | — | Aukščiausio išsilavinimo įgijimo metai | — |
| `pe040` | `string` | — | `4` | `open` | — | Aukščiausias įgytas išsilavinimas (ISCED lygis) | — |
| `ph010` | `string` | — | `4` | `open` | — | Bendra sveikatos būklė | — |
| `ph020` | `string` | — | `4` | `open` | — | Sergate kokia nors lėtine (chroniška) liga arba turite ilgalaikių sveikatos sutrikimų? | — |
| `ph030` | `string` | — | `4` | `open` | — | Veiklos apribojimas dėl sveikatos sutrikimų 6 mėn. ar ilgesnį laikotarpį | — |
| `ph040` | `string` | — | `4` | `open` | — | Nors vienas atvejis, kai negavote medicininės konsultacijos ar gydymo (išskyrus odontologo) per paskutinius 12 mėn. | — |
| `ph050` | `string` | — | `4` | `open` | — | Priežastis, dėl kurios negavote medicininės konsultacijos, gydymo (išskyrus odontologo) | — |
| `ph060` | `string` | — | `4` | `open` | — | Nors vienas atvejis, kai negavote odontologo konsultacijos, gydymo per paskutinius 12 mėn. | — |
| `ph070` | `string` | — | `4` | `open` | — | Priežastis, dėl kurios negavote odontologo konsultacijos, gydymo | — |
| `pl015` | `string` | — | `4` | `open` | — | Ar kada nors turėjote nuolatinį darbą ne trumpiau kaip 6 mėn.? | — |
| `pl020` | `string` | — | `4` | `open` | — | Ar per paskutines 4 savaites ieškojote darbo? | — |
| `pl025` | `string` | — | `4` | `open` | — | Jei rastumėte darbą, ar galėtumėte per artimiausias 2 savaites pradėti dirbti? | — |
| `pl031` | `string` | — | `4` | `open` | — | Ekonominio aktyvumo (veiklos) pobūdis šiuo metu | — |
| `pl040` | `string` | — | `4` | `open` | — | Užimtumo statusas dabartiniame ar paskutiniame pagrindiniame darbe | — |
| `pl050` | `string` | — | `4` | `open` | — | Profesijos kodas (ISCO-88(COM)) | — |
| `pl060` | `integer` | — | `4` | `open` | — | Valandų, praleistų pagrindiame darbe, skaičius per savaitę | — |
| `pl073` | `integer` | — | `4` | `open` | — | Mėnesių, praleistų dirbant samdomą darbą visą darbo dieną, skaičius | — |
| `pl074` | `integer` | — | `4` | `open` | — | Mėnesių, praleistų dirbant samdomą darbą ne visą darbo dieną, skaičius | — |
| `pl075` | `integer` | — | `4` | `open` | — | Mėnesių, praleistų besiverčiant individualia veikla, dirbant šeimos versle visą darbo dieną, skaičius | — |
| `pl076` | `integer` | — | `4` | `open` | — | Mėnesių, praleistų besiverčiant individualia veikla, dirbant šeimos versle ne visą darbo dieną, skaičius | — |
| `pl080` | `integer` | — | `4` | `open` | — | Mėnesių skaičius, kai buvote bedarbiu | — |
| `pl085` | `integer` | — | `4` | `open` | — | Mėnesių skaičius, kai buvote senatvės ar išankstinės senatvės pensininku | — |
| `pl086` | `integer` | — | `4` | `open` | — | Mėnesių skaičius, kai buvote dėl negalios nedirbančiu asmeniu | — |
| `pl087` | `integer` | — | `4` | `open` | — | Mėnesių, praleistų besimokant, studijuojant, skaičius | — |
| `pl088` | `integer` | — | `4` | `open` | — | Mėnesių, praleistų privalomojoje pradinėje karo tarnyboje, skaičius | — |
| `pl089` | `integer` | — | `4` | `open` | — | Mėnesių skaičius, kai buvote namų šeimininku (-e) | — |
| `pl090` | `integer` | — | `4` | `open` | — | Mėnesių skaičius, kai buvote kitu neaktyviu asmeniu | — |
| `pl100` | `integer` | — | `4` | `open` | — | Valandų, praleistų nepagrindiame darbe, skaičius per savaitę | — |
| `pl111` | `string` | — | `4` | `open` | — | Įmonės veiklos kodas ( NACE red. 2) | — |
| `pl120` | `string` | — | `4` | `open` | — | Priežastis, dėl kurios dirbate trumpiau nei 30 valandų per savaitę | — |
| `pl130` | `string` | — | `4` | `open` | — | Darbuotojų skaičius įstaigoje, įmonėje, šeimos versle | — |
| `pl140` | `string` | — | `4` | `open` | — | Dabartinio ar paskutinio pagrindinio darbo sutarties tipas | — |
| `pl150` | `string` | — | `4` | `open` | — | Ar turite pavaldinių dabartiniame pagrindiniame darbe (turėjote paskutiniame pagrindiniame darbe)? | — |
| `py010g` | `number` | — | `2` | `open` | — | Metinės samdomojo darbo pajamos | — |
| `py010n` | `number` | — | `2` | `open` | — | Metinės samdomojo darbo pajamos, atskaičius mokesčius | — |
| `py020g` | `number` | — | `2` | `open` | — | Metinės pajamos iš darbdavio natūra | — |
| `py021g` | `number` | — | `2` | `open` | — | Metinė piniginė nauda, gauta, naudojantis darbdavio automobiliu asmeniniams tikslams | — |
| `py030g` | `number` | — | `2` | `open` | — | Metinės darbdavio socialinio draudimo įmokos | — |
| `py035g` | `number` | — | `2` | `open` | — | Papildomos metinės įmokos į privačius pensijų draudimo fondus | — |
| `py050g` | `number` | — | `2` | `open` | — | Metinės savarankiško darbo pajamos | — |
| `py050n` | `number` | — | `2` | `open` | — | Metinės savarankiško darbo pajamos, atskaičius mokesčius | — |
| `py070g` | `number` | — | `2` | `open` | — | Metinė suvartotų produktų, gautų iš savo asmeninio ūkio, vertė | — |
| `py080g` | `number` | — | `2` | `open` | — | Metinės privačių pensijų fondų ar pensijų draudimo išmokos | — |
| `py090g` | `number` | — | `2` | `open` | — | Metinės socialinės išmokos bedarbiams | — |
| `py090n` | `number` | — | `2` | `open` | — | Metinės socialinės išmokos bedarbiams, atskaičius mokesčius | — |
| `py100g` | `number` | — | `2` | `open` | — | Metinės socialinės išmokos senatvėje | — |
| `py110g` | `number` | — | `2` | `open` | — | Metinės socialinės išmokos našliams, našlaičiams | — |
| `py120g` | `number` | — | `2` | `open` | — | Metinės socialinės išmokos ligos atveju | — |
| `py120n` | `number` | — | `2` | `open` | — | Metinės socialinės išmokos ligos atveju, atskaičius mokesčius | — |
| `py130g` | `number` | — | `2` | `open` | — | Metinės socialinės išmokos negalios atveju | — |
| `py140g` | `number` | — | `2` | `open` | — | Metinės socialinės išmokos mokymuisi (stipendijos) | — |
| `ap` | `string` | — | `4` | `open` | — | Apskritys | — |
| `sl` | `string` | — | `4` | `open` | — | Sluoksniai | — |
| `m_k` | `string` | — | `4` | `open` | — | Miestas ar kaimas | — |
| `pl051` | `string` | — | `4` | `open` | — | Profesijos kodas (ISCO-08(COM)) dabartiniame ar paskutiniame pagrindiniame darbe | — |
| `pl190` | `integer` | — | `4` | `open` | — | Asmens amžius, kai jis pradėjo dirbti nuolatinį darbą | — |
| `pl200` | `integer` | — | `4` | `open` | — | Kiek metų asmuo dirba (-o) samdomuoju darbuotoju ar užsiima (-ėmė) privačia veikla? | — |
| `pd020` | `string` | — | `4` | `open` | — | Ar keičiate bent dalį susidėvėjusių drabužių naujais, ne dėvėtais drabužiais? | — |
| `pd030` | `string` | — | `4` | `open` | — | Ar turite dvi poras geros būklės kasdienių batų? | — |
| `pd050` | `string` | — | `4` | `open` | — | Ar bent kartą per mėnesį susitinkate su draugais / giminėmis pasivaišinti gėrimais / valgiais? | — |
| `pd060` | `string` | — | `4` | `open` | — | Ar Jūs reguliariai dalyvaujate laisvalaikio veikloje, už kurią reikia mokėti? | — |
| `pd070` | `string` | — | `4` | `open` | — | Ar išleidžiate beveik kas savaitę nedidelę pinigų sumą sau, savo malonumui? | — |
| `pd080` | `string` | — | `4` | `open` | — | Ar turite interneto prieigą asmeninėms reikmėms namuose, kai reikia? | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Statistinio tyrimo metai | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rb090` | `"1"` | — | — | Vyras | — |
| `rb090` | `"2"` | — | — | Moteris | — |
| `pb190` | `"1"` | — | — | Niekada nebuvau vedęs / ištekėjusi | — |
| `pb190` | `"2"` | — | — | Vedęs / ištekėjusi | — |
| `pb190` | `"3"` | — | — | Sutuoktinis (-ė) gyvena atskirai | — |
| `pb190` | `"4"` | — | — | Našlys (-ė) | — |
| `pb190` | `"5"` | — | — | Išsituokęs (-usi) | — |
| `pb200` | `"1"` | — | — | Taip, teisiniu pagrindu | — |
| `pb200` | `"2"` | — | — | Taip, be teisinio pagrindo | — |
| `pb200` | `"3"` | — | — | Ne | — |
| `pe010` | `"1"` | — | — | Taip | — |
| `pe010` | `"2"` | — | — | Ne | — |
| `pe020` | `"0"` | — | — | Ikimokyklinis ugdymas | — |
| `pe020` | `"10"` | — | — | Pradinis mokymas | — |
| `pe020` | `"20"` | — | — | Pagrindinis mokymas | — |
| `pe020` | `"30"` | — | — | Vidurinis mokymas | — |
| `pe020` | `"34"` | — | — | Bendrasis išsilavinimas | — |
| `pe020` | `"35"` | — | — | Profesinis išsilavinimas | — |
| `pe020` | `"40"` | — | — | Profesinis mokymas turint vidurinį išsilavinimą | — |
| `pe020` | `"45"` | — | — | Profesinis išsilavinimas | — |
| `pe020` | `"60"` | — | — | Bakalauro studijos | — |
| `pe020` | `"70"` | — | — | Magistrantūros studijos | — |
| `pe020` | `"80"` | — | — | Doktorantūra | — |
| `pe040` | `"0"` | — | — | Ikimokyklinis ugdymas | — |
| `pe040` | `"100"` | — | — | Pradinis ugdymas | — |
| `pe040` | `"200"` | — | — | Pagrindinis ugdymas | — |
| `pe040` | `"300"` | — | — | Vidurinis ugdymas | — |
| `pe040` | `"344"` | — | — | Vidurinio ugdymo programos | — |
| `pe040` | `"352"` | — | — | Profesinio mokymo programos, nesuteikiančios vidurinio išsilavinimo | — |
| `pe040` | `"354"` | — | — | Profesinio mokymo programos kartu su vidurinio ugdymo programomis | — |
| `pe040` | `"400"` | — | — | Profesinio mokymo programos turint vidurinį išsilavinimą | — |
| `pe040` | `"450"` | — | — | Profesinis išsilavinimas | — |
| `pe040` | `"600"` | — | — | Bakalauro studijos | — |
| `pe040` | `"700"` | — | — | Magistrantūros studijos | — |
| `pe040` | `"800"` | — | — | Doktorantūra | — |
| `ph010` | `"1"` | — | — | Labai gera | — |
| `ph010` | `"2"` | — | — | Gera | — |
| `ph010` | `"3"` | — | — | Vidutiniška | — |
| `ph010` | `"4"` | — | — | Bloga | — |
| `ph010` | `"5"` | — | — | Labai bloga | — |
| `ph020` | `"1"` | — | — | Taip | — |
| `ph020` | `"2"` | — | — | Ne | — |
| `ph030` | `"1"` | — | — | Taip, labai apribota | — |
| `ph030` | `"2"` | — | — | Taip, apribota | — |
| `ph030` | `"3"` | — | — | Ne, neapribota | — |
| `ph040` | `"1"` | — | — | Taip | — |
| `ph040` | `"2"` | — | — | Ne | — |
| `ph050` | `"1"` | — | — | Neįstengiau susimokėti (per brangu) | — |
| `ph050` | `"2"` | — | — | Ilgai teko laukti paslaugos (sunku gauti taloną, nukreipimą ir kt.) | — |
| `ph050` | `"3"` | — | — | Dėl laiko stokos (darbas, vaikų priežiūra ir kt.) | — |
| `ph050` | `"4"` | — | — | Per toli, nebuvo transporto | — |
| `ph050` | `"5"` | — | — | Gydytojų, ligoninių, tyrimo, gydymo baimė | — |
| `ph050` | `"6"` | — | — | Norėjau palaukti, tikėjausi, kad negalavimas praeis savaime | — |
| `ph050` | `"7"` | — | — | Nežinojau nė vieno gero gydytojo ar specialisto | — |
| `ph050` | `"8"` | — | — | Kitos priežastys | — |
| `ph060` | `"1"` | — | — | Taip | — |
| `ph060` | `"2"` | — | — | Ne | — |
| `ph070` | `"1"` | — | — | Neįstengiau susimokėti (per brangu) | — |
| `ph070` | `"2"` | — | — | Ilgai teko laukti paslaugos (sunku gauti taloną, nukreipimą ir kt.) | — |
| `ph070` | `"3"` | — | — | Dėl laiko stokos (darbas, vaikų priežiūra ir kt.) | — |
| `ph070` | `"4"` | — | — | Per toli, nebuvo transporto | — |
| `ph070` | `"5"` | — | — | Gydytojų, ligoninių, tyrimo, gydymo baimė | — |
| `ph070` | `"6"` | — | — | Norėjau palaukti, tikėjausi, kad negalavimas praeis savaime | — |
| `ph070` | `"7"` | — | — | Nežinojau nė vieno gero gydytojo ar specialisto | — |
| `ph070` | `"8"` | — | — | Kitos priežastys | — |
| `pl015` | `"1"` | — | — | Taip | — |
| `pl015` | `"2"` | — | — | Ne | — |
| `pl020` | `"1"` | — | — | Taip | — |
| `pl020` | `"2"` | — | — | Ne | — |
| `pl025` | `"1"` | — | — | Taip | — |
| `pl025` | `"2"` | — | — | Ne | — |
| `pl031` | `"1"` | — | — | Samdomas darbuotojas, dirbantis visą darbo dieną | — |
| `pl031` | `"2"` | — | — | Samdomas darbuotojas, dirbantis ne visą darbo dieną | — |
| `pl031` | `"3"` | — | — | Savarankiškai dirbantis asmuo, dirbantis visą darbo dieną (įskaitant dirbantį be atlyginimo šeimos versle) | — |
| `pl031` | `"4"` | — | — | Savarankiškai dirbantis asmuo, dirbantis ne visą darbo dieną (įskaitant dirbantį be atlyginimo šeimos versle) | — |
| `pl031` | `"5"` | — | — | Bedarbis | — |
| `pl031` | `"6"` | — | — | Mokinys, studentas | — |
| `pl031` | `"7"` | — | — | Senatvės pensininkas | — |
| `pl031` | `"8"` | — | — | Dėl negalios nedirbantis asmuo | — |
| `pl031` | `"9"` | — | — | Privalomosios pradinės karo tarnybos karys | — |
| `pl031` | `"10"` | — | — | Namų šeimininkas (-ė) | — |
| `pl031` | `"11"` | — | — | Kitas ekonomiškai neaktyvus asmuo (išėjęs vaiko priežiūros atostogų ir ir gaunantis mažiau nei pusės algos dydžio išmoką kt.) | — |
| `pl040` | `"1"` | — | — | Savarankiškai dirbantis ir turintis samdomųjų darbuotojų asmuo | — |
| `pl040` | `"2"` | — | — | Savarankiškai dirbantis be samdomųjų darbuotojų asmuo | — |
| `pl040` | `"3"` | — | — | Samdomas darbuotojas | — |
| `pl040` | `"4"` | — | — | Dirbantis be atlyginimo šeimos versle, asmeniniame žemės ūkyje asmuo | — |
| `pl120` | `"1"` | — | — | Mokiausi (studijavau) | — |
| `pl120` | `"2"` | — | — | Negalėjau daugiau dirbti dėl ligos (negalios) | — |
| `pl120` | `"3"` | — | — | Norėčiau dirbti ilgiau, tačiau nerandu visos dienos darbo | — |
| `pl120` | `"4"` | — | — | Nenoriu dirbti daugiau valandų | — |
| `pl120` | `"5"` | — | — | Dirbtų valandų skaičius prilygsta visai darbo savaitei | — |
| `pl120` | `"6"` | — | — | Esu namų šeimininkas (-ė), prižiūriu vaikus arba kitus asmenis | — |
| `pl120` | `"7"` | — | — | Dėl kitų priežasčių | — |
| `pl130` | `"1"` | — | — | Tikslus skaičius, jeigu yra nuo 1 iki 10 | — |
| `pl130` | `"2"` | — | — | Tikslus skaičius, jeigu yra nuo 1 iki 10 | — |
| `pl130` | `"3"` | — | — | Tikslus skaičius, jeigu yra nuo 1 iki 10 | — |
| `pl130` | `"4"` | — | — | Tikslus skaičius, jeigu yra nuo 1 iki 10 | — |
| `pl130` | `"5"` | — | — | Tikslus skaičius, jeigu yra nuo 1 iki 10 | — |
| `pl130` | `"6"` | — | — | Tikslus skaičius, jeigu yra nuo 1 iki 10 | — |
| `pl130` | `"7"` | — | — | Tikslus skaičius, jeigu yra nuo 1 iki 10 | — |
| `pl130` | `"8"` | — | — | Tikslus skaičius, jeigu yra nuo 1 iki 10 | — |
| `pl130` | `"9"` | — | — | Tikslus skaičius, jeigu yra nuo 1 iki 10 | — |
| `pl130` | `"10"` | — | — | Tikslus skaičius, jeigu yra nuo 1 iki 10 | — |
| `pl130` | `"11"` | — | — | Nuo 11 iki 19 asmenų | — |
| `pl130` | `"12"` | — | — | Nuo 20 iki 49 asmenų | — |
| `pl130` | `"13"` | — | — | 50 ar daugiau asmenų | — |
| `pl130` | `"14"` | — | — | Mažiau negu 11 asmenų | — |
| `pl130` | `"15"` | — | — | Daugiau negu 10 asmenų | — |
| `pl140` | `"1"` | — | — | Nuolatinis darbas/neterminuota darbo sutartis | — |
| `pl140` | `"2"` | — | — | Laikinas darbas/terminuota darbo sutartis | — |
| `pl150` | `"1"` | — | — | Taip | — |
| `pl150` | `"2"` | — | — | Ne | — |
| `ap` | `"1"` | — | — | Alytaus apskritis | — |
| `ap` | `"2"` | — | — | Kauno apskritis | — |
| `ap` | `"3"` | — | — | Klaipėdos apskritis | — |
| `ap` | `"4"` | — | — | Marijampolės apskritis | — |
| `ap` | `"5"` | — | — | Panevėžio apskritis | — |
| `ap` | `"6"` | — | — | Šiaulių apskritis | — |
| `ap` | `"7"` | — | — | Tauragės apskritis | — |
| `ap` | `"8"` | — | — | Telšių apskritis | — |
| `ap` | `"9"` | — | — | Utenos apskritis | — |
| `ap` | `"10"` | — | — | Vilniaus apskritis | — |
| `sl` | `"1"` | — | — | Vilnius | — |
| `sl` | `"2"` | — | — | Kaunas | — |
| `sl` | `"3"` | — | — | Klaipėda | — |
| `sl` | `"4"` | — | — | Šiauliai | — |
| `sl` | `"5"` | — | — | Panevėžys | — |
| `sl` | `"6"` | — | — | Kiti miestai | — |
| `sl` | `"7"` | — | — | Kaimai | — |
| `m_k` | `"1"` | — | — | Miestas | — |
| `m_k` | `"2"` | — | — | Kaimas | — |
| `pd020` | `"1"` | — | — | Taip | — |
| `pd020` | `"2"` | — | — | Ne, nes negaliu sau to leisti | — |
| `pd020` | `"3"` | — | — | Ne, dėl kitos priežasties | — |
| `pd030` | `"1"` | — | — | Taip | — |
| `pd030` | `"2"` | — | — | Ne, nes negaliu sau to leisti | — |
| `pd030` | `"3"` | — | — | Ne, dėl kitos priežasties | — |
| `pd050` | `"1"` | — | — | Taip | — |
| `pd050` | `"2"` | — | — | Ne, nes negaliu sau to leisti | — |
| `pd050` | `"3"` | — | — | Ne, dėl kitos priežasties | — |
| `pd060` | `"1"` | — | — | Taip | — |
| `pd060` | `"2"` | — | — | Ne, nes negaliu sau to leisti | — |
| `pd060` | `"3"` | — | — | Ne, dėl kitos priežasties | — |
| `pd070` | `"1"` | — | — | Taip | — |
| `pd070` | `"2"` | — | — | Ne, nes negaliu sau to leisti | — |
| `pd070` | `"3"` | — | — | Ne, dėl kitos priežasties | — |
| `pd080` | `"1"` | — | — | Taip | — |
| `pd080` | `"2"` | — | — | Ne, nes negaliu sau to leisti | — |
| `pd080` | `"3"` | — | — | Ne, dėl kitos priežasties | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `py010g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py010n` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py020g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py021g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py030g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py035g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py035g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py050g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py050n` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py070g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py080g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py090g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py090n` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py100g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py110g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py120g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py120n` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py130g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `py140g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `ap` | `create(property: "apskritis", type: "ref", ref: "/datasets/gov/rc/ar/apskritis/Apskritis")` | `type` | `2` | `open` | — | — | — |
| `ap` | `update(property: "apskritis.adm_kodas", type: "")` | `type` | `4` | — | — | — | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/pajamu_ir_gyvenimo_salygos (https://data.gov.lt/datasets/799/)
