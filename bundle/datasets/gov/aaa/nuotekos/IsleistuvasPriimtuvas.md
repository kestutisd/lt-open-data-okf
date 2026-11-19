---
type: Table
title: "IsleistuvasPriimtuvas — Išleistuvai į gamt. aplinką, į nuotakyną ir kt. įrenginiai pagal aob_uvo.aob_rusis su priimtuvo (įskaitant vandens telkinius) informacija"
description: "Spinta table datasets/gov/aaa/nuotekos/IsleistuvasPriimtuvas (20 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/nuotekos/IsleistuvasPriimtuvas"
tags: [gov, aaa, isleistuvaspriimtuvas, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L146"
    title: "atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv#L146"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1784/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/nuotekos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# IsleistuvasPriimtuvas — Išleistuvai į gamt. aplinką, į nuotakyną ir kt. įrenginiai pagal aob_uvo.aob_rusis su priimtuvo (įskaitant...

- **Model:** `datasets/gov/aaa/nuotekos/IsleistuvasPriimtuvas`[^manifest]
- **Dataset:** [Metinių nuotekų tvarkymo apskaitos ataskaitų duomenys](../nuotekos.md) (`datasets/gov/aaa/nuotekos`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/nuotekos.csv#L146](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L146)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/nuotekos/IsleistuvasPriimtuvas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aob_id` | `string` | — | `4` | `open` | — | Ataskaitinio objekto id | — |
| `usb_aob_id` | `string` | — | `2` | `open` | — | Ūkio subjekto id | Siejasi su lentele UkioSubjektas, stulpeliu usb_aob_id |
| `aob_aob_id_prikl` | `string` | — | `2` | `open` | — | Priklausomumo objektui id | Siejasi su lentele UkioSubjektas, stulpeliu aob_aob_id_prikl |
| `aob_tipas` | `string` | — | `4` | `open` | — | Ataskaitinio objekto tipas | — |
| `aob_pavad` | `string` | — | `1` | `open` | — | Ataskaitinio objekto pavadinimas | — |
| `aob_kodas` | `string` | — | `3` | `open` | — | Ataskaitinio objekto kodas | — |
| `aob_kategorija` | `string` | — | `4` | `open` | — | Ataskaitinio objekto kategorija | — |
| `aob_rusis` | `string` | — | `4` | `open` | — | Ataskaitinio objekto rūšis | — |
| `aob_gis_taskas` | `geometry(point, 3346)` | — | `3` | `open` | — | Ataskaitinio objekto koordinatės | — |
| `uod_tipas` | `string` | — | `4` | `open` | — | ŪS veiklos objekto tipas | — |
| `uod_tsl_kita_priimt_kateg` | `string` | — | `3` | `open` | — | Priimtuvo kategorijos įvardinimas, kai nurodyta kategorija yra "kita" | — |
| `uod_tsl_atst_iki_ziociu` | `integer` | — | `3` | `open` | — | Atstumas kilometrais nuo upės (upelio) žiočių iki nuotekų išleistuvo | — |
| `uod_tsl_pastabos` | `string` | — | `2` | `open` | — | Kito ūkio subjekto ar jo veiklos objekto, į kurio nuotekų surinkimo sistemą yra išleidžiamos nuotekos, įvardinimas, kai sąvaduose nerandamas reikiamas ŪS ar AOB | — |
| `uod_tsl_upes_krantas` | `string` | — | `3` | `open` | — | Nuotekų išleistuvo upės krantas | — |
| `ivo_ident` | `string` | — | `2` | `open` | — | Paviršinio vandens objekto identifikatorius | — |
| `ivo_pavad` | `string` | — | `2` | `open` | — | Paviršinio vandens objekto pavadinimas | — |
| `prk_kodas` | `string` | — | `4` | `open` | — | Priimtuvo kategorijos identifikacinis kodas | — |
| `prk_pavad` | `string` | — | `3` | `open` | — | Priimtuvo kategorijos pavadinimas | — |
| `dok_atsisk_data_nuo` | `integer` | — | `2` | `open` | — | Data, už kurią yra teikiamas dokumentas. | — |
| `adr_sav_pavad` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `aob_tipas` | `"USB"` | — | — | Ūkio subjektas | — |
| `aob_tipas` | `"UVO"` | — | — | Ūkinės veiklos objektas | — |
| `aob_kategorija` | `"M"` | — | — | Maudykla | — |
| `aob_kategorija` | `"I"` | — | — | Įrenginys | — |
| `aob_kategorija` | `"T"` | — | — | Taršos šaltinis | — |
| `aob_kategorija` | `"V"` | — | — | Vandens šaltinis | — |
| `aob_kategorija` | `"O"` | — | — | Ūkinės veiklos objektas | — |
| `aob_rusis` | `"OI"` | — | — | Oro taršos įrenginys | — |
| `aob_rusis` | `"KI"` | — | — | Kitas įrenginys | — |
| `aob_rusis` | `"IT"` | — | — | Išsklaidytosios oro taršos šaltinis | — |
| `aob_rusis` | `"ST"` | — | — | Sutelktosios oro taršos šaltinis | — |
| `aob_rusis` | `"IG"` | — | — | Išleistuvas į gamtinę aplinką | — |
| `aob_rusis` | `"IN"` | — | — | Išleistuvas į nuotakyną | — |
| `aob_rusis` | `"PV"` | — | — | Paviršinio vandens šaltinis | — |
| `aob_rusis` | `"ZV"` | — | — | Požeminio vandens šaltinis | — |
| `aob_rusis` | `"NV"` | — | — | Nuotekų valymo įrenginys | — |
| `aob_rusis` | `"KV"` | — | — | Iš kitų gaunamo vandens šaltinis | — |
| `uod_tipas` | `"MAU"` | — | — | Maudykla | — |
| `uod_tipas` | `"OTI"` | — | — | Oro / vandens taršos įrenginys | — |
| `uod_tipas` | `"IKS"` | — | — | Iš kitų gaunamo vandens šaltinis | — |
| `uod_tipas` | `"PVS"` | — | — | Paviršinio vandens šaltinis | — |
| `uod_tipas` | `"UVO"` | — | — | Ūkinės veiklos objektas | — |
| `uod_tipas` | `"PZS"` | — | — | Požeminio vandens šaltinis | — |
| `uod_tipas` | `"OTS"` | — | — | Oro taršos šaltinis | — |
| `uod_tipas` | `"NIS"` | — | — | Nuotekų išleistuvas | — |
| `uod_tipas` | `"NVI"` | — | — | Nuotekų valymo įrenginys | — |
| `uod_tipas` | `"KI"` | — | — | Kitas įrenginys | — |
| `prk_kodas` | `"UPE"` | — | — | upė (upelis) | — |
| `prk_kodas` | `"KAN"` | — | — | kanalas | — |
| `prk_kodas` | `"MEL"` | — | — | melioracijos griovys | — |
| `prk_kodas` | `"EZE"` | — | — | ežeras | — |
| `prk_kodas` | `"TVN"` | — | — | tvenkinys | — |
| `prk_kodas` | `"KUD"` | — | — | kūdra | — |
| `prk_kodas` | `"PEL"` | — | — | pelkė | — |
| `prk_kodas` | `"FLT"` | — | — | natūrali nuotekų filtravimo sistema | — |
| `prk_kodas` | `"JUR"` | — | — | Baltijos jūra | — |
| `prk_kodas` | `"MAR"` | — | — | Kuršių marios | — |
| `prk_kodas` | `"KT"` | — | — | kita kategorija (nurodyti) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_atsisk_data_nuo` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv#L146 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L146)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/nuotekos (https://data.gov.lt/datasets/1784/)
