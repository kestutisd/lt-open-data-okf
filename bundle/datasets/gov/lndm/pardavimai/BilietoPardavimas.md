---
type: Table
title: "BilietoPardavimas — Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys"
description: "Duomenų rinkinyje pateikiami duomenys iš Lietuvos nacionalinio dailės muziejaus lankytojų aptarnavimo ir bilietų pardavimo sistemos „nSoft“, apimančios bilietų bei muziejuje parduodamų prekių ir paslaugų pardavimus bei grąžinimus."
resource: "https://get.data.gov.lt/datasets/gov/lndm/pardavimai/BilietoPardavimas"
tags: [gov, lndm, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lndm/bilietu_pardavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lndm/bilietu_pardavimai.csv#L11"
    last_modified: "2026-11-11T14:39:20Z"
---

# BilietoPardavimas — Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys

Duomenų rinkinyje pateikiami duomenys iš Lietuvos nacionalinio dailės muziejaus lankytojų aptarnavimo ir bilietų pardavimo sistemos „nSoft“, apimančios bilietų bei muziejuje parduodamų prekių ir paslaugų pardavimus bei grąžinimus. Sistemoje registruojama kiekviena pardavimo operacija, nurodomas jos identifikatorius, parduota prekė ar paslauga bei, jei taikomas, bilieto numeris.

Duomenyse fiksuojamas parduotas kiekis, vieneto kaina ir pritaikyta nuolaida, sudarant galimybę analizuoti kainodarą ir nuolaidų taikymo praktiką. Taip pat pateikiamas tikslus pardavimo laikas ir informacija apie renginį – jo pavadinimas ir pradžios laikas, leidžiantys vertinti lankytojų srautus konkrečių ekspozicijų ar renginių kontekste. Atskirai žymimi grąžinimo atvejai, kas svarbu finansinių srautų ir vartotojų elgsenos analizei.

Papildomas laukas „padalinys“ leidžia identifikuoti konkretų muziejaus padalinį, kuriame įvyko pardavimas, todėl duomenys gali būti naudojami teritorinei ar organizacinei veiklos analizei. Rinkinys sudaro pagrindą lankomumo, pajamų struktūros, renginių populiarumo ir komercinės veiklos rezultatų vertinimui.

- **Model:** `datasets/gov/lndm/pardavimai/BilietoPardavimas`[^manifest]
- **Dataset:** [Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys](../pardavimai.md) (`datasets/gov/lndm/pardavimai`)
- **Manifest CSV:** [datasets/gov/lndm/bilietu_pardavimai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lndm/bilietu_pardavimai.csv#L11)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lndm/pardavimai/BilietoPardavimas`
- **Primary Key (`ref`):** `pard_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pard_id` | `string` | — | `4` | `open` | — | Pardavimo identifikatorius | — |
| `pard_preke` | `string` | — | `4` | `open` | — | Pardavimo prekė | — |
| `bilieto_numeris` | `string` | — | `4` | `open` | — | Bilieto numeris | — |
| `kiekis` | `integer` | — | `4` | `open` | — | Bilietų kiekis | — |
| `vnt_kaina` | `number` | — | `4` | `open` | — | Pardavimo kaina | — |
| `nuolaida` | `number` | — | `4` | `open` | — | Pardavimo nuolaida | — |
| `pardavimo_laikas` | `datetime` | `S` | `4` | `open` | — | Pardavimo laikas | — |
| `renginio_pavadinimas` | `string` | — | `4` | `open` | — | Renginio pavadinimas | — |
| `renginio_pradz_laikas` | `datetime` | `S` | `4` | `open` | — | Bilieto renginio data ir laikas | — |
| `grazinimas` | `boolean` | — | `4` | `open` | — | Ar bilietas grąžintas | — |
| `padalinys` | `string` | — | `4` | `open` | — | Padalinio pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lndm/bilietu_pardavimai.csv
