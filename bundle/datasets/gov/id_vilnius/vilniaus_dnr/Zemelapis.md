---
type: Table
title: "Zemelapis — Vilniaus miesto žemėlapiai"
description: "\"Duomenys iš „ID Vilnius“ apie Vilniaus miesto planus, žemėlapius, ortografines nuotraukas ir kitą kartografinę medžiagą."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/Zemelapis"
tags: [gov, id_vilnius, zemelapis, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L91"
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L91"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Zemelapis — Vilniaus miesto žemėlapiai

"Duomenys iš „ID Vilnius“ apie Vilniaus miesto planus, žemėlapius, ortografines nuotraukas ir kitą kartografinę medžiagą. Viena lentelės eilutė yra vienas žemėlapis (kartografinis objektas). Eilutės informaciją sudaro žemėlapio identifikacinis numeris, pavadinimas, autorius, sudarymo data, aprašymas, grupė, tipas, mastelis, šaltinis, šaltinio, žemėlapio ir legendos nuorodos."[^manifest]

- **Model:** `datasets/gov/id_vilnius/vilniaus_dnr/Zemelapis`[^manifest]
- **Dataset:** [Vilniaus miesto istoriniai duomenys - Vilniaus DNR](../vilniaus_dnr.md) (`datasets/gov/id_vilnius/vilniaus_dnr`)[^manifest]
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L91](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L91)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/Zemelapis` (`deployed`)[^manifest]
- **Provider:** `id_vilnius`[^manifest]
- **Primary Key (`ref`):** `zemelapio_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `zemelapio_id` | `string` | — | `4` | `open` | — | Žemėlapio identifikacinis numeris (pirminis raktas) | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Žemėlapio pavadinimas | — |
| `autorius` | `string` | — | `4` | `open` | — | Žemėlapio sudarytojas | — |
| `sudarymo_data_txt` | `string` | — | `3` | `open` | — | Žemėlapio sudarymo metai (amžius) tekstiniu formatu | — |
| `sudarymo_data` | `date` | `Y` | `4` | `open` | — | Žemėlapio sudarymo data | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Žemėlapio aprašymas | — |
| `grupe` | `string` | — | `4` | `open` | — | Žemėlapio grupė | — |
| `tipas` | `string` | — | `4` | `open` | — | Žemėlapio tipas | — |
| `mastelis` | `string` | — | `4` | `open` | — | Žemėlapio mastelis | — |
| `saltinis` | `string` | — | `3` | `open` | — | Žemėlapio šaltinio pavadinimas | — |
| `saltinio_nuoroda` | `string` | — | `4` | `open` | — | Nuoroda į žemėlapio šaltinį | — |
| `zemelapio_nuoroda` | `string` | — | `4` | `open` | — | Nuorodą į žemėlapį | — |
| `legendos_nuoroda` | `string` | — | `4` | `open` | — | Nuoroda į žemėlapio legendą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L91 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L91)
