# Notice & Attribution

## Unofficial & Unverified Disclaimer

This repository distributes an **unofficial, automated [Open Knowledge Format (`OKF v0.3`)](https://github.com/open-knowledge-format/open-knowledge-format) knowledge bundle** derived mechanically from public Lithuanian Open Data Spinta DSA schema manifests, national DCAT-AP catalog metadata, and statutory EU/ISO reference classifications.

- Neither Lithuanian public-sector agencies (*Valstybės skaitmeninių sprendimų agentūra* — VSSA, *Valstybės duomenų agentūra* — VDA, *VĮ Registrų centras*, *VMI*, *Sodra*, *VKC*, *Viešųjų pirkimų tarnyba* — VPT) nor human data stewards have reviewed, verified, or endorsed this bundle.
- Every shipped concept omits `verified:` in YAML frontmatter (`0` `human:`, `team:`, or `process:` verifications), so OKF v0.3 consumers deterministically derive the `unverified` trust tier (SPEC.md §5.3).
- Upstream free-text comments and descriptions are scrubbed to remove personal email addresses, phone numbers, and personal names while retaining official institutional contact addresses (`info@...`, `atverimas@...`, `duomenys@...`).

## Upstream Sources & Provenance (`inputs.lock.json`)

Exact commit SHAs, byte sizes, and SHA-256 checksums for every upstream input are pinned in `inputs.lock.json`:

1. **Spinta DSA Schema Manifests (`team:vssa`):**
   - **Repository:** [`atviriduomenys/manifest`](https://github.com/atviriduomenys/manifest) (commit `ec54998dcea52a0d26dc1c172eacec438d47e727`, `2026-11-11T14:39:20Z`)
   - **Deployment List:** `get_data_gov_lt.in` in `atviriduomenys/manifest`
   - **License:** GNU Affero General Public License v3.0 (`AGPL-3.0-only`)
2. **National Open Data Portal Catalog Metadata (`team:vda`):**
   - **DCAT-AP RDF Export:** `https://data.gov.lt/edp/dcat-ap.rdf`
   - **Portal:** [`data.gov.lt`](https://data.gov.lt)
3. **Statutory EU Legal Acts & Publications Office Authority Tables:**
   - **EVRK 2 / NACE Rev. 2 & EVRK 2.1:** Regulation (EC) No 1893/2006 (`CELEX:32006R1893`) and Delegated Regulation (EU) 2023/137 (`CELEX:32023R0137`)
   - **CPV / BVPŽ Procurement Codes:** Regulation (EC) No 213/2008 (`CELEX:32008R0213`)
   - **Euro / Lithuanian Litas Conversion:** Council Regulation (EU) No 851/2014 (`CELEX:32014R0851`, fixed irrevocable rate `1 EUR = 3.45280 LTL`) and Council Regulation (EC) No 1103/97 (`CELEX:31997R1103`)
   - **Language & Currency Authority Tables:** Publications Office of the European Union SPARQL authority tables (`http://publications.europa.eu/resource/authority/language`, `http://publications.europa.eu/resource/authority/currency`)
   - **Reuse Terms:** European Commission Reuse Decision `2011/833/EU` (EUR-Lex / Publications Office reuse notice)
4. **Supplementary ISO Reference Tables:**
   - **ISO 639-2/3 & ISO 4217 CSVs:** [`datasets/language-codes`](https://github.com/datasets/language-codes) and [`datasets/currency-codes`](https://github.com/datasets/currency-codes) — Open Data Commons Public Domain Dedication and License (`ODC-PDDL-1.0`)
5. **Open Knowledge Format Specification & Tooling Patterns:**
   - **Specification:** [`open-knowledge-format/open-knowledge-format`](https://github.com/open-knowledge-format/open-knowledge-format) (`OKF v0.3`, `Apache-2.0`)

## License

This repository and knowledge bundle are distributed under the **GNU Affero General Public License v3.0 only (`AGPL-3.0-only`)**, matching the license of the upstream [`atviriduomenys/manifest`](https://github.com/atviriduomenys/manifest) repository (see [LICENSE](LICENSE)).
