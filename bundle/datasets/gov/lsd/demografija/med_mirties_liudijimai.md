---
type: Dataset
title: "Mirčių skaičius pagal skaitmeninius medicininius mirties liudijimus"
description: "DUOMENŲ ŠALTINIS: Naudojami eSveikatos (ESPBI IS) skaitmeninių medicininių mirties liudijimų (forma E106) duomenys, kuriuos Registrų centras kasdien teikia į Valstybės duoenų agentūros (VDA) Valstybės duomenų valdysenos informacinę sistemą (VDV IS)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/demografija/med_mirties_liudijimai"
tags: [gov, lsd, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/demografija/demografija.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/demografija/demografija.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2025/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/demografija/med_mirties_liudijimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Mirčių skaičius pagal skaitmeninius medicininius mirties liudijimus

- **Namespace:** `datasets/gov/lsd/demografija/med_mirties_liudijimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/demografija/demografija.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/demografija/demografija.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/demografija/med_mirties_liudijimai` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2025/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/demografija/med_mirties_liudijimai`[^dcat]
- **Portal Title (`@lt`):** Mirčių skaičius pagal skaitmeninius medicininius mirties liudijimus[^dcat]
- **Portal Title (`@en`):** Deaths (according to digital medical death certificates)[^dcat]
- **Issued (`dct:issued`):** `2023-04-02`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2022-10-04` .. `2026-04-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

DUOMENŲ ŠALTINIS: Naudojami eSveikatos (ESPBI IS) skaitmeninių medicininių mirties liudijimų (forma E106) duomenys, kuriuos Registrų centras kasdien teikia į Valstybės duoenų agentūros (VDA) Valstybės duomenų valdysenos informacinę sistemą (VDV IS). IMTIS, APIMTIS, ATNAUJINIMAS: Dėl bet kokių priežasčių mirę asmenys, kurių mirtis yra dokumentuota skaitmeniniame medicininame mirties liudijime (forma E106) eSveikatos sistemoje. Palikti tik validų lietuvišką asmens kodą (pagal struktūrą ir kontrolinį skaitmenį) mirties liudijime turintys asmenys. Pateikiamos mirtys, įvykusios nuo 2018 metų sausio 1 d. iki septintos dienos prieš lentelės atnaujinimo datą. Duomenys atnaujinami kas savaitę. LENTELĖS STRUKTŪRA: Lentelė yra agreguota pagal tris požymius: mirties datą, mirusiojo amžių ir lytį, tad kiekviena eilutė yra unikali šių trijų požymių kombinacija. Paskutinis stulpelis (mirusiųjų skaičius) niekada nėra lygus 0, t. y. jeigu konkrečią dieną konkrečioje amžiaus ir lyties grupėje nebuvo mirusių asmenų - tokia eilutė tiesiog nėra įtraukiama į lentelę. PASITEIRAVIMUI: Valstybės duomenų valdysenos komanda: vdv@stat.gov.lt. SVARBIOS PASTABOS: Tai nėra oficialioji mirčių statistika, skelbiama https://osp.stat.gov.lt/ ir https://www.hi.lt/. Ši Lentelė yra paruošta iš tarpinių nepilnų duomenų. Šiuose duomenys retais atvejais duomenys gali būti retrospektyviai atnaujinami (pvz., dėl Valstybinės teismo medicinos tarnybos vykdomos ekspertizės). Šiuose duomenyse neapskaitomos perinatalinės mirtys (medicininiai perinatalinės mirties liudijimai, forma E106-2-1). Šie duomenys nežymiai skirsis nuo tikslesnės Higienos instituto (HI) vykdomos mirčių apskaitos: HI apskaito ir neskaitmeninius ("popierinius") medicininius mirties liudijimus, kurių gali būti apie 1%; tačiau šioje lentelėje yra tik skaitmeniniai medicininiai mirties liudijimai. Šie duomenys nežymiai skirsis nuo Valstybės duomenų agentūros rengiamos oficialiosios mirtingumo statistikos, kurioje apskaitomi tik nuolatiniai gyventojai, o einamiesiems metams naudojama ne faktinė mirties data (naudojama data, kuomet apie mirtį sužinota); tačiau šioje lentelėje į apimtį gali patekti ir Lietuvos teritorijoje mirę ne Lietuvos piliečiai ar asmenys, kurie nėra nuolatiniai Lietuvos gyventojai, taip pat naudojama faktinė mirties data. Taip pat duomenyse yra pašalinti mirusieji, kurie medicininiame mirties liudijime neturėjo validaus lietuviško asmens kodo. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

[Please pay a very close attention to the section "IMPORTANT NOTES"'] DATA SOURCE: Data from Lithuania's centralised health register "eSveikata" (ESPBI IS): digital medical death certificates (Form E106), which the Centre of Registers daily provides to the State Data Governance Information System (SDG IS) of the State Data Agency. SAMPLE, SCOPE, UPDATE: Persons who have died of any cause and whose death is documented on a digital medical death certificate (Form E106) in the eSveikata system. Only the persons with a valid Lithuanian personal identification number (according to the structure and check digit) on the death certificate are covered here. Deaths occurring between 1 January 2018 and the seventh day before the table update date are presented. The data is updated weekly. TABLE STRUCTURE: The table is aggregated on three attributes: date of death, age group of the deceased, sex. Each row is therefore a unique combination of these three attributes. The last column (number of deaths) is never equal to 0, i.e. if on a specific date, in a specific age and sex group, no person died from a specific cause, this row is simply not included in the table. CONTACTS: State Data Governance team: vdv@stat.gov.lt. IMPORTANT NOTES: [1] These are not official statistics on the causes (and counts) of death produced by the Institute of Hygiene. [2] In rare cases, data can be retrospectively updated (e.g. due to expert examination by the State Forensic Medicine Service). [3] These data do not include perinatal deaths (medical certificates of perinatal death, Form E106-2-1). [4] These data will differ from the more accurate death records kept by the Institute of Hygiene: The Institute of Hygiene additionally collects non-digital (i.e., paper) medical death certificates (they could make up around 1% of total deaths); however, this table includes only digital medical death certificates. [5] These data will slightly differ from the official mortality statistics compiled by the State Data Agency, where only the resident population is included and the actual date of death is not used (the date on which the death was reported is used); however, in this table, the scope may cover deaths of non-Lithuanian citizens or persons who are not permanent residents of Lithuania who died in the territory of the Republic of Lithuania, and the actual date of death is used. [6] The data also exclude the deaths of persons who did not have a valid Lithuanian personal identification number on their medical death certificate.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MedMirtiesLiudijimas](med_mirties_liudijimai/MedMirtiesLiudijimas.md) | Mirčių skaičiai pagal elektroninius medicininius mirties liudijimus | `4` | `id` | `open` | `5` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/demografija/demografija.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/demografija/demografija.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/demografija/med_mirties_liudijimai (https://data.gov.lt/datasets/2025/)
