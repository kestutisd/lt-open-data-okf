---
type: Dataset
title: "Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys"
description: "Duomenų rinkinyje pateikiami duomenys iš Lietuvos nacionalinio dailės muziejaus lankytojų aptarnavimo ir bilietų pardavimo sistemos „nSoft“, apimančios bilietų bei muziejuje parduodamų prekių ir paslaugų pardavimus bei grąžinimus."
resource: "https://get.data.gov.lt/datasets/gov/lndm/pardavimai"
tags: [gov, lndm, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lndm/bilietu_pardavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lndm/bilietu_pardavimai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys

Duomenų rinkinyje pateikiami duomenys iš Lietuvos nacionalinio dailės muziejaus lankytojų aptarnavimo ir bilietų pardavimo sistemos „nSoft“, apimančios bilietų bei muziejuje parduodamų prekių ir paslaugų pardavimus bei grąžinimus. Sistemoje registruojama kiekviena pardavimo operacija, nurodomas jos identifikatorius, parduota prekė ar paslauga bei, jei taikomas, bilieto numeris.

Duomenyse fiksuojamas parduotas kiekis, vieneto kaina ir pritaikyta nuolaida, sudarant galimybę analizuoti kainodarą ir nuolaidų taikymo praktiką. Taip pat pateikiamas tikslus pardavimo laikas ir informacija apie renginį – jo pavadinimas ir pradžios laikas, leidžiantys vertinti lankytojų srautus konkrečių ekspozicijų ar renginių kontekste. Atskirai žymimi grąžinimo atvejai, kas svarbu finansinių srautų ir vartotojų elgsenos analizei.

Papildomas laukas „padalinys“ leidžia identifikuoti konkretų muziejaus padalinį, kuriame įvyko pardavimas, todėl duomenys gali būti naudojami teritorinei ar organizacinei veiklos analizei. Rinkinys sudaro pagrindą lankomumo, pajamų struktūros, renginių populiarumo ir komercinės veiklos rezultatų vertinimui.

- **Namespace:** `datasets/gov/lndm/pardavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lndm/bilietu_pardavimai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lndm/bilietu_pardavimai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lndm/pardavimai`
- **Parent Namespace (`ns`):** Lietuvos nacionalinis dailės muziejus (`datasets/gov/lndm`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BilietoPardavimas](pardavimai/BilietoPardavimas.md) | Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys | `4` | `pard_id` | — | 11 | Duomenų rinkinyje pateikiami duomenys iš Lietuvos nacionalinio dailės muziejaus lankytojų aptarnavimo ir bilietų pardavimo sistemos „nSoft“, apimančios... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lndm/bilietu_pardavimai.csv
