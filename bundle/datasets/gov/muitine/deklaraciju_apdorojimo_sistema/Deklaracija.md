---
type: Table
title: "Deklaracija — Muitinės importo ir eksporto deklaracijų duomenys"
description: "Muitinės importo ir eksporto (reeksporto) deklaracijų prekių rūšių lygio duomenys"
resource: "https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema/Deklaracija"
tags: [gov, muitine, deklaracija, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3996/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/deklaraciju_apdorojimo_sistema"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Deklaracija — Muitinės importo ir eksporto deklaracijų duomenys

Muitinės importo ir eksporto (reeksporto) deklaracijų prekių rūšių lygio duomenys[^manifest]

- **Model:** `datasets/gov/muitine/deklaraciju_apdorojimo_sistema/Deklaracija`[^manifest]
- **Dataset:** [Muitinės importo ir eksporto deklaracijų duomenys ir deklaracijų prašomų įforminti procedūrų...](../deklaraciju_apdorojimo_sistema.md) (`datasets/gov/muitine/deklaraciju_apdorojimo_sistema`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema/Deklaracija` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA pirminis raktas | — |
| `deklaracijos_numeris_mrn` | `string` | — | `4` | `open` | — | Deklaracijos numeris MRN | — |
| `eksportuotojo_ar_importuotojo_pavadinimas` | `string` | — | `4` | `open` | — | Eksprtuotojo ar importuotojo pavadinimas | — |
| `eksportuotojo_ar_importuotojo_kodas` | `string` | — | `4` | `open` | — | Eksportuotojo ar importuotojo kodas | — |
| `eksportuotojo_ar_importuotojo_adresas` | `string` | — | `4` | `open` | — | Eksportuotojo ar importuotojo adresas | — |
| `eksportuotojo_ar_importuotojo_salis` | `string` | — | `4` | `open` | — | Eksportuotojo ar importuotojo adreso šalies kodas | — |
| `deklaracijos_iforminimo_metai` | `integer` | — | `4` | `open` | — | Deklaracijos įforminimo metai | — |
| `duomenu_rinkinio_tipas` | `string` | — | `4` | `open` | — | Duomenų rinkinio (deklaracijos) tipas | — |
| `deklaracijos_rusis` | `string` | — | `4` | `open` | — | Deklaracijos rūšis | — |
| `eksporto_paskirties_ar_importo_issiuntimo_salis` | `string` | — | `4` | `open` | — | Eksporto paskirties ar importo išsiuntimo šalis | — |
| `prekes_kilmes_salis` | `string` | — | `4` | `open` | — | Prekės kilmės šalis | — |
| `prasoma_iforminti_procedura` | `string` | — | `4` | `open` | — | Prašoma įforminti procedūra | — |
| `suderintos_sistemos_subpozicijos_kodas` | `string` | — | `4` | `open` | — | Suderintos sistemos subpozicijos kodas | — |
| `kombinuotosios_nomenklaturos_kodas` | `string` | — | `4` | `open` | — | Kombinuotos nomenklatūros kodas | — |
| `taric_kodas` | `string` | — | `4` | `open` | — | TARIC kodas | — |
| `mase_bruto` | `number` | — | `4` | `open` | — | Deklaruojamos prekės bruto masė kilogramais | — |
| `mase_neto` | `number` | — | `4` | `open` | — | Deklaruojamos prekės neto masė kilogramais | — |
| `papildomi_mato_vienetai` | `string` | — | `4` | `open` | — | Papildomi mato vienetai | — |
| `kiekis_papildomais_mato_vnt` | `number` | — | `4` | `open` | — | Kiekis papildomais mato vientetais | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `deklaracijos_rusis` | `"Importo (IM)"` | — | — | Importo deklaracija | — |
| `deklaracijos_rusis` | `"Eksporto (EX)"` | — | — | Eksporto deklaracija | — |
| `deklaracijos_rusis` | `"Specialiųjų priemonių (CO)"` | — | — | Specailiųjų priemonių | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/deklaraciju_apdorojimo_sistema (https://data.gov.lt/datasets/3996/)
