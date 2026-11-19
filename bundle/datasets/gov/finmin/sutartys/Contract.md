---
type: Table
title: "Contract — Projekto sutartis"
description: "Spinta table datasets/gov/finmin/sutartys/Contract (47 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/Contract"
tags: [gov, finmin, contract, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Contract — Projekto sutartis

- **Model:** `datasets/gov/finmin/sutartys/Contract`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/Contract` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `project`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `project` | `ref` | [Project](../paraiskos/Project.md) (`level=4 UUID`: `project._id`) | `4` | `open` | — | Projekto identifikatorius | — |
| `name` | `string` | — | `4` | `open` | — | Projekto pavadinimas sutartyje | — |
| `tripartite` | `boolean` | — | `4` | `open` | — | Trišalė sutartis | — |
| `state_aid` | `boolean` | — | `4` | `open` | — | Teikiama valstybės pagalba | — |
| `de_minimis_aid` | `boolean` | — | `4` | `open` | — | Teikiama de minimis pagalba | — |
| `awards` | `boolean` | — | `4` | `open` | — | Taikomi apdovanojimai | — |
| `iti` | `boolean` | — | `4` | `open` | — | Integruotų teritorijų investicijų projektas (ITI) | — |
| `baltic_strategy` | `string` | — | `3` | `open` | — | Projektas prisideda prie Baltijos jūros regiono strategijos įgyvendinimo | — |
| `is_submitted_ppp` | `boolean` | — | `4` | `open` | — | Teikiamas PPP | — |
| `partic_attend` | `boolean` | — | `4` | `open` | — | Projekto veiklose dalyvauja projekto dalyviai | — |
| `esf` | `boolean` | — | `4` | `open` | — | ESF Tarptautinis projektas | — |
| `is_provided_gng` | `boolean` | — | `4` | `open` | — | Teikiami GNG duomenys | — |
| `implement_type` | `string` | — | `3` | `open` | — | Projekto įgyvendinimo tipas | — |
| `impl_partners` | `boolean` | — | `4` | `open` | — | Projektas, kuris visiškai arba iš dalies įgyvendinamas socialinių partnerių ar NVO | — |
| `women_attend` | `boolean` | — | `4` | `open` | — | Projektas, skirtas tvariam moterų dalyvavimui ir pažangai darbo rinkoje | — |
| `partnership` | `boolean` | — | `4` | `open` | — | Viešos – privačios partnerystės programa | — |
| `voluminous` | `boolean` | — | `4` | `open` | — | Didelės apimties projektas | — |
| `executor` | `string` | — | `2` | `open` | — | Vykdytojo pavadinimas | Nerodoma, kai fizinis asmuo arba turi fizinio asmens duomenų |
| `executor_code` | `string` | — | `2` | `open` | — | Vykdytojo JAR kodas | Užsienio pareiškėjams nurodyti analogiški kodai. Fiziniams asmenims vertės pašalintos |
| `executor_foreign_person` | `boolean` | — | `4` | `open` | — | Vykdytojas yra užsienyje registruotas juridinis asmuo | — |
| `legal_person_type` | `string` | — | `3` | `open` | — | Juridinio asmens tipas | — |
| `subject_legal_form` | `string` | — | `3` | `open` | — | Subjekto teisinė forma | — |
| `description` | `string` | — | `4` | `open` | — | Projekto santrauka | — |
| `county` | `string` | — | `2` | `open` | — | Apskritis, kuriai tenka didžioji dalis projekto lėšų | — |
| `municipality` | `string` | — | `2` | `open` | — | Savivaldybė, kuriai tenka didžioji dalis projekto lėšų | — |
| `eurostat_territory` | `string` | — | `2` | `open` | — | Projekto įgyvendinimo teritorija pagal Eurostat skirstymą | — |
| `in_another_eu` | `boolean` | — | `4` | `open` | — | Projektas ar jo dalis įgyvendinami kitoje ES valstybėje narėje (ne Lietuvos Respublikoje) | — |
| `outside_eu` | `boolean` | — | `4` | `open` | — | Projektas ar jo dalis įgyvendinami už ES teritorijos ribų | — |
| `fin_outside_amount` | `number` | — | `2` | `open` | — | Projekto finansavimo lėšų suma, skiriama veikloms, įgyvendinamoms ne programos teritorijoje | — |
| `duration` | `integer` | `mo` | `4` | `open` | — | Projekto įgyvendinimo trukmė (mėnesiais) | — |
| `principle` | `boolean` | — | `4` | `open` | — | Projekto įgyvendinimo metu bus užtikrintas horizontaliųjų principų laikymasis | — |
| `started` | `date` | `D` | `4` | `open` | — | Sutarties įsigaliojimo data | — |
| `canceled` | `date` | `D` | `4` | `open` | — | Sutarties nutraukimo data | — |
| `finished` | `date` | `D` | `4` | `open` | — | Projekto baigimo data | — |
| `impl_from` | `date` | `D` | `4` | `open` | — | Projekto veiklų įgyvendinimo pradžia | — |
| `impl_till` | `date` | `D` | `4` | `open` | — | Projekto veiklų įgyvendinimo pabaiga | — |
| `fin_eligibility` | `string` | — | `3` | `open` | — | PVM tinkamumas finansuoti. | — |
| `max_advance_amount` | `number` | — | `2` | `open` | — | Maksimalus avansas (suma) | — |
| `final_pay_by` | `date` | `D` | `4` | `open` | — | Galutinio mokėjimo prašymo pateikimo data | — |
| `expense_compensation` | `boolean` | — | `4` | `open` | — | Ar bus teikiami mokėjimo prašymai, kurių apmokėjimo būdas „Išlaidų kompensavimas“ | — |
| `account_payment` | `boolean` | — | `4` | `open` | — | Ar bus teikiami mokėjimo prašymai, kurių apmokėjimo būdas „Sąskaitų apmokėjimas“ | — |
| `fixed_rate` | `boolean` | — | `4` | `open` | — | Taikomi fiksuotieji projekto išlaidų vieneto įkainiai | — |
| `fixed_sum` | `boolean` | — | `4` | `open` | — | Taikomos fiksuotosios projekto išlaidų sumos | — |
| `finished_report` | `boolean` | — | `4` | `open` | — | Teikiama ataskaita po projekto finansavimo pabaigos | — |
| `finished_report_period` | `integer` | `yr` | `4` | `open` | — | Ataskaitų teikimo laikotarpis (metais) | — |
| `finished_report_order` | `string` | — | `3` | `open` | — | Ataskaitos teikimo tvarka | — |
| `store_until` | `date` | `D` | `4` | `open` | — | Su projekto įgyvendinimu susijusių dokumentų saugojimo terminas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fin_outside_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `max_advance_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
