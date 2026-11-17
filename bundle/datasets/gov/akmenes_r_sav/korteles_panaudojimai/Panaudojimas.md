---
type: Table
title: "Panaudojimas — Akmeniečio kortelės panaudojimai"
description: "Informacija apie Akmenės rajono savivaldybės išduotos Akmeniečio kortelės panaudojimus"
resource: "https://get.data.gov.lt/datasets/gov/akmenes_r_sav/korteles_panaudojimai/Panaudojimas"
tags: [gov, akmenes_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Panaudojimas — Akmeniečio kortelės panaudojimai

Informacija apie Akmenės rajono savivaldybės išduotos Akmeniečio kortelės panaudojimus

- **Model:** `datasets/gov/akmenes_r_sav/korteles_panaudojimai/Panaudojimas`[^manifest]
- **Dataset:** [Akmeniečio kortelės panaudojimai](../korteles_panaudojimai.md) (`datasets/gov/akmenes_r_sav/korteles_panaudojimai`)
- **Manifest CSV:** [datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/akmenes_r_sav/korteles_panaudojimai/Panaudojimas`
- **Primary Key (`ref`):** `panaudojimo_id`
- **Level:** `4`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/akmenes_r_sav/korteles_panaudojimai.csv
