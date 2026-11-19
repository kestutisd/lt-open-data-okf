---
type: Table
title: "VandensNaudojimas — Metinių vandens naudojimo apskaitos ataskaitų duomenys"
description: "Spinta table datasets/gov/aaa/vandens_naudojimas/VandensNaudojimas (23 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/vandens_naudojimas/VandensNaudojimas"
tags: [gov, aaa, vandensnaudojimas, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/vandens_naudojimas.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/aaa/vandens_naudojimas.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1783/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/vandens_naudojimas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# VandensNaudojimas — Metinių vandens naudojimo apskaitos ataskaitų duomenys

- **Model:** `datasets/gov/aaa/vandens_naudojimas/VandensNaudojimas`[^manifest]
- **Dataset:** [Metinių vandens naudojimo apskaitos ataskaitų duomenys](../vandens_naudojimas.md) (`datasets/gov/aaa/vandens_naudojimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/vandens_naudojimas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/vandens_naudojimas.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/vandens_naudojimas/VandensNaudojimas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės nr. | — |
| `atsisk_data_nuo` | `integer` | — | `2` | `open` | — | Data (metai), už kurią yra teikiamas dokumentas. | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė | — |
| `jar_kodas` | `string` | — | `2` | `open` | — | Įmonės JAR kodas | Juridinis asmuo sunaudojęs vandenį |
| `objektas` | `string` | — | `3` | `open` | — | Ataskaitinio objekto pavadinimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Ataskaitinio objekto adresas | — |
| `vand_sal_kodas` | `string` | — | `3` | `open` | — | Vandens šaltinio kodas | — |
| `vandens_rusis` | `string` | — | `3` | `open` | — | Vandens rūšies pavadinimas | — |
| `vand_sal_pavad` | `string` | — | `3` | `open` | — | Vandens šaltinio pavadinimas | — |
| `koord` | `geometry(point, 3346)` | — | `2` | `open` | — | Vandens telkinio koordinatės (LKS-94) | — |
| `telkinys` | `string` | — | `2` | `open` | — | Vandens telkinio pavadinimas | — |
| `telkinys_graktas` | `string` | — | `2` | `open` | — | Vandens telkinio kodas (GRPK graktas) | — |
| `tiekejas` | `string` | — | `2` | `open` | — | Vandens tiekėjas (JAR kodas) | Juridinis asmuo tiekiantis vandenį |
| `paimta_viso` | `number` | — | `3` | `open` | — | Bendras išgauto ir / arba iš kitų asmenų gauto vandens kiekis (pagal skaitliukų parodymus), tūkst. m3. | — |
| `sunaudota_viso` | `number` | — | `3` | `open` | — | Bendras sunaudoto vandens kiekis, tūkst. m3. | — |
| `sunaudota_ausinimui` | `number` | — | `3` | `open` | — | Aušinimui sunaudoto vandens kiekis, tūkst. m3. | — |
| `patiekta_viso` | `number` | — | `3` | `open` | — | Bendras patiekto vandens kiekis, tūkst. m3. | — |
| `patiekta_panaudoto` | `number` | — | `3` | `open` | — | Patiekto panaudoto vandens kiekis, tūkst. m3. | — |
| `patiekta_gyventojams` | `number` | — | `3` | `open` | — | Bendras patiekto gyventojams vandens kiekis, tūkst. m3. | — |
| `nuostoliai_viso` | `number` | — | `3` | `open` | — | Bendras vandens nuostolių kiekis, tūkst. m3. | — |
| `nuost_panaudoto` | `number` | — | `3` | `open` | — | Vandens nuostoliai tiekiant panaudotą vandenį, tūkst. m3. | — |
| `sutaupyta_viso` | `number` | — | `3` | `open` | — | Bendras įmonės viduje sutaupyto vandens kiekis, tūkst. m3. | — |
| `sutaupyta_ausinimui` | `number` | — | `3` | `open` | — | Įmonės viduje sutaupyto vandens, skirto aušinimui, kiekis, tūkst. m3. | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atsisk_data_nuo` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `savivaldybe` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | — | — | — | — |
| `jar_kodas` | `update(property: "jar_kodas.ja_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `tiekejas` | `update(property: "tiekejas.ja_kodas", type: "")` | `type` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/vandens_naudojimas.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/vandens_naudojimas.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/vandens_naudojimas (https://data.gov.lt/datasets/1783/)
