---
type: Table
title: "Produktas — Pateikiama informacija apie Lietuvos Respublikoje registruotus augalų apsaugos produktus"
description: "Spinta table datasets/gov/vat/registruoti_aap/Produktas (50 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/registruoti_aap/Produktas"
tags: [gov, vat, produktas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r33_registruoti_aap.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r33_registruoti_aap.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1889/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/registruoti_aap"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Produktas — Pateikiama informacija apie Lietuvos Respublikoje registruotus augalų apsaugos produktus

- **Model:** `datasets/gov/vat/registruoti_aap/Produktas`[^manifest]
- **Dataset:** [Informacija apie Lietuvos Respublikoje registruotus augalų apsaugos produktus](../registruoti_aap.md) (`datasets/gov/vat/registruoti_aap`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r33_registruoti_aap.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r33_registruoti_aap.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/registruoti_aap/Produktas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `produktas` | `string` | — | `4` | `open` | — | AAP pavadinimas | Bendroji informacija |
| `savininkas` | `string` | — | `1` | `open` | — | AAP registracijos savininkas | Bendroji informacija |
| `atstovas` | `string` | — | `1` | `open` | — | AAP registracijos savininko atstovas | Bendroji informacija |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Registravimo Nr. Lietuvoje | Registracijos duomenys |
| `registracijos_atnaujinimas` | `string` | — | `2` | `open` | — | Registracijos atnaujinimo data | — |
| `registracijos_pradzia` | `string` | — | `2` | `open` | — | AAP registracijos data | Registracijos duomenys |
| `registracijos_pabaiga` | `string` | — | `2` | `open` | — | AAP registracijos pabaigos data | Registracijos duomenys |
| `naudoti_iki` | `string` | — | `2` | `open` | — | Pasibaigus registracijai naudoti iki | Registracijos duomenys |
| `prekiauti_iki` | `string` | — | `2` | `open` | — | Pasibaigus registracijai prekiauti iki | Registracijos duomenys |
| `medziagos_aprasymas` | `string` | — | `2` | `open` | — | Cheminė medžiaga / Mikroorganizmas | Cheminės medžiagos / Mikroorganizmo suformuotas aprašymas |
| `veiklioji_medziaga` | `string` | — | `4` | `open` | — | Cheminė medžiaga / Mikroorganizmas | — |
| `veikimo_grupe` | `string` | — | `3` | `open` | — | Veikimo grupė | Veikimo grupių suformuotas aprašymas |
| `aap_tipas` | `string` | — | `4` | `open` | — | Augalų apsaugos produkto tipas | — |
| `augalas` | `string` | — | `3` | `open` | — | Lietuviškas augalo pavadinimas | Numatomi naudojimai (GAP) |
| `kenksmingas_organizmas` | `string` | — | `2` | `open` | — | Lietuviški kenksmingųjų organizmų pavadinimai | Numatomi naudojimai (GAP) |
| `numatomas_naudojimas` | `string` | — | `4` | `open` | — | Naudotojas | Numatomi naudojimai (GAP) |
| `naudojimo_budas` | `string` | — | `2` | `open` | — | Naudojimo būdas | Naudojimo būdų suformuotas aprašymas |
| `naudojimo_plotas` | `string` | — | `4` | `open` | — | Maži / dideli plotai | Numatomi naudojimai (GAP) |
| `produkto_forma` | `string` | — | `3` | `open` | — | Produkto forma | Bendroji informacija |
| `platintojas` | `string` | — | `1` | `open` | — | Platinojas | Bendroji informacija |
| `pakuote` | `string` | — | `1` | `open` | — | Produkto pakuotės | Bendroji informacija |
| `pastaba` | `string` | — | `2` | `open` | — | Pastabos | Bendroji informacija |
| `medz_cas_nr` | `string` | — | `4` | `open` | — | Medžiagos CAS Nr. / Mikroorganizmo Nr. | Veiklioji medžiaga |
| `veikl_medz_kiekis` | `string` | — | `2` | `open` | — | Veikliosios medžiagos kiekis | Veiklioji medžiaga |
| `matavimo_vienetai` | `string` | — | `2` | `open` | — | Veikliosios medžiagos matavimo vienetai | Veiklioji medžiaga |
| `klasifikavimas` | `string` | — | `2` | `open` | — | Klasifikavimas ir etiketė | — |
| `pavojaus_fraze` | `string` | — | `2` | `open` | — | Pavojaus frazė | Klasifikavimas ir etiketė |
| `ghs_piktograma` | `string` | — | `2` | `open` | — | GHS piktograma | Klasifikavimas ir etiketė |
| `atsargumo_fraze` | `string` | — | `2` | `open` | — | Atsargumo frazės | Klasifikavimas ir etiketė |
| `signalinis_zodis` | `string` | — | `4` | `open` | — | Signalinis žodis | Klasifikavimas ir etiketė |
| `papildomas_sakinys` | `string` | — | `2` | `open` | — | Papildomas sakinys | Klasifikavimas ir etiketė |
| `tipas` | `string` | — | `4` | `open` | — | Tipas | Numatomi naudojimai (GAP) |
| `naudojimo_tipas` | `string` | — | `3` | `open` | — | Naudojimo tipas | Numatomi naudojimai (GAP) |
| `naudojimo_laikas` | `string` | — | `2` | `open` | — | Naudojimo laikas | Numatomi naudojimai (GAP) |
| `augalo_eppo` | `string` | — | `2` | `open` | — | Lotyniškas augalo pavadinimas ir EPPO kodas | Numatomi naudojimai (GAP) |
| `augalas_pap` | `string` | — | `2` | `open` | — | Lietuviškas augalo pavadinimas (papildomas) | Numatomi naudojimai (GAP) |
| `kenksm_org_eppo` | `string` | — | `2` | `open` | — | Lotyniški kenksmingų organizmų pavadinimai ir EPPO kodai | Numatomi naudojimai (GAP) |
| `kenksm_organizmas` | `string` | — | `2` | `open` | — | Lietuviški kenksmingųjų organizmų pavadinimai (papildomas) | Numatomi naudojimai (GAP) |
| `naudojimu_sk` | `string` | — | `2` | `open` | — | Didžiausias naudojimų skaičius | Numatomi naudojimai (GAP) |
| `naudojimu_intervalas` | `string` | — | `2` | `open` | — | Mažiausias intervalas tarp naudojimų (dienomis) | Numatomi naudojimai (GAP) |
| `naudojimo_norma` | `string` | — | `2` | `open` | — | Naudojimo norma | Numatomi naudojimai (GAP) |
| `naudojimo_normos_vnt` | `string` | — | `2` | `open` | — | Naudojimo normos vnt. | Numatomi naudojimai (GAP) |
| `vandens_kiekis` | `string` | — | `2` | `open` | — | Vandens kiekis l/ha | Numatomi naudojimai (GAP) |
| `karencijos_laikotarpis` | `string` | — | `2` | `open` | — | Karencijos laikotarpis dienomis | Numatomi naudojimai (GAP) |
| `naudojimo_pastaba` | `string` | — | `2` | `open` | — | Pastabos | Numatomi naudojimai (GAP) |
| `apribojimas` | `string` | — | `2` | `open` | — | Naudojimo apribojimai | Numatomi naudojimai (GAP) |
| `reglamento_keitimas` | `string` | — | `2` | `open` | — | AAP reglamento keitimo data | Registracijos duomenys |
| `isakymo_registravimas` | `string` | — | `2` | `open` | — | VATŽŪM direktoriaus įsakymo dėl AAP registravimo data | Registracijos duomenys |
| `isakymo_nr` | `string` | — | `4` | `open` | — | VATŽŪM direktoriaus įsakymo dėl AAP registravimo registracijos numeris | Registracijos duomenys |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiklioji_medziaga` | `"Cheminė medžiaga"` | — | — | — | — |
| `veiklioji_medziaga` | `"Mikroorganizmas"` | — | — | — | — |
| `aap_tipas` | `"CHEMINIS"` | — | — | — | — |
| `aap_tipas` | `"MIKROBIOLOGINIS"` | — | — | — | — |
| `numatomas_naudojimas` | `"PROFESIONALIAJAM_NAUDOJIMUI"` | — | — | — | — |
| `numatomas_naudojimas` | `"NEPROFESIONALIAJAM_NAUDOJIMUI"` | — | — | — | — |
| `naudojimo_plotas` | `"DIDELIAIS_PLOTAIS"` | — | — | — | — |
| `naudojimo_plotas` | `"MAZAIS_PLOTAIS"` | — | — | — | — |
| `signalinis_zodis` | `"Atsargiai"` | — | — | — | — |
| `signalinis_zodis` | `"Pavojinga"` | — | — | — | — |
| `signalinis_zodis` | `"Be signalinio žodžio"` | — | — | — | — |
| `tipas` | `"CHEMINE_MEDZIAGA"` | — | — | — | — |
| `tipas` | `"MIKOORGANIZMAS"` | — | — | — | — |
| `tipas` | `"PREPARATAS_SEKLU_APDOROJIMUI"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r33_registruoti_aap.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r33_registruoti_aap.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/registruoti_aap (https://data.gov.lt/datasets/1889/)
