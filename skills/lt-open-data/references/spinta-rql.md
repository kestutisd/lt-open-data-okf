# Spinta DSA REST and RQL Query Reference (`get.data.gov.lt`)

## 1. Endpoint Anatomy and Dual Query Syntax

- Build every API URL from the table concept's frontmatter `resource:` (`https://get.data.gov.lt/<dataset>/<Model>`), never from the upstream manifest CSV filename, because declared Spinta namespaces often differ from CSV file paths.
- Use Spyna expression syntax (`?limit(10)&select(_id,<field>)&sort(-<field>)`) as the primary query grammar on `get.data.gov.lt`.
- Use UAPI underscore syntax (`?_limit=10&_select=_id,<field>&_sort=-<field>&_page=<token>&_count`) only when a client library requires `key=value` query parameters.
- Never pass unprefixed control parameters such as `?page=1`, `?offset=20`, `?per_page=50`, or `?format=csv` because Spinta interprets every key without a leading `_` as a column equality filter and returns HTTP `400` `PropertyNotFound`.

```text
https://get.data.gov.lt/<dataset>/<Model>/:format/json?select(_id,<field1>,<field2>)&limit(20)
```

## 2. Filter Operators, Literal Types, and Boolean Logic

- Filter exact equality and inequality with `<field>="<val>"` (or `<field>.eq("<val>")`) and `<field>!=<val>` (or `<field>.ne("<val>")`, UAPI `<field>._ne=<val>`).
- Double-quote string, ISO date (`"YYYY-MM-DD"`), and UUID literals in Spyna expressions while keeping numbers, `true`, `false`, and `null` unquoted (`<field>=null`, `<field>!=null`) because quoting numeric or null literals forces string comparison and triggers validation errors.
- Express range filters with `.gt(<val>)`, `.ge(<val>)`, `.lt(<val>)`, and `.le(<val>)` (UAPI `._gt`, `._ge`, `._lt`, `._le`) rather than raw `<` or `>` symbols because raw angle brackets require percent-encoding (`%3C`, `%3E`) and break unquoted shell commands.
- Match string prefixes with `<field>.startswith("<prefix>")` (UAPI `._sw`) and substrings with `<field>.contains("<substr>")` (UAPI `._co`), noting that default Spinta backends evaluate string matches case-sensitively.
- Avoid `.endswith()` and inline `.lower()` in URL filters because Spinta storage backends omit implementations for them and fail with HTTP `400` `UnknownMethod`.
- Combine AND conditions with `&` (`<cond1>&<cond2>`) and wrap OR branches in parentheses (`(<cond1>|<cond2>)&limit(20)`) or use `any(<field>,"<v1>","<v2>")` so operator precedence binds accurately.

```text
https://get.data.gov.lt/<dataset>/<Model>/:format/json?<field1>.ge(100)&(<field2>="<v1>"|<field2>="<v2>")&limit(20)
```

## 3. Projections, Foreign-Key (`ref`) Serialization, Sorting, Pagination, and Counts

- Pass `select(_id,<field1>,<field2>)` on wide tables to project only required properties and keep response payloads compact.
- Match foreign-key (`ref`) projection and filter syntax strictly to the column's Spinta maturity `level` in `# Schema`:
  - `level >= 4` (`4` or `5`): project `select(<fk>._id)` and filter `<fk>._id="<uuid>"` because Spinta serializes `{"_id": "<uuid>"}` pointing to `<TargetModel>._id` even when `# Schema` `Ref` displays `<TargetModel>[<pk>]`.
  - Natural-key lookup at `level >= 4`: run two sequential queries by fetching `_id` from `<TargetModel>/:format/json?<pk>="<val>"&select(_id)&limit(5)` first and then filtering `<Model>/:format/json?<fk>._id="<uuid>"&limit(20)`.
  - `level = 3`: project `select(<fk>.<pk>)` and filter `<fk>.<pk>="<val>"` because Spinta serializes natural-key object `{"<pk>": "<val>"}` without `_id`.
  - `level <= 2` (`0`, `1`, `2`, or blank marker cell): project `select(<field>)` and filter `<field>="<val>"` with no dotted subfield because Spinta stores an unlinked scalar value.
- Order results with `sort(<field>)` for ascending order, `sort(-<field>)` for descending order, or `sort(-<field1>,<field2>)` for multi-column sorting.
- Paginate exclusively via cursor tokens from `"_page": {"next": "<base64-token>"}` using `?limit(<N>)&page("<base64-token>")` (or `?_limit=<N>&_page=<base64-token>`) until `"_page"` or `"next"` is absent because Spinta supports no numeric offset pagination.
- Query exact row totals with `/:format/json?count()` or `?<filter>&count()` (returning `{"_data":[{"count()":<integer>}]}`) rather than counting rows in a truncated sample page.

```text
https://get.data.gov.lt/<dataset>/<Model>/:format/json?count()
https://get.data.gov.lt/<dataset>/<Model>/:format/json?limit(100)&page("<base64-token>")
```

## 4. Format Route Suffixes and Default Row Caps

- Insert `/:format/<fmt>` immediately after `<Model>` and before `?`:
  - `/:format/json`: returns `{"_data": [...], "_page": {...}}` for structured API reads, `count()`, and cursor pagination.
  - `/:format/jsonl`: streams one JSON object per line for bounded multi-row exports without buffering one array.
  - `/:format/csv`: outputs UTF-8 CSV and flattens nested `ref` objects into dotted headers (`<fk>._id`, `<fk>.<pk>`).
  - `/:format/rdf`: outputs RDF/XML Linked Data driven by `# Prefixes` and `URI` ontology mappings.
  - `/:format/html` and `/:format/ascii`: render human-readable tables (`/:format/html` caps browser views at `100` rows per page by default).
- Include `?limit(<N>)` on every exploratory `json`, `jsonl`, and `csv` request because programmatic formats omit the `100`-row HTML cap and stream up to `100000` rows per batch by default, stalling client buffers on large tables.

## 5. Unsupported SQL Constructs, HTTP Errors, Encoding, and Pacing

- Never send SQL aggregate functions (`sum()`, `avg()`, `min()`, `max()`) to Spinta because only `count()` runs server-side and other aggregates fail with HTTP `400` `UnknownMethod`.
- Check `?count()` before computing client-side sums or averages over `select(...)`, and perform client-side aggregation only when total row volume is small; otherwise state that server-side aggregation is unsupported.
- Never send SQL clauses (`GROUP BY`, `HAVING`, `JOIN`, `OFFSET`, `WHERE`) because Spinta evaluates single-model row filters and rejects SQL syntax with HTTP `400` `InvalidSyntax`.
- Stop immediately on HTTP `401` (`AuthorizedClientsOnly`) or HTTP `403` (`Forbidden`) without probing workarounds, and cite `# Schema` `Access` (`open` and `open (inherited)` allow anonymous reads, `public` requires GDPR-authorized recipients, and `protected`/`private` are restricted).
- Expect HTTP `404` (`ModelNotFound`) whenever a concept omits frontmatter `resource:` (`undeployed` in `get_data_gov_lt.in`).
- Pass `-g` (`--globoff`) to `curl` / `curl.exe` so `()` and `[]` are not glob-expanded by the shell, and percent-encode spaces (`%20`), quotes (`%22`), `|` (`%7C`), and non-ASCII characters in raw HTTP clients.
- Keep total URL length below `2000` bytes (batching `any()` lists to `<= 50` items) because reverse proxies reject oversized query strings with HTTP `414 URI Too Long`.
- Send single sequential requests with an explicit timeout (`-m 15`), avoid concurrent bursts, and stop immediately without automatic retries on HTTP `429` or `502`/`503`/`504`, falling back to static bundle schema facts.
