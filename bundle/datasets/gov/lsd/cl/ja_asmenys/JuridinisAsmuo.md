---
type: Table
title: "JuridinisAsmuo — Juridinis Asmuo"
description: "Spinta table datasets/gov/lsd/cl/ja_asmenys/JuridinisAsmuo (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/cl/ja_asmenys/JuridinisAsmuo"
tags: [gov, lsd, juridinisasmuo, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/ja_asmenys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lsd/cl/ja_asmenys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2088/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/cl/ja_asmenys"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# JuridinisAsmuo — Juridinis Asmuo

- **Model:** `datasets/gov/lsd/cl/ja_asmenys/JuridinisAsmuo`[^manifest]
- **Dataset:** [Juridinių asmenų ekonominės veiklos rūšys ir instituciniai sektoriai](../ja_asmenys.md) (`datasets/gov/lsd/cl/ja_asmenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/cl/ja_asmenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/ja_asmenys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/cl/ja_asmenys/JuridinisAsmuo` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-02-25`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas (JA kodas) | Juridinis asmuo, tai įmonė, įstaiga ar organizacija, registruota Juridinių asmenų registre (VĮ Registrų centras, JAR). |
| `pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens pavadinimas (JAR duomuo) | Juridinio asmens pavadinimas (JAR duomuo) |
| `isregistruotas` | `date` | `D` | `4` | `open` | — | Išregistravimo data (JA išregistruotas) | Juridinio asmens išregistravimo data (JAR duomuo) |
| `veikla` | `ref` | [EkonominesVeiklosRusis](../evrk/EkonominesVeiklosRusis.md) (`level=4 UUID`: `veikla._id`) | `4` | `open` | — | Pagrindinės ekonominės veiklos rūšies kodas (Ekonominė veikla) | Juridinių asmenų ekonominė veikla klasifikuojama pagal Ekonominės veiklos rūšių klasifikatorių (EVRK), tai privaloma visiems duomenų teikėjams, kurių duomenys kaip statistinės informacijos šaltiniai apibrėžti Lietuvos Respublikos statistikos įstatyme. Vadovaujantis pagrindinėmis EVRK klasifikavimo taisyklėmis vienetai, vykdantys kelias ekonominės veiklos rūšis, statistikos tikslais klasifikuojami pagal pagrindinę veiklą, sukuriančią didžiausią vieneto bendrosios pridėtinės vertės dalį (pridėtinė vertė išreiškiama skirtumu tarp pagamintos produkcijos ir tarpinio vartojimo), todėl SŪRS nurodomas tik pagrindinės veiklos rūšies kodas. EVRK kodo struktūra yra hierarchinė (t. y. sekcijos, skyriai, grupės, klasės ir poklasiai), leidžianti rinkti statistinius duomenis žemiausiame lygmenyje ir agreguoti į aukštesnį lygmenį. Juridinių asmenų vykdoma pagrindinė veiklos rūšis nurodoma EVRK klasių arba poklasių lygmeniu. |
| `veikla_atnaujinta` | `date` | `D` | `4` | `open` | — | Pagrindinės veiklos rūšies atnaujinimo data (Veiklos atnaujinimo data) | Data, kada paskutinį kartą buvo atnaujintas juridinio asmens pagrindinės veiklos rūšies kodas. |
| `evrk_2_1` | `ref` | [EkonominesVeiklosRusis](../evrk2_1/EkonominesVeiklosRusis.md) (`level=4 UUID`: `evrk_2_1._id`) | `4` | `open` | — | Pagrindinės ekonominės veiklos rūšies kodas atnaujinta versija 2.1(Ekonominė veikla 2.1) | — |
| `evrk_2_1_data` | `date` | `D` | `4` | `open` | — | Pagrindinės veiklos 2.1 rūšies atnaujinimo data (Veiklos atnaujinimo data) | — |
| `evrk_2_1_pavadinimas` | `string` | — | `4` | `open` | — | Pagrindinės veiklos 2.1 rūšies pavadinimas | — |
| `sektorius` | `ref` | [Sektorius](../sektoriai/Sektorius.md) (`level=4 UUID`: `sektorius._id`) | `4` | `open` | — | Institucinis sektorius ir subsektorius (Institucinis sektorius) | Ūkio subjektai (fiziniai ir juridiniai asmenys), kurie gali savarankiškai nuosavybės teise turėti prekių ir turto, prisiimti įsipareigojimus, vykdyti ekonominę veiklą ir sudaryti sandorius su kitais vienetais vadinami instituciniais vienetais. ESS sistemoje instituciniai vienetai skirstomi į penkis tarpusavyje nesidubliuojančius šalies institucinius sektorius. Šie penki sektoriai sudaro visą šalies ekonomiką. Vienetai nerezidentai gali būti susiję su visais šiais penkiais šalies sektoriais ir šios sąsajos pateikiamos kaip šalies sektorių ir šeštojo sektoriaus – likusio pasaulio sektoriaus – ryšiai. Sektoriai skirstomi į subsektorius. Ūkio subjektų instituciniai sektoriai ir subsektoriai nustatomi, tikslinami ir koduojami statistiniame ūkio subjektų registre nuolat remiantis administraciniais ir statistiniais duomenų šaltiniais. Šie duomenysyra informacijos šaltinis valstybės institucijoms, privačioms bendrovėms ir organizacijoms. Jie yra naudojami sudarant nacionalines sąskaitas, mokėjimų balansą, pinigų ir finansų statistikai rengti. |
| `iregistruotas` | `date` | `D` | `4` | `open` | — | Įregistravimo data | Juridinio asmens įregistravimo data (JAR duomuo) |
| `veiklos_pavadinimas` | `string` | — | `4` | `open` | — | Ekonomines veiklos rusies pavadinimas | Juridinio asmens vykdomos ekonomines veiklos rusies pavadinimas |
| `nuosavybes_forma_pavadinimas` | `string` | — | `4` | `open` | — | Nuosavybes formos pavadinimas | — |
| `nuosavybes_forma` | `integer` | — | `4` | `open` | — | Nuosavybės formos | — |
| `veikiantis` | `integer` | — | `4` | `open` | — | Veikiantys reikšmės | Šis požymis nurodo, kad tam tikram momentui, statistinis vienetas yra veikiantis, t.y. vykdo ekonominę veiklą, turi darbuotojų ir (arba) pajamų. Veikiančių statistinių vienetų sąrašas atnaujinamas vieną kartą per metus ir fiksuojamas sausio 1 d. |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `nuosavybes_forma` | `11` | — | — | Viešoji nuosavybė be užsienio kapitalo | Viešoji nuosavybė, kurioje valstybės ar savivaldybės nuosavybė sudaro 50% arba daugiau kaip 50 % subjekto įstatinio kapitalo ir jo sudėtyje nėra užsienio investuotojų kapitalo |
| `nuosavybes_forma` | `12` | — | — | Viešoji nuosavybė su užsienio kapitalu | Viešoji nuosavybė, kurioje valstybės ar savivaldybės nuosavybė sudaro 50% arba daugiau kaip 50 % subjekto įstatinio kapitalo ir jo sudėtyje yra užsienio investuotojų kapitalo |
| `nuosavybes_forma` | `21` | — | — | Privati nuosavybė be užsienio kapitalo | Privati nuosavybė, kurioje Lietuvos fiziniams bei juridiniams asmenims priklauso daugiau kaip 50 % subjekto įstatinio kapitalo ir jo sudėtyje nėra užsienio investuotojų kapitalo |
| `nuosavybes_forma` | `22` | — | — | Privati nuosavybė su užsienio kapitalu | Privati nuosavybė, kurioje Lietuvos fiziniams bei juridiniams asmenims priklauso daugiau kaip 50 % subjekto įstatinio kapitalo ir jo sudėtyje yra užsienio investuotojų kapitalo |
| `nuosavybes_forma` | `23` | — | — | Privati nuosavybė daugiau nei 50% užsienio kapitalo | Privati nuosavybė, kurioje užsienio fizinių bei juridinių asmenų nuosavybė sudaro daugiau kaip 50 % subjekto įstatinio kapitalo |
| `veikiantis` | `1` | — | — | Veikla vykdoma | — |
| `veikiantis` | `0` | — | — | Veikla nevykdoma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(base: "/datasets/gov/rc/jar/JuridinisAsmuo", ref: "kodas")` | `base` | `4` | `open` | — | — | — |
| `(model)` | `update(ref: "kodas")` | `ref` | `4` | `open` | — | — | — |
| `kodas` | `update(property: "kodas", type: "")` | `property, type` | `4` | `open` | — | — | — |
| `pavadinimas` | `update(property: "pavadinimas@lt", type: "")` | `property, type` | `4` | `open` | — | — | — |
| `isregistruotas` | `update(property: "isregistruotas")` | `property, type` | `4` | `open` | — | — | — |
| `veikla_atnaujinta` | `update(property: "veikla_atnaujinta")` | `property, type` | `4` | `open` | — | — | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/cl/ja_asmenys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/ja_asmenys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/cl/ja_asmenys (https://data.gov.lt/datasets/2088/)
