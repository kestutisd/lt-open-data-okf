---
type: Dataset
title: "Savanoriavimo valandos"
description: "Rinkinyje pateikiami Jaunimo reikalų agentūros jaunimo savanoriškos tarnybos savanorių registruotos savanoriavimo valandos priimančioje organizacijoje („PO“)."
resource: "https://get.data.gov.lt/datasets/gov/jra/savanoriavimo_valandos"
tags: [gov, jra, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/savanoriavimo_valandos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/jra/savanoriavimo_valandos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3863/"
    title: "data.gov.lt DCAT-AP — datasets/gov/jra/savanoriavimo_valandos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Savanoriavimo valandos

- **Namespace:** `datasets/gov/jra/savanoriavimo_valandos`[^manifest]
- **Manifest CSV:** [datasets/gov/jra/savanoriavimo_valandos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/savanoriavimo_valandos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/jra/savanoriavimo_valandos` (`deployed`)[^manifest]
- **Provider:** `jra` — Jaunimo reikalų agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3863/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/jra/savanoriavimo_valandos`[^dcat]
- **Portal Title (`@lt`):** Jaunimo savanoriškos tarnybos savanoriavimo valandos[^dcat]
- **Portal Title (`@en`):** Volunteering hours for youth voluntary service[^dcat]
- **Issued (`dct:issued`):** `2025-07-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-06-14`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Jaunimo reikalų agentūros jaunimo savanoriškos tarnybos savanorių registruotos savanoriavimo valandos priimančioje organizacijoje („PO“). Savanoriauti gali asmenys nuo 14 iki 29 m. Per 6 mėn. laikotarpį surinkę nemažiau kaip 240 savanoriavimo valandų (ne mažiau kaip 35 val. per mėnesį), savanoriai gauna pažymėjimą, patvirtinantį teisę į papildomą 0,25 stojamąjį balą į Lietuvos aukštojo mokslo įstaigas. Rinkinyje nurodomas tik savanorišką veiklą organizuojančios („SVO“) organizacijos pavadinimas ir veiklos sritis, nenurodant adreso, nes registruojamas tik buveinės, o ne savanoriavimo organizavimo veiklos adresas. Savanorio lytis („dedikuota_lytis“) nustatyta iš savanorio vardo ir pavardės. Jei pagal vardą ir pavardę nepavyko nustatyti lyties, stulpelyje rašoma „nenustatyta“. Jei vardas baigiasi -a arba -ė raide arba pavardė baigiaisi -ienė, -aitė, -ytė, -utė, -iūtė, -ė raidėmis, tada priskiriama moteriška lytis („mot“). Jei vardas baigiasi -s arba pavardė baigiasi -as, -is, -ys, -us raidėmis – priskiriama vyriška lytis („vyr“). Duomenys kaupiami nuo 2019 metų, bet nuo 2022 metų pradėtas elektroninis grafikų pildymas į sistemą. Iki 2022 metų grafikai buvo vedami rankiniu būdu iš skenuotų savanoriavimo grafikų. Stulpelyje „savan_men_nr“ nurodomas mėnesio eilės numeris, o „savan_val_suma“ – tą mėnesį savanoriautų valandų skaičius. Šie stulpeliai pildyti iki perėjimo prie elektroninės grafikų pildymo sistemos, bet gali būti pildomi ir toliau. Savanoriavimo valandas pradėjus pildyti elektroninėje grafikų pildymo sistemoje pildomi šie stulpeliai: „savan_pradzios_data“, „savan_pabaigos_data“, „savan_val_trukme“ . Stulpelis „ataskaitos_id“ – grafiko kėlimo į sistemą identifikatorius. Informacija rinkinyje atnaujinama kas metus. Duomenų teikėjas – Jaunimo reikalų agentūra. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes volunteer hours registered by youth volunteers of the Youth Agency in the host organisation (“PO”). Volunteering is open to persons aged between 14 and 29. Within a 6-month period, after gathering at least 240 hours of volunteering (at least 35 hours per month), volunteers receive a certificate confirming the right to an additional admission point of 0.25 to Lithuanian higher education institutions. The package refers only to the name and field of activity of the organisation organising voluntary activities (“SVO”), without specifying the address, since only the address of the establishment and not the voluntary activity is recorded. The volunteer's gender (“dedicated” _gender) is determined from the volunteer's name. If the gender cannot be determined by name, the column reads “not identified.” If the name ends - or the name ends - in letters, then the female gender (“mot”) is assigned. If the name ends - or the last name ends - the letters include the male gender (“head”). Data has been compiled since 2019, but electronic filling of schedules into the system has been launched since 2022. By 2022, the schedules had been manually led from scanned volunteering schedules. The “savan_men_nr” column shall indicate the serial number of the month and the “savan_val_sum” shall indicate the number of hours volunteered during that month. These columns are filled in until the transition to the electronic graph filling system, but can continue to be filled in. When volunteering hours begin to be filled in, the following columns shall be filled in in the electronic graph filling system: “savan_start _date”, “savan_end _date”, “savan_val_duration”. The “report_id” column is the identifier for elevating the schedule to the system. The information in the collection is updated annually. The data provider is the Agency for Youth Affairs. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SavanoriavimoValandos](savanoriavimo_valandos/SavanoriavimoValandos.md) | Savanoriavimo valandos | `4` | — | — | `27` | Jaunimo reikalų agentūros jaunimo savanoriškos tarnybos savanorių savanoriautos valandos priimančiose organizacijose |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/jra/savanoriavimo_valandos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/savanoriavimo_valandos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/jra/savanoriavimo_valandos (https://data.gov.lt/datasets/3863/)
