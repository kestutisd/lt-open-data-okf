---
type: Table
title: "IsleistuvasTarsa — Metinę nuotekų ataskaitą teikiančio subjekto duomenys dėl išleidžiamų nuotekų (įskaitant kiekius pagal išleistuvą)"
description: "Spinta table datasets/gov/aaa/nuotekos/IsleistuvasTarsa (36 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/nuotekos/IsleistuvasTarsa"
tags: [gov, aaa, isleistuvastarsa, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L64"
    title: "atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv#L64"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1784/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/nuotekos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# IsleistuvasTarsa — Metinę nuotekų ataskaitą teikiančio subjekto duomenys dėl išleidžiamų nuotekų (įskaitant kiekius pagal išleistuvą)

- **Model:** `datasets/gov/aaa/nuotekos/IsleistuvasTarsa`[^manifest]
- **Dataset:** [Metinių nuotekų tvarkymo apskaitos ataskaitų duomenys](../nuotekos.md) (`datasets/gov/aaa/nuotekos`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/nuotekos.csv#L64](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L64)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/nuotekos/IsleistuvasTarsa` (`deployed`)[^manifest]
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
| `nin_nust_budas` | `string` | — | `4` | `open` | — | Nuotekų kiekio nustatymo būdas | — |
| `nin_kit_nuot_rusis` | `string` | — | `3` | `open` | — | Nuotekų rūšies detalizavimas, kai išleidžiamų nuotekų rūšis yra "kita" | — |
| `nin_perd_budas` | `string` | — | `4` | `open` | — | Nuotekų perdavimo būdas | — |
| `inr_kodas` | `string` | — | `4` | `open` | — | Išleidžiamų nuotekų rūšies kodas | — |
| `inr_pavad` | `string` | — | `3` | `open` | — | Išleidžiamų nuotekų rūšies pavadinimas | — |
| `inr_isl_i_gamtine_aplinka` | `string` | — | `2` | `open` | — | Požymis, ar išleidžiama į gamtinę aplinką | — |
| `inr_isl_i_nuotakyna` | `string` | — | `2` | `open` | — | Požymis, ar išleidžiama į nuotakyną | — |
| `nii_laik_nuo` | `date` | `D` | `4` | `open` | — | Nuotekų išleidimo laikotarpio pradžia | — |
| `nii_laik_iki` | `date` | `D` | `4` | `open` | — | Nuotekų išleidimo laikotarpio pabaiga | — |
| `nii_nuot_kiek_ivest` | `number` | — | `3` | `open` | — | Duomenų teikėjo įvestas nuotekų kiekis | Duomenų teikėjo įvestas per nurodytą laikotarpį išleistas nuotekų kiekis |
| `nii_nuot_pobudis` | `string` | — | `4` | `open` | — | Nuotekų pobūdis | — |
| `tin_konc_pries_val_iv` | `number` | — | `3` | `open` | — | Duomenų teikėjo įvesta vidutinė metinė teršalo koncentracija nuotekose prieš valymą | — |
| `tin_konc_nuot_iv` | `number` | — | `3` | `open` | — | Duomenų teikėjo įvesta vidutinė metinė teršalo koncentracija išleidžiamose nuotekose | — |
| `tin_didz_par_konc_iv` | `number` | — | `3` | `open` | — | Duomenų teikėjo įvesta didžiausia momentinė / paros teršalo koncentracija išleidžiamose nuotekose | — |
| `tin_isl_kiek_iv` | `number` | — | `3` | `open` | — | Duomenų teikėjo įvestas su nuotekomis išleistas teršalo kiekis | — |
| `tin_isv_efekt_iv` | `number` | — | `3` | `open` | — | Duomenų teikėjo įvestas teršalo išvalymo efektyvumas | Procentais |
| `tin_met_dlk` | `number` | — | `3` | `open` | — | Teršalo metinė didžiausia leistina koncentracija | — |
| `tin_par_dlk` | `number` | — | `3` | `open` | — | Teršalo paros didžiausia leistina koncentracija | — |
| `tin_met_llt` | `number` | — | `3` | `open` | — | Leidžiamas per metus išleisti teršalo kiekis (leistina metinė tarša) | — |
| `tin_par_llt` | `number` | — | `3` | `open` | — | Leidžiamas per parą išleisti teršalo kiekis (leistina paros tarša ) | — |
| `trs_kodas` | `string` | — | `4` | `open` | — | Teršalo kodas | — |
| `trs_pavad` | `string` | — | `4` | `open` | — | Teršalo pavadinimas | — |
| `mvn_kodas` | `string` | — | `4` | `open` | — | Matavimo vieneto kodas | — |
| `mvn_pavad` | `string` | — | `4` | `open` | — | Matavimo vieneto pavadinimas | — |
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
| `nin_nust_budas` | `"A"` | — | — | Apskaičiuota | — |
| `nin_nust_budas` | `"V"` | — | — | Įvertinta | — |
| `nin_nust_budas` | `"M"` | — | — | Išmatuota prietaisais | — |
| `nin_perd_budas` | `"SURINK"` | — | — | Nuotekų surinkimo sistema | — |
| `nin_perd_budas` | `"ASTR"` | — | — | Asenizaciniu transportu | — |
| `inr_kodas` | `"BN"` | — | — | buitinės nuotekos | — |
| `inr_kodas` | `"GN"` | — | — | gamybinės nuotekos | — |
| `inr_kodas` | `"KN"` | — | — | komunalinės nuotekos | — |
| `inr_kodas` | `"PN"` | — | — | paviršinės nuotekos | — |
| `inr_kodas` | `"ZV"` | — | — | žuvininkystės tvenkinių vanduo | — |
| `inr_kodas` | `"AV"` | — | — | aušinimo vanduo | — |
| `inr_kodas` | `"KT"` | — | — | kita rūšis (nurodyti) | — |
| `nii_nuot_pobudis` | `"ISVAL"` | — | — | išvalytos iki nustatytų normų | — |
| `nii_nuot_pobudis` | `"NEREIK"` | — | — | nereikalaujančios valymo | — |
| `nii_nuot_pobudis` | `"NEPAK"` | — | — | nepakankamai išvalytos | — |
| `nii_nuot_pobudis` | `"NEVA"` | — | — | nevalytos | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_atsisk_data_nuo` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv#L64 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L64)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/nuotekos (https://data.gov.lt/datasets/1784/)
