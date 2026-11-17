---
type: Table
title: "PirmaDialize — Pirmos dializės duomenys"
description: "Pacientų pirmos dializės data (mėnesio tikslumu), dializės tipas."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/PirmaDialize"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L48"
    last_modified: "2026-11-11T14:39:20Z"
---

# PirmaDialize — Pirmos dializės duomenys

Pacientų pirmos dializės data (mėnesio tikslumu), dializės tipas. Vienam asmeniui gali būti registruotos kelios pirmosios dializės datos, nes po atliktos inksto transplantacijos, transplantatui nustojus funkcionuoti, įrašoma nauja dializės pradžios data.

- **Model:** `datasets/gov/lsd/sveikata/inkstu_biopsijos/PirmaDialize`[^manifest]
- **Dataset:** [Pacientų, kuriems atlikta inkstų biopsija, duomenys](../inkstu_biopsijos.md) (`datasets/gov/lsd/sveikata/inkstu_biopsijos`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L48)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/PirmaDialize`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius sudarytas iš stulpelių - asmens_kodas, pirma_dialize, _dializes_tipas |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `dializes_eiles_nr` | `integer` | — | `4` | `open` | — | Dializės eilės numeris | Rodiklis, nurodantis kelintą kartą asmeniui pradedama nauja dializės gydymų serija. Dializės eilės numeris 1 nurodo kada asmuo pirmą kartą gyvenime pradėjo dializės gydymų seriją. Sekantys eilės numeriai nurodo kada dializės gydymų serijos prasidėjo po atitinkamos inkstų transplantacijos. Pvz., Nr. 2 nurodo dializės gydymų seriją po pirmos transplantacijos, Nr. 3 nurodo dializės gydymų seriją po antros transplantacijos ir t.t. |
| `pirma_dialize` | `date` | `M` | `4` | `open` | — | Pirma dializės gydymų serijos diena | — |
| `dializes_tipas` | `string` | — | `4` | `open` | — | Atliekamos dializės tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dializes_tipas` | `"Hemodializė"` | — | — | Hemodializė | — |
| `dializes_tipas` | `"Peritoninė dializė"` | — | — | Peritoninė dializė | — |
| `dializes_tipas` | `"Numatoma"` | — | — | Numatoma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv
