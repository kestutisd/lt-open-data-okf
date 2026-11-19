---
type: Table
title: "Muitine — Prekių saugojimo ir muitinio tikrinimo vietos, pripažintos tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti"
description: "Pateikiama informacija apie prekių saugojimo ir muitinio tikrinimo vietas, pripažintas tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto pavadinimas; sandėlio / terminalo tipas ir..."
resource: "https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos/Muitine"
tags: [gov, vat, muitine, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/tikrinimo_vietos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1857/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/tikrinimo_vietos"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Muitine — Prekių saugojimo ir muitinio tikrinimo vietos, pripažintos tinkamomis augalams, augaliniams produktams ir kitiems susijusiems...

**Dataset Context:** Pateikiama informacija apie prekių saugojimo ir muitinio tikrinimo vietas, pripažintas tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto pavadinimas; sandėlio / terminalo tipas ir numeris; sandėlio / terminalo adresas) Pateikiama informacija apie Patikrinimo vietas, pripažintas tinkamomis atlikti fitosanitarinį tikrinimą įvežamiems į Lietuvos Respubliką ir Europos Sąjungą augalams, augaliniams produktams ir kitiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto pavadinimas; sandėlio / terminalo adresas)[^manifest]

- **Model:** `datasets/gov/vat/tikrinimo_vietos/Muitine`[^manifest]
- **Dataset:** [Informacija apie įvežamų augalų, augalinių produktų ir kitų objektų saugojimo ir muitinio...](../tikrinimo_vietos.md) (`datasets/gov/vat/tikrinimo_vietos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/tikrinimo_vietos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos/Muitine` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eil. Nr. | — |
| `pazymejimo_isdavimas` | `date` | `D` | `4` | `open` | — | Pažymėjimo išdavimo data | — |
| `pazymejimo_nr` | `string` | — | `4` | `open` | — | Pažymėjimo numeris | — |
| `terminalas` | `ref` | [AdresoTaskas](../../rc/ar/adresotaskas/AdresoTaskas.md) (`level=3`: `terminalas.aob_kodas`) | `3` | `open` | — | Sandėlio / terminalo adresas | — |
| `tipo_nr` | `string` | — | `1` | `open` | — | Sandėlio / terminalo tipas ir numeris | — |
| `ukio_subjektas` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=2` scalar) | `2` | `open` | — | Ūkio subjektas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/tikrinimo_vietos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/tikrinimo_vietos (https://data.gov.lt/datasets/1857/)
