---
type: Dataset
title: "Diagnozių dažnis"
description: "Diagnozių TLK-10-AM kodų, nurodytų ESPBI IS (e-sveikatos) dokumentuose, dažniai pagal įvairius pjūvius."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes"
tags: [gov, lsd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2843/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/diagnozes"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Diagnozių dažnis

- **Namespace:** `datasets/gov/lsd/sveikata/diagnozes`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2843/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes`[^dcat]
- **Portal Title (`@lt`):** Įvairių diagnozių TLK-10-AM kodų dažniai[^dcat]
- **Portal Title (`@en`):** Frequencies of various ICD-10-AM codes[^dcat]
- **Issued (`dct:issued`):** `2024-10-31`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-10-31` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Diagnozių TLK-10-AM kodų, nurodytų ESPBI IS (e-sveikatos) dokumentuose, dažniai pagal įvairius pjūvius. Nurodytas skaičius unikalių asmenų, kuriems per nurodytą periodą ESPBI IS dokumentų diagnozės laukeliuose buvo bent kartą įrašytas konkretus TLK kodas, taip pat išskaidant pagal savivaldybę ir kitus parametrus. Kai kurie TLK-10-AM kodai nurodo medicinines procedūras, o ne diagnozes; jų dažniai taip pat pateikti. Čia pateikiami duomenys yra tik skirti tik preliminariam vertinimui ir nėra oficialiosios statistikos dalis. Pastabos: metinėse lentelėse nurodytas skaičius nėra naujų diagnozių per metus skaičius (sergamumas), nes asmenys, sergantys liga kelerius metus, bus įskaičiuojami į kiekvienų metų sumą. Šis skaičius gali nukrypti nuo tikrojo ligotumo (skaičiaus asmenų, kurie šiuo metu serga liga): diagnozės gali būti negalutinės arba nepatvirtintos; diagnozė gali būti neužrašyta dokumente, jei nėra aktuali apsilankymo metu; ligos gali būti trumpalaikės; nėra stebima, kada sergantys asmenys atvyko į šalį, išvyko iš šalies, arba mirė; vienas žmogus gali būti priskaičiuotas keliose savivaldybėse, jei lankėsi skirtingų savivaldybių SPĮ. Gydymo įstaigoms savivaldybė priskirta jungiant ESPBI IS ir VASPVT SPĮLIS sistemų duomenis. Asmens gyvenamoji vieta nustatyta pagal GR. Oficialioji statistika apie ligų dažnius Lietuvoje teikiama Higienos instituto (www.hi.lt). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Frequencies of ICD-10-AM medical codes reported in electronic health records from the ESPBI IS (e-health system) documents. The frequency is calculated as the number of unique persons who have received the particular ICD code in the diagnosis field of an ESPBI IS document at least once during the index period, further split by municipality and other parameters. The data provided here is intended for preliminary evaluation only and is not part of official statistics. Note: the yearly frequency is not the number of new cases diagnosed that year (incidence), because patients who suffer from a disease for a period of several years will be included in the tally for each year. This number can also deviate from the actual prevalence (number of patients who currently suffer from a disease): the diagnoses indicated here can be unverified or not final; a diagnosis may have been not recorded if it was not relevant at the time of visit; the period of illness may be short; the time at which patients enter the country, leave the country, or die is not tracked or accounted for; a person can be counted repeatedly across several municipalities, if he or she attended healthcare providers in different locations. The municipality of the provider was assigned based on a combination of data from ESPBI IS and VASPVT SPĮLIS systems. Residential addresses were identified from GR. Official statistics about disease rates in Lithuania is provided by the Institute of Hygiene (www.hi.lt)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [EspbiDiagnoze025](diagnozes/EspbiDiagnoze025.md) | Diagnozių dažnis pagal E025 formos duomenis | `4` | `vda_id` | — | `7` | "Diagnozių TLK-10-AM kodų, nurodytų ESPBI IS E025 dokumente (“Ambulatorinio apsilankymo aprašymas”), dažnis pagal apsilankymo metus, lytį ir savivaldybę... |
| [EspbiDiagnoze003](diagnozes/EspbiDiagnoze003.md) | Diagnozių dažnis pagal E003 formos duomenis | `4` | `vda_id` | — | `7` | "Diagnozių TLK-10-AM kodų, nurodytų ESPBI IS E003 dokumente (“Stacionaro epikrizė”), dažnis pagal apsilankymo metus, lytį ir savivaldybę sveikatos... |
| [Persalimas](diagnozes/Persalimas.md) | Kvėpavimo takų infekcijų dažnis dienos tikslumu | `4` | `vda_id` | — | `6` | "Kvėpavimo takų infekcijų diagnozių dinamika: TLK-10-AM kodų, nurodytų ESPBI IS E025 dokumente (“Ambulatorinio apsilankymo aprašymas”), dažnis pagal... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/diagnozes (https://data.gov.lt/datasets/2843/)
