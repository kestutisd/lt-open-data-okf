---
type: Table
title: "BilietoPardavimas — Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys"
description: "Duomenų rinkinyje pateikiami duomenys iš Lietuvos nacionalinio dailės muziejaus lankytojų aptarnavimo ir bilietų pardavimo sistemos „nSoft“, apimančios bilietų bei muziejuje parduodamų prekių ir paslaugų pardavimus bei grąžinimus."
resource: "https://get.data.gov.lt/datasets/gov/lndm/pardavimai/BilietoPardavimas"
tags: [gov, lndm, bilietopardavimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lndm/bilietu_pardavimai.csv#L11"
    title: "atviriduomenys/manifest — datasets/gov/lndm/bilietu_pardavimai.csv#L11"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4271/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lndm/pardavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# BilietoPardavimas — Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys

Duomenų rinkinyje pateikiami duomenys iš Lietuvos nacionalinio dailės muziejaus lankytojų aptarnavimo ir bilietų pardavimo sistemos „nSoft“, apimančios bilietų bei muziejuje parduodamų prekių ir paslaugų pardavimus bei grąžinimus. Sistemoje registruojama kiekviena pardavimo operacija, nurodomas jos identifikatorius, parduota prekė ar paslauga bei, jei taikomas, bilieto numeris. Duomenyse fiksuojamas parduotas kiekis, vieneto kaina ir pritaikyta nuolaida, sudarant galimybę analizuoti kainodarą ir nuolaidų taikymo praktiką. Taip pat pateikiamas tikslus pardavimo laikas ir informacija apie renginį – jo pavadinimas ir pradžios laikas, leidžiantys vertinti lankytojų srautus konkrečių ekspozicijų ar renginių kontekste. Atskirai žymimi grąžinimo atvejai, kas svarbu finansinių srautų ir vartotojų elgsenos analizei. Papildomas laukas „padalinys“ leidžia identifikuoti konkretų muziejaus padalinį, kuriame įvyko pardavimas, todėl duomenys gali būti naudojami teritorinei ar organizacinei veiklos analizei. Rinkinys sudaro pagrindą lankomumo, pajamų struktūros, renginių populiarumo ir komercinės veiklos rezultatų vertinimui. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/lndm/pardavimai/BilietoPardavimas`[^manifest]
- **Dataset:** [Lietuvos nacionalinio dailės muziejaus bilietų pardavimo sistemos duomenys](../pardavimai.md) (`datasets/gov/lndm/pardavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lndm/bilietu_pardavimai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lndm/bilietu_pardavimai.csv#L11)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lndm/pardavimai/BilietoPardavimas` (`deployed`)[^manifest]
- **Provider:** `lndm` — Lietuvos nacionalinis dailės muziejus *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `pard_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lndm/bilietu_pardavimai.csv#L11 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lndm/bilietu_pardavimai.csv#L11)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lndm/pardavimai (https://data.gov.lt/datasets/4271/)
