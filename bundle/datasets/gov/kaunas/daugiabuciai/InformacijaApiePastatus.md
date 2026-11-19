---
type: Table
title: "InformacijaApiePastatus — Daugiabučiai, valdytojai"
description: "Kauno miesto daugiabučiai namai (3 ir daugiau butų), kuriems reikalingi bendro naudojimo objektų valdytojai"
resource: "https://get.data.gov.lt/datasets/gov/kaunas/daugiabuciai/InformacijaApiePastatus"
tags: [gov, kaunas, informacijaapiepastatus, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/daugiabuciai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/kaunas/daugiabuciai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1361/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kaunas/daugiabuciai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# InformacijaApiePastatus — Daugiabučiai, valdytojai

**Dataset Context:** Kauno miesto daugiabučiai namai (3 ir daugiau butų), kuriems reikalingi bendro naudojimo objektų valdytojai[^manifest]

- **Model:** `datasets/gov/kaunas/daugiabuciai/InformacijaApiePastatus`[^manifest]
- **Dataset:** [Kauno miesto savivaldybės teikiami duomenys](../daugiabuciai.md) (`datasets/gov/kaunas/daugiabuciai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kaunas/daugiabuciai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/daugiabuciai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kaunas/daugiabuciai/InformacijaApiePastatus` (`deployed`)[^manifest]
- **Provider:** `kaunas` — Kauno miesto savivaldybė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | — | `open` | — | Namo ID | Namo indentifikacinis numeris sistemoje |
| `gatves_id` | `integer` | — | — | `open` | — | Gatvės ID | Gatvės ID, kurioje yra namas |
| `namo_nr` | `string` | — | — | `open` | — | Namo numeris | Namo numeris |
| `namo_pap_info` | `string` | — | — | `open` | — | Namo papildoma informacija | Papildoma informacija apie namą. |
| `namo_plotas` | `number` | — | — | `open` | — | Namo plotas | Namo plotas |
| `butu_sk` | `string` | — | — | `open` | — | Butų skaičius | Butų skaičius |
| `negyvenamu_skaicius` | `integer` | — | — | `open` | — | Negyvenamų butų skaičius | Negyvenamų butų skaičius name |
| `statybos_metai` | `string` | — | — | `open` | — | Statybos metai | Statybos metai. |
| `tarifas` | `number` | — | — | `open` | — | Administravimo tarifas | Namo administravimo tarifas |
| `aukstu_sk` | `string` | — | — | `open` | — | Aukštų skaičius | Namo aukštų skaičius |
| `zemes_plotas` | `number` | — | — | `open` | — | Žemės plotas | Namo žemės plotas. |
| `bukle` | `string` | — | — | `open` | — | Būklės ID | Namo būklės indentifikacinis numeris. |
| `pabaigos_data` | `string` | — | — | `open` | — | Pabaigos data | Namo renovacijos pabaigimo data. |
| `skyrimo_pagrindas` | `string` | — | — | `open` | — | Skyrimo pagrindas | Data kada namo valdytojas buvo įregistruotas registrų centre arba kada sudaryta sutartis ir įsakymo numeris. |
| `administravimo_pabaiga` | `date` | — | — | `open` | — | Administravimo pabaiga | Namo administravimo pabaigos data. |
| `ar_perduotas` | `integer` | — | — | `open` | — | Perdavimo būsenos ID | Namo perdavimo kitam valdytojui būsenos indentifikacinis numeris. |
| `atlikti_darbai` | `string` | — | — | `open` | — | Atlikti darbai | Name atlikti darbai |
| `seniunija` | `string` | — | — | `open` | — | Seniūnija | Seniūnijos pavadinimas |
| `gatve` | `string` | — | — | `open` | — | Gatvė | Gatvės pavadinimas |
| `bukles_pav` | `string` | — | — | `open` | — | Būklė | Namo būklės pavadinimas. |
| `valdymo_forma` | `string` | — | — | `open` | — | Valdymo forma | Valdymo formos pavadinimas. |
| `vald_pav` | `string` | — | — | `open` | — | Valdytojas | Namo valdytojo pavadinimas. |
| `vald_asmuo` | `string` | — | — | `open` | — | Valdytojo atsakingas asmuo | Namo valdytojo atsakingas asmuo |
| `telefonas` | `string` | — | — | `open` | — | Atsakingo asmens telefonas | Namo valdytojo atsakingo asmens telefono numeris. |
| `pareigu_pav` | `string` | — | — | `open` | — | Atsakingo asmens pareigos | Namo valdytojo atsakingo asmens pareigos. |
| `perduotas_pav` | `string` | — | — | `open` | — | Perdavimo būsenos pavadinimas | Namo perdavimo kitam valdytojui būsenos pavadinimas. |
| `rangovas` | `string` | — | — | `open` | — | Rangovas | Namo rangovo pavadinimas. |
| `koord_x` | `number` | — | — | `open` | — | X koordinatė | X koordinatė LKS94 |
| `koord_y` | `number` | — | — | `open` | — | Y koordinatė | Y koordinatė LKS94 |
| `lng` | `number` | — | — | `open` | — | Ilgumos koordinatės | Ilguma, WGS84 |
| `lat` | `number` | — | — | `open` | — | Platumos koordinatės | Platuma WGS84 |

[^manifest]: atviriduomenys/manifest — datasets/gov/kaunas/daugiabuciai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/daugiabuciai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kaunas/daugiabuciai (https://data.gov.lt/datasets/1361/)
