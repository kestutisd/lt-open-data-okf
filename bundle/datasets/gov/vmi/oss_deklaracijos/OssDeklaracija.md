---
type: Table
title: "OssDeklaracija — OSS Deklaracijoas"
description: "One Stop Shop (OSS) - tai sistema, kuri palengvina mokestinių PVM prievolių vykdymą ūkio subjektams, parduodantiems neapmokestinamiesiems asmenims tam tikras prekes ar paslaugas, už kurias PVM turėtų būti sumokėtas kitoje valstybėje narėje tais atvejais, kai veikla apima..."
resource: "https://get.data.gov.lt/datasets/gov/vmi/oss_deklaracijos/OssDeklaracija"
tags: [gov, vmi, ossdeklaracija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/oss.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/oss.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1910/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/oss_deklaracijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# OssDeklaracija — OSS Deklaracijoas

One Stop Shop (OSS) - tai sistema, kuri palengvina mokestinių PVM prievolių vykdymą ūkio subjektams, parduodantiems neapmokestinamiesiems asmenims tam tikras prekes ar paslaugas, už kurias PVM turėtų būti sumokėtas kitoje valstybėje narėje tais atvejais, kai veikla apima daugiau nei vienos ES valstybės narės teritoriją. Ūkio subjektai, besinaudojantys sistema, registruojasi, deklaruoja ir moka PVM vienoje valstybėje narėje, neatsižvelgdami į tai, kad paslaugas teikia ir (ar) prekes tiekia keliose ES valstybėse narėse.[^manifest]

- **Model:** `datasets/gov/vmi/oss_deklaracijos/OssDeklaracija`[^manifest]
- **Dataset:** [OSS specialiųjų schemų naudotojų deklaracijų duomenys](../oss_deklaracijos.md) (`datasets/gov/vmi/oss_deklaracijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/oss.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/oss.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/oss_deklaracijos/OssDeklaracija` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `dalyvio_id` | `integer` | — | `4` | `open` | — | OSS dalyvio identifikatorius | — |
| `pvm_nr_id` | `string` | — | `4` | `open` | — | Mokesčių mokėtojo ID OSS sistemoje | — |
| `pvm_kodo_valstybe` | `string` | — | `2` | `open` | — | Valstybė,suteikusi PVM mokėtojo kodą | — |
| `moketojo_kodo_valstybe` | `string` | — | `2` | `open` | — | Valstybė, suteikusi mokesčių mokėtojo kodą | — |
| `veiklos_salis` | `string` | — | `2` | `open` | — | Verslo vietos šalis | — |
| `registracijos_schema` | `string` | — | `4` | `open` | — | Schemos požymis | — |
| `reg_statusas` | `string` | — | `4` | `open` | — | Registracijos statuso požymio pavadinimas | — |
| `veiklos` | `string` | — | `4` | `open` | — | Veikla | — |
| `patvirtinimo_pasirinkimas` | `integer` | — | `4` | `open` | — | Registracijos metu pasirinktas patvirtinimo požymis dėl vertės viršijimo | — |
| `tiekimo_pozymis` | `string` | — | `4` | `open` | — | Tiekimo požymis | — |
| `dek_statusas` | `integer` | — | `4` | `open` | — | Deklaracijos statusas | — |
| `pateikimo_data` | `date` | `D` | `4` | `open` | — | Duomenų įrašymo į lentelę data (sysdate) | — |
| `metai` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio metai | — |
| `ketvirtis` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio ketvirtis | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio mėnuo | — |
| `dek_salis` | `string` | — | `2` | `open` | — | Vartojimo valstybė narė | — |
| `apmokestinta_verte` | `number` | — | `2` | `open` | — | Apmokestinamoji vertė | — |
| `pvm_suma` | `number` | — | `2` | `open` | — | PVM suma | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `registracijos_schema` | `"ES"` | — | — | ES prievolė | ES schema skirta prievolių, susijusių su Europos Sąjungos vidaus nuotoline prekyba prekėmis, prekių tiekimo valstybėje narėje naudojant elektronines sąsajas, kuriomis sudaromos sąlygos tiekti prekes, ir paslaugų, kurias teikia Europos Sąjungoje, tačiau ne vartojimo valstybėje narėje įsisteigę apmokestinamieji asmenys, įvykdymui. |
| `registracijos_schema` | `"Importo"` | — | — | ES supaprastinta PVM prievolė | Importo schema naudojama, siekiant supaprastintai įvykdyti PVM prievoles, susijusias su nuotoline prekybai iš trečiųjų teritorijų ar trečiųjų valstybių importuojamomis prekėmis. Ši schema dar gali būti vadinama IOSS. |
| `registracijos_schema` | `"non-ES"` | — | — | Veikla trečiųjų valstybių importui | Ne ES schema skirta Europos Sąjungoje neįsikūrusiems asmenims, kurie teikia paslaugas neapmokestinamiesiems asmenims, kai tokių paslaugų suteikimo vieta yra atitinkama Europos Sąjungos valstybė narė. |
| `reg_statusas` | `"Received"` | — | — | Priimta | — |
| `reg_statusas` | `"Approved"` | — | — | Patvirtinta | — |
| `reg_statusas` | `"Rejected"` | — | — | Atmesta | — |
| `reg_statusas` | `"Cancelled"` | — | — | Ištrinta | — |
| `reg_statusas` | `"Processing"` | — | — | Apdorojama | — |
| `veiklos` | `"T"` | — | — | T - telekomunikacijos | T - telekomunikacijų, radijo ir televizijos transliavimo ar elektroniniu būdu teikiamos paslaugos |
| `veiklos` | `"K"` | — | — | K - kitos paslaugos | K - kitos paslaugos nei telekomunikacijų, radijo ir televizijos transliavimo ar elektroniniu būdu teikiamos paslaugos, kai tokių kitų paslaugų teikimui taikomos PVM įstatymo XII skyriaus Šeštojo skirsnio nuostatos |
| `veiklos` | `"P"` | — | — | P - ES nuotolinė prekyba | P - ES vidaus nuotolinė prekyba prekėmis |
| `veiklos` | `"TP"` | — | — | T ir P deklaruotos veiklos | — |
| `veiklos` | `"KP"` | — | — | K ir P deklaruotos veiklos | — |
| `veiklos` | `"TKP"` | — | — | T, K, P deklaruotos veiklos | — |
| `patvirtinimo_pasirinkimas` | `1` | — | — | Paslaugos, prekės virsija 10000 | Telekomunikacijų, radijo ir televizijos transliavimo ar elektroniniu būdu teikiamų paslaugų ir / ar ES vidaus nuotolinės prekybos prekių tiekimo vertė (neįskaitant PVM) viršijo 10 000 eurų |
| `patvirtinimo_pasirinkimas` | `2` | — | — | Paslaugos, prekės nevirsija 10000 | Telekomunikacijų, radijo ir televizijos transliavimo ar elektroniniu būdu teikiamų paslaugų ir / ar ES vidaus nuotolinės prekybos prekių tiekimo vertė (neįskaitant PVM) neviršijo 10 000 eurų, tačiau noriu pasinaudoti PVM įstatymo 13² straipsnio 2 dalyje nustatyta galimybe |
| `tiekimo_pozymis` | `"GOODS"` | — | — | GOODS – Prekės | — |
| `tiekimo_pozymis` | `"SERVICES"` | — | — | SERVICES – Paslaugos | — |
| `dek_statusas` | `6` | — | — | Teisinga | — |
| `dek_statusas` | `7` | — | — | Priimta su klaidomis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apmokestinta_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `pvm_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/oss.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/oss.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/oss_deklaracijos (https://data.gov.lt/datasets/1910/)
