---
type: Dataset
title: "Mirties priežastys pagal skaitmeninius medicininius mirties liudijimus"
description: "DUOMENŲ ŠALTINIS: Naudojami eSveikatos (ESPBI IS) skaitmeninių medicininių mirties liudijimų (forma E106) duomenys, kuriuos Registrų centras kasdien teikia į Valstybės duomenų agentūros (VDA) Valstybės duomenų valdysenos informacinę sistemą (VDV IS)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/mirciu_priezastys"
tags: [gov, lsd, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2026/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/mirciu_priezastys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Mirties priežastys pagal skaitmeninius medicininius mirties liudijimus

- **Namespace:** `datasets/gov/lsd/sveikata/mirciu_priezastys`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/mirciu_priezastys` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2026/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/mirciu_priezastys`[^dcat]
- **Portal Title (`@lt`):** Mirties priežastys pagal skaitmeninius medicininius mirties liudijimus[^dcat]
- **Portal Title (`@en`):** Causes of death according to digital medical death certificates[^dcat]
- **Issued (`dct:issued`):** `2023-07-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-01` .. `2026-04-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

DUOMENŲ ŠALTINIS: Naudojami eSveikatos (ESPBI IS) skaitmeninių medicininių mirties liudijimų (forma E106) duomenys, kuriuos Registrų centras kasdien teikia į Valstybės duomenų agentūros (VDA) Valstybės duomenų valdysenos informacinę sistemą (VDV IS). IMTIS, APIMTIS, ATNAUJINIMAS: Dėl bet kokių priežasčių mirę asmenys, kurių mirtis yra dokumentuota skaitmeniniame medicininame mirties liudijime (forma E106) eSveikatos sistemoje. Palikti tik validų lietuvišką asmens kodą (pagal struktūrą ir kontrolinį skaitmenį) mirties liudijime turintys asmenys. Pateikiamos mirtys, įvykusios nuo 2018 metų sausio 1 d. iki septintos dienos prieš lentelės atnaujinimo datą. Duomenys atnaujinami trečią kiekvieno mėnesio dieną. LENTELĖS STRUKTŪRA: Lentelė yra agreguota pagal penkis požymius: mirties metus, mirties mėnesį, mirusiojo amžiaus grupę, lytį, nerevizuotą pagrindinę mirties priežastį (triženklį TLK-10-AM diagnozės kodą). Tad kiekviena eilutė yra unikali šių penkių požymių kombinacija. Paskutinis stulpelis (mirusiųjų skaičius) niekada nėra lygus 0, t. y. jeigu konkrečiais metais, konkretų mėnesį, konkrečioje amžiaus ir lyties grupėje dėl konkrečios priežasties nemirė nei vienas asmuo - tokia eilutė tiesiog nėra įtraukiama į lentelę. MIRTIES PRIEŽASTYS: Į Medicininio mirties liudijimo pagrindinės mirties priežasties eilutę gydytojo įrašytas TLK-10-AM kodas. PASITEIRAVIMUI: Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. SVARBIOS PASTABOS: [1] Tai nėra oficialioji mirties priežasčių statistika, kurią rengia Higienos institutas. Šioje lentelėje mirties priežastys yra nerevizuotos, tai yra tokios, kokias jas medicininiame mirties liudijime įrašė sveikatos priežiūros specialistas. Šie įrašai vėliau Mirties atvejų ir jų priežasčių valstybės registre yra revizuojami ir sukoduojami ir pagal tarptautines Pasaulio sveikatos organizacijos (PSO) taisykles išrenkama pagrindinė mirties priežastis. Plačiau apie sąvokas "pagrindinė mirties priežastis", "tarpinė mirties priežastis" ir "tiesioginė mirties priežastis" skaitykite čia: https://hi.lt/uploads/pdf/padaliniai/MPR/MML_rekomendacijos.pdf. [2] Šiuose duomenys retais atvejais duomenys gali būti retrospektyviai atnaujinami (pvz., dėl Valstybinės teismo medicinos tarnybos vykdomos ekspertizės). [3] Šiuose duomenyse neapskaitomos perinatalinės mirtys (medicininiai perinatalinės mirties liudijimai, forma E106-2-1). [4] Šie duomenys skirsis nuo tikslesnės Higienos instituto (HI) vykdomos mirčių apskaitos: HI apskaito ir neskaitmeninius ("popierinius") medicininius mirties liudijimus, kurių gali būti apie 1%; tačiau šioje lentelėje yra tik skaitmeniniai medicininiai mirties liudijimai. [5] Šie duomenys nežymiai skirsis nuo VDA rengiamos oficialiosios mirtingumo statistikos, kurioje apskaitomi tik nuolatiniai gyventojai, o einamiesiems metams naudojama ne faktinė mirties data (naudojama data, kuomet apie mirtį sužinota); tačiau šioje lentelėje į apimtį gali patekti ir Lietuvos teritorijoje mirę ne Lietuvos piliečiai ar asmenys, kurie nėra nuolatiniai Lietuvos gyventojai, taip pat naudojama faktinė mirties data. [6] Taip pat duomenyse yra pašalinti mirusieji, kurie medicininiame mirties liudijime neturėjo validaus lietuviško asmens kodo. [7] Csv faile yra nurodomas priezastis._id, kurį galima rasti TLK klasifikatoriuje https://get.data.gov.lt/datasets/gov/vlk/tlk10am/Tlk10am arba atsisiųsti patogesnę versiją su klasifikatoriaus kodu ir pavadinimu https://get.data.gov.lt/datasets/gov/lsd/sveikata/mirciu_priezastys/MirtiesPriezastis?select(mirties_metai,mirties_menuo,amziaus_grupe,lytis,priezastis.code,priezastis.name,asmenu_sk). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

[Please pay a very close attention to the section "IMPORTANT NOTES"'] DATA SOURCE: Data from Lithuania's centralised health register "eSveikata" (ESPBI IS): digital medical death certificates (Form E106), which the Centre of Registers daily provides to the State Data Governance Information System (SDG IS) of the State Data Agency. SAMPLE, SCOPE, UPDATE: Persons who have died of any cause and whose death is documented on a digital medical death certificate (Form E106) in the eSveikata system. Only the persons with a valid Lithuanian personal identification number (according to the structure and check digit) on the death certificate are covered here. Deaths occurring between 1 January 2018 and the seventh day before the table update date are presented. The data is updated weekly. TABLE STRUCTURE: The table is aggregated on five attributes: year of death, month of death, age group of the deceased, sex, unrevised main cause of death (ICD-10-AM diagnosis code, shortened to the first 3 symbols). Each row is therefore a unique combination of these five attributes. The last column (number of deaths) is never equal to 0, i.e. if in a specific year, in a specific month, in a specific age and sex group, no person died from a specific cause, this row is simply not included in the table. CAUSES OF DEATH: Unrevised ICD-10-AM code entered by the doctor in the main cause of death section of the medical death certificate. Codes are shortened to first 3 symbols. CONTACTS: State Data Governance team: vdv@stat.gov.lt. IMPORTANT NOTES: [1] These are not official statistics on the causes of death produced by the Institute of Hygiene. In this table, the causes of death are unrevised, i.e. are as entered by the health professional into the medical death certificate. In official statistics, these entries would be revised and recoded in the State Register of Deaths and Causes of Death and the primary cause of death is determined in accordance with the international rules of the World Health Organisation (WHO). For more information on the concepts 'primary cause of death', 'intermediate cause of death' and 'immediate cause of death', see here: https://hi.lt/uploads/pdf/padaliniai/MPR/MML_rekomendacijos.pdf. [2] In rare cases, data can be retrospectively updated (e.g. due to expert examination by the State Forensic Medicine Service). [3] These data do not include perinatal deaths (medical certificates of perinatal death, Form E106-2-1). [4] These data will differ from the more accurate death records kept by the Institute of Hygiene: The Institute of Hygiene additionally collects non-digital (i.e., paper) medical death certificates (they could make up around 1% of total deaths); however, this table includes only digital medical death certificates. [5] These data will slightly differ from the official mortality statistics compiled by the State Data Agency, where only the resident population is included and the actual date of death is not used (the date on which the death was reported is used); however, in this table, the scope may cover deaths of non-Lithuanian citizens or persons who are not permanent residents of Lithuania who died in the territory of the Republic of Lithuania, and the actual date of death is used. [6] The data also exclude the deaths of persons who did not have a valid Lithuanian personal identification number on their medical death certificate.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MirtiesPriezastis](mirciu_priezastys/MirtiesPriezastis.md) | Mirtys ir jų priežastys Lietuvoje | `4` | `id` | `open` | `7` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/mirciu_priezastys (https://data.gov.lt/datasets/2026/)
