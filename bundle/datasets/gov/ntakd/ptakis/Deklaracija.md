---
type: Table
title: "Deklaracija — Kontroliuojamų medžiagų deklaracijų duomenys"
description: "Narkotikų, tabako ir alkoholio kontrolės departamento (NTAKD) naudojama Pirmtakų teisėtos apyvartos kontrolės informacinė sistema (PTAKIS) kaupia juridinių bei fizinių asmenų narkotinių pirmtakų (prekursorių) deklaracijas."
resource: "https://get.data.gov.lt/datasets/gov/ntakd/ptakis/Deklaracija"
tags: [gov, ntakd, deklaracija, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/prekursoriai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/ntakd/prekursoriai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2822/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ntakd/ptakis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Deklaracija — Kontroliuojamų medžiagų deklaracijų duomenys

Narkotikų, tabako ir alkoholio kontrolės departamento (NTAKD) naudojama Pirmtakų teisėtos apyvartos kontrolės informacinė sistema (PTAKIS) kaupia juridinių bei fizinių asmenų narkotinių pirmtakų (prekursorių) deklaracijas. Duomenys kaupiami nuo 2021-04-01 ir atnaujinami iki šiol. Duomenų rinkinys sudarytas iš pseudonimizuoto deklaravusio fizinio arba juridinio asmens (deklaranto) kodo, deklaranto asmens rūšies, ataskaitos formos, deklaruotos medžiagos pavadinimo, paskirties ir kiekių deklaracijos periodo pradžioje ir pabaigoje, deklaracijos periodo metų ir deklaracijos numerio tais metais. Vienas įrašas atitinka vieną deklaranto, medžiagos, deklaracijos metų ir periodo numerio kombinaciją. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/ntakd/ptakis/Deklaracija`[^manifest]
- **Dataset:** [Kontroliuojamų medžiagų deklaracijų duomenys](../ptakis.md) (`datasets/gov/ntakd/ptakis`)[^manifest]
- **Manifest CSV:** [datasets/gov/ntakd/prekursoriai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/prekursoriai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntakd/ptakis/Deklaracija` (`deployed`)[^manifest]
- **Provider:** `ntakd` — Narkotikų, tabako ir alkoholio kontrolės departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `deklaranto_kodas` | `string` | — | `4` | `open` | — | Deklaraciją pateikusio asmens pseudonimizuotas kodas | — |
| `deklaranto_asmens_rusis` | `string` | — | `4` | `open` | — | Deklaraciją pateikusio asmens rūšis | — |
| `medziaga` | `string` | — | `4` | `open` | — | Deklaruota medžiaga | — |
| `ataskaitos_forma` | `string` | — | `4` | `open` | — | Deklaracijos ataskaitos forma | — |
| `paskirtis` | `string` | — | `4` | `open` | — | Deklaruotos medžiagos paskirtis | — |
| `kiekis_periodo_pradzioje` | `number` | — | `4` | `open` | — | Medžiagos kiekis deklaracijos periodo pradžioje | — |
| `kiekis_periodo_pabaigoje` | `number` | — | `4` | `open` | — | Medžiagos kiekis deklaracijos periodo pabaigoje | — |
| `mato_vienetas` | `string` | — | `4` | `open` | — | Deklaruotos medžiagos matavimo vienetas | — |
| `dekl_periodo_metai` | `integer` | — | `4` | `open` | — | Deklaracijos periodo metai | — |
| `dekl_periodo_nr` | `integer` | — | `4` | `open` | — | Deklaracijos numeris esamais metais | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `deklaranto_asmens_rusis` | `"Juridinis"` | — | — | LR juridinis asmuo | — |
| `deklaranto_asmens_rusis` | `"Fizinis"` | — | — | LR fizinis asmuo | — |
| `deklaranto_asmens_rusis` | `"Nežinoma"` | — | — | Nei LR juridinis, nei LR fizinis asmuo | — |
| `mato_vienetas` | `"kg"` | — | — | Kilogramai | — |
| `mato_vienetas` | `"l"` | — | — | Litrai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntakd/prekursoriai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/prekursoriai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ntakd/ptakis (https://data.gov.lt/datasets/2822/)
