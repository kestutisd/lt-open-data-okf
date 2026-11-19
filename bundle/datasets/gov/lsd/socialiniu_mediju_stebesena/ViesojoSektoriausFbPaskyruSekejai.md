---
type: Table
title: "ViesojoSektoriausFbPaskyruSekejai — Viešojo sektoriaus Facebook paskyrų stebėsena"
description: "Lentelėje pateikiami valstybinių institucijų, įstaigų, tarnybų, agentūrų Facebook paskyrų sekėjų skačiaus stebėsenos rezultatai."
resource: "https://get.data.gov.lt/datasets/gov/lsd/socialiniu_mediju_stebesena/ViesojoSektoriausFbPaskyruSekejai"
tags: [gov, lsd, viesojosektoriausfbpaskyrusekejai, deployed, level-3, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/soc_erdves_stebesena.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/lsd/soc_erdves_stebesena.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2030/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/socialiniu_mediju_stebesena"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ViesojoSektoriausFbPaskyruSekejai — Viešojo sektoriaus Facebook paskyrų stebėsena

Lentelėje pateikiami valstybinių institucijų, įstaigų, tarnybų, agentūrų Facebook paskyrų sekėjų skačiaus stebėsenos rezultatai. Stebėsena vykdyta 2022-07-11, atnaujinimo data šiuo metu nenumatyta. Įtrauktos 99 paskyros. Stebėsena yra skirta viešojo sektoriaus bendravimui su visuomene skatinti, taip pat visuomenės informavimui apie šių paskyrų egzistavimą bei naudą. Pastabos: Ne visos įstaigos turi socialinių medijų paskyras (pvz., Valstybinė lietuvių kalbos komisija). Įstagos gali turėti kelias paskyras (pvz., Lietuvos statistikos departamentas ir Valstybės duomenų analitika). Facebook paskyra gali nepriklausyti vienai konkrečiai įstaigai (pvz., Lietuvos teismai) arba priklausyti nebeegzistuojančiai įstaigai (Valstybinė energetikos inspekcija).[^manifest]

- **Model:** `datasets/gov/lsd/socialiniu_mediju_stebesena/ViesojoSektoriausFbPaskyruSekejai`[^manifest]
- **Dataset:** [Socialinių medijų stebėsena](../socialiniu_mediju_stebesena.md) (`datasets/gov/lsd/socialiniu_mediju_stebesena`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/soc_erdves_stebesena.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/soc_erdves_stebesena.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/socialiniu_mediju_stebesena/ViesojoSektoriausFbPaskyruSekejai` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `url`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `OTHER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `data` | `date` | `D` | `4` | `open` | — | Data | Data, kuomet vykdyta paskyrų stebėsena |
| `jar_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens kodas | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Valstybinės institucijos, įstaigos, tarnybos, agentūros pavadinimas | — |
| `sekeju_sk` | `integer` | — | `4` | `open` | — | Stebimos Facebook paskyros sekėjų ('followers') skaičius | — |
| `url` | `url` | — | `4` | `open` | — | URL adresas | Stebimos Facebook paskyros URL adresas |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar_kodas` | `update(property: "ja_kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `pavadinimas` | `update(property: "ja_pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/soc_erdves_stebesena.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/soc_erdves_stebesena.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/socialiniu_mediju_stebesena (https://data.gov.lt/datasets/2030/)
