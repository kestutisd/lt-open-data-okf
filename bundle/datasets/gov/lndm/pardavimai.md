---
type: Dataset
title: "Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys"
description: "Duomenų rinkinyje pateikiami duomenys iš Lietuvos nacionalinio dailės muziejaus lankytojų aptarnavimo ir bilietų pardavimo sistemos „nSoft“, apimančios bilietų bei muziejuje parduodamų prekių ir paslaugų pardavimus bei grąžinimus."
resource: "https://get.data.gov.lt/datasets/gov/lndm/pardavimai"
tags: [gov, lndm, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lndm/bilietu_pardavimai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lndm/bilietu_pardavimai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4271/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lndm/pardavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys

Duomenų rinkinyje pateikiami duomenys iš Lietuvos nacionalinio dailės muziejaus lankytojų aptarnavimo ir bilietų pardavimo sistemos „nSoft“, apimančios bilietų bei muziejuje parduodamų prekių ir paslaugų pardavimus bei grąžinimus. Sistemoje registruojama kiekviena pardavimo operacija, nurodomas jos identifikatorius, parduota prekė ar paslauga bei, jei taikomas, bilieto numeris. Duomenyse fiksuojamas parduotas kiekis, vieneto kaina ir pritaikyta nuolaida, sudarant galimybę analizuoti kainodarą ir nuolaidų taikymo praktiką. Taip pat pateikiamas tikslus pardavimo laikas ir informacija apie renginį – jo pavadinimas ir pradžios laikas, leidžiantys vertinti lankytojų srautus konkrečių ekspozicijų ar renginių kontekste. Atskirai žymimi grąžinimo atvejai, kas svarbu finansinių srautų ir vartotojų elgsenos analizei. Papildomas laukas „padalinys“ leidžia identifikuoti konkretų muziejaus padalinį, kuriame įvyko pardavimas, todėl duomenys gali būti naudojami teritorinei ar organizacinei veiklos analizei. Rinkinys sudaro pagrindą lankomumo, pajamų struktūros, renginių populiarumo ir komercinės veiklos rezultatų vertinimui. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Namespace:** `datasets/gov/lndm/pardavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lndm/bilietu_pardavimai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lndm/bilietu_pardavimai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lndm/pardavimai` (`deployed`)[^manifest]
- **Provider:** `lndm` — Lietuvos nacionalinis dailės muziejus *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4271/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lndm/pardavimai`[^dcat]
- **Portal Title (`@lt`):** Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys[^dcat]
- **Portal Title (`@en`):** Data on ticket sales system of the Lithuanian National Museum of Art[^dcat]
- **Issued (`dct:issued`):** `2026-02-27`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-03-02` .. `2026-03-10`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BilietoPardavimas](pardavimai/BilietoPardavimas.md) | Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys | `4` | `pard_id` | — | `11` | Duomenų rinkinyje pateikiami duomenys iš Lietuvos nacionalinio dailės muziejaus lankytojų aptarnavimo ir bilietų pardavimo sistemos „nSoft“, apimančios... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lndm/bilietu_pardavimai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lndm/bilietu_pardavimai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lndm/pardavimai (https://data.gov.lt/datasets/4271/)
