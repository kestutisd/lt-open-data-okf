---
type: Table
title: "Panaudojimas — Akmeniečio kortelės panaudojimai"
description: "Informacija apie Akmenės rajono savivaldybės išduotos Akmeniečio kortelės panaudojimus"
resource: "https://get.data.gov.lt/datasets/gov/akmenes_r_sav/korteles_panaudojimai/Panaudojimas"
tags: [gov, akmenes_r_sav, panaudojimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4133/"
    title: "data.gov.lt DCAT-AP — datasets/gov/akmenes_r_sav/korteles_panaudojimai"
    author: "team:vda"
    last_modified: "2026-10-23T00:00:00Z"
---

# Panaudojimas — Akmeniečio kortelės panaudojimai

Informacija apie Akmenės rajono savivaldybės išduotos Akmeniečio kortelės panaudojimus[^manifest]

- **Model:** `datasets/gov/akmenes_r_sav/korteles_panaudojimai/Panaudojimas`[^manifest]
- **Dataset:** [Akmeniečio kortelės panaudojimai](../korteles_panaudojimai.md) (`datasets/gov/akmenes_r_sav/korteles_panaudojimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/akmenes_r_sav/korteles_panaudojimai/Panaudojimas` (`deployed`)[^manifest]
- **Provider:** `akmenes_r_sav` — Akmenės rajono savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `panaudojimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-23`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `panaudojimo_id` | `string` | — | `4` | `open` | — | Kortelės panaudojimo identifikatorius | — |
| `panaudojimo_laikas` | `datetime` | — | `4` | `open` | — | Kortelės panaudojimo laikas | — |
| `suteikta_nuolaida` | `number` | — | `4` | `open` | — | Suteikta nuolaida paslaugai panaudojus kortelę | — |
| `naudotojo_asmens_kodas` | `string` | — | `4` | `open` | — | Kortelės naudotojo asmens kodas | — |
| `vda_kortele_panaikinta` | `boolean` | — | `4` | `open` | — | Požymis ar Akmeniečio kortelė panaikinta | — |
| `vda_ak_validacija` | `string` | — | `4` | `open` | — | VDA asmens kodo validacija | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Kortelės naudotojo vardas ir pavardė | — |
| `naudotojo_lytis` | `string` | — | `4` | `open` | — | Kortelės naudotojo lytis | — |
| `naudotojo_grupe` | `string` | — | `4` | `open` | — | Kortelės naudotojo grupė | — |
| `vda_amziaus_grupe` | `string` | — | `4` | `open` | — | VDA nustatyta kortelės naudotojo amžiaus grupė | — |
| `qr_kodas` | `string` | — | `4` | `open` | — | Naudotojo kortelės QR kodo numeris | — |
| `imones_pavadinimas` | `string` | — | `4` | `open` | — | Įmonės (arba teikiamos paslaugos) pavadinimas | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės (juridinio asmens) kodas | — |
| `vda_jar_kodo_validacija` | `string` | — | `4` | `open` | — | VDA juridinio asmens kodo validacija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vda_ak_validacija` | `"Nenustatytas asmuo"` | — | — | — | — |
| `vda_ak_validacija` | `"Fizinis asmuo"` | — | — | — | — |
| `vda_ak_validacija` | `"Juridinis asmuo"` | — | — | — | — |
| `naudotojo_lytis` | `"Vyras"` | — | — | — | — |
| `naudotojo_lytis` | `"Moteris"` | — | — | — | — |
| `naudotojo_grupe` | `"Gyventojas"` | — | — | — | — |
| `naudotojo_grupe` | `"Senjoras"` | — | — | — | — |
| `naudotojo_grupe` | `"Vaikas"` | — | — | — | — |
| `vda_jar_kodo_validacija` | `"Nenustatytas asmuo"` | — | — | — | — |
| `vda_jar_kodo_validacija` | `"Fizinis asmuo"` | — | — | — | — |
| `vda_jar_kodo_validacija` | `"Juridinis asmuo"` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/akmenes_r_sav/korteles_panaudojimai (https://data.gov.lt/datasets/4133/)
