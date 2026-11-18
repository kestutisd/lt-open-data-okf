# Cross-OS OKF Bundle Resolution, Sparse Cache, and Search Fallbacks

## 1. Tool Selection and `BUNDLE_DIR` Resolution

- Prefer built-in harness Read, Glob, and Grep tools before spawning shell processes because native tools avoid shell quoting bugs, locale encoding mismatches, and subprocess overhead.
- Resolve `BUNDLE_DIR` to the first existing directory containing `index.md`:
  1. `./bundle` when the current workspace is a clone of `lt-open-data-okf`.
  2. `${XDG_CACHE_HOME:-$HOME/.cache}/lt-open-data-okf/bundle` on POSIX shells, `$HOME/.cache/lt-open-data-okf/bundle` in PowerShell, or `%USERPROFILE%\.cache\lt-open-data-okf\bundle` in Windows CMD.
- Bootstrap the user cache via shallow sparse-checkout when no local bundle exists and both `git` and HTTPS access are available.
- Fall back to progressive raw HTTPS fetches only when local files and `git` are unavailable.

## 2. Mandatory Search Exclusions and Stem Pairing

- Exclude `viz.html` from every content search because it embeds the interactive graph as a multi-megabyte single-line JSON payload that floods context windows on match.
- Exclude `index.md` at every directory depth during keyword searches because directory indexes list navigation links rather than authoritative `# Schema` column definitions (open specific `index.md` files directly only when browsing hierarchy).
- Exclude `log.md` from schema searches because it records bundle generation history rather than dataset or table schemas.
- Pair inflected Lithuanian stems with unaccented ASCII stems (`<lt_stem>|<ascii_stem>`) because titles and descriptions inflect across grammatical cases while Spinta paths, `<Model>` names, and `<field>` names use ASCII `snake_case` or `PascalCase` (and occasional legacy upstream strings corrupt diacritics).
- Search from `$BUNDLE_DIR` root (with exclusions) rather than hardcoding a single top-level subfolder because `bundle/index.md` lists all preserved upstream top-level namespaces under `# Subdirectories`.

## 3. Lightweight Sparse-Checkout Cache Bootstrap

- Pass `--depth 1 --filter=blob:none --sparse` with `--no-cone` patterns `'bundle/**'` and `'!bundle/viz.html'` so Git downloads Markdown schema files while skipping `bundle/viz.html`.
- Omit a leading `/` on sparse-checkout patterns because internal `/` already anchors `--no-cone` patterns to the repository root, whereas a leading `/` triggers MSYS2 path rewriting in Git Bash on Windows.
- Set `REFRESH_BUNDLE=1` (or run `git -C <cache> pull --ff-only`) only when updated upstream schemas are requested so routine offline queries incur zero network calls.

### POSIX (`sh` / `bash` / `zsh`)

```sh
CACHE_REPO="${XDG_CACHE_HOME:-$HOME/.cache}/lt-open-data-okf"
if [ ! -f "$CACHE_REPO/bundle/index.md" ]; then
  git clone --depth 1 --filter=blob:none --sparse https://github.com/kestutisd/lt-open-data-okf.git "$CACHE_REPO"
  git -C "$CACHE_REPO" sparse-checkout set --no-cone 'bundle/**' '!bundle/viz.html'
fi
if [ "${REFRESH_BUNDLE:-0}" = "1" ]; then
  git -C "$CACHE_REPO" pull --ff-only
fi
```

### Windows PowerShell (`powershell.exe` 5.1 and `pwsh` 7+)

- Avoid POSIX `${XDG_CACHE_HOME:-...}` brace defaults in PowerShell because PowerShell parses `XDG_CACHE_HOME:` as a drive prefix and silently expands the variable to an empty string.
- Use automatic `$HOME` (populated in all PowerShell versions even when `$env:HOME` is unset) alongside `$env:XDG_CACHE_HOME`.

```powershell
$CacheRepo = if ($env:XDG_CACHE_HOME) { "$env:XDG_CACHE_HOME/lt-open-data-okf" } else { "$HOME/.cache/lt-open-data-okf" }
if (-not (Test-Path "$CacheRepo/bundle/index.md")) {
    git clone --depth 1 --filter=blob:none --sparse https://github.com/kestutisd/lt-open-data-okf.git "$CacheRepo"
    git -C "$CacheRepo" sparse-checkout set --no-cone 'bundle/**' '!bundle/viz.html'
}
if ($env:REFRESH_BUNDLE -eq "1") {
    git -C "$CacheRepo" pull --ff-only
}
```

### Windows CMD (`cmd.exe`)

- Use double quotes `"..."` in `cmd.exe` because single quotes `'...'` are written literally into `.git/info/sparse-checkout`.
- Never set and expand `%VAR%` on the same `&` or `&&` command line because `cmd.exe` expands `%VAR%` at parse time before `set` runs.

```bat
if not exist "%USERPROFILE%\.cache\lt-open-data-okf\bundle\index.md" (
  git clone --depth 1 --filter=blob:none --sparse https://github.com/kestutisd/lt-open-data-okf.git "%USERPROFILE%\.cache\lt-open-data-okf"
  git -C "%USERPROFILE%\.cache\lt-open-data-okf" sparse-checkout set --no-cone "bundle/**" "!bundle/viz.html"
)
```

## 4. Per-OS UTF-8 Schema Search Fallbacks

- Set `PATTERN` / `$Pattern` to your target regex (`<lt_stem>|<ascii_stem>` or `<field>`).
- Keep pathspec exclusions `':!viz.html' ':!index.md' ':!**/index.md' ':!log.md'` (not `*index.md`) so nested directory `index.md` files are excluded without hiding concept files ending in `_index.md`.

### POSIX (`sh` / `bash` / `zsh`)

- Pass `-n` to `rg` explicitly because `rg` omits line numbers when stdout is piped in non-TTY runners.

```sh
if [ -f "./bundle/index.md" ]; then
  BUNDLE_DIR="./bundle"
else
  BUNDLE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/lt-open-data-okf/bundle"
fi
PATTERN="${PATTERN:-type: Table}"

if command -v rg >/dev/null 2>&1; then
  rg -ni -g '*.md' -g '!index.md' -g '!log.md' -- "$PATTERN" "$BUNDLE_DIR"
elif git -C "$BUNDLE_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git -C "$BUNDLE_DIR" grep -niE -- "$PATTERN" . ':!viz.html' ':!index.md' ':!**/index.md' ':!log.md'
elif grep --help 2>&1 | grep -q -- '--exclude'; then
  grep -rniE --include='*.md' --exclude='index.md' --exclude='log.md' -- "$PATTERN" "$BUNDLE_DIR"
else
  find "$BUNDLE_DIR" -type f -name '*.md' ! -name 'index.md' ! -name 'log.md' -exec grep -niHE -- "$PATTERN" {} +
fi
```

### Windows PowerShell (`powershell.exe` 5.1 and `pwsh` 7+)

- Set `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8` so UTF-8 Baltic characters do not mojibake on legacy Windows console code pages.
- Pass `-Encoding UTF8` to `Select-String` because Windows PowerShell 5.1 defaults to legacy ANSI encoding on UTF-8 files without BOM.
- Call `curl.exe` explicitly (never bare `curl`, which aliases `Invoke-WebRequest` in Windows PowerShell 5.1).

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$CacheRepo = if ($env:XDG_CACHE_HOME) { "$env:XDG_CACHE_HOME/lt-open-data-okf" } else { "$HOME/.cache/lt-open-data-okf" }
$BundleDir = if (Test-Path "./bundle/index.md") { "./bundle" } else { "$CacheRepo/bundle" }
$Pattern = if ($Pattern) { $Pattern } else { "type: Table" }

if (Get-Command git -ErrorAction SilentlyContinue) {
    git -C "$BundleDir" grep -niE -- "$Pattern" . ':!viz.html' ':!index.md' ':!**/index.md' ':!log.md'
} else {
    Get-ChildItem -LiteralPath $BundleDir -Recurse -Filter "*.md" -File |
        Where-Object { $_.Name -notin 'index.md', 'log.md' } |
        Select-String -Pattern $Pattern -Encoding UTF8
}
```

### Windows CMD (`cmd.exe`)

- Prefer `git -C ... grep` in CMD because `findstr` lacks full Unicode case-folding for non-ASCII characters.
- Pair ASCII stems and strip `index.md` and `log.md` via `findstr /V` whenever `git` is unavailable in CMD.

```bat
git -C "%USERPROFILE%\.cache\lt-open-data-okf\bundle" grep -niE -- "type: Table" . ":!viz.html" ":!index.md" ":!**/index.md" ":!log.md"
pushd "%USERPROFILE%\.cache\lt-open-data-okf\bundle" && findstr /S /I /N /R /C:"type: Table" *.md | findstr /V /I /R "^index\.md: ^log\.md: \\index\.md: \\log\.md:" && popd
```

### Minimal `LC_ALL=C` Containers

- Prefix `LC_ALL=C.UTF-8` or run `python3 -X utf8` in minimal containers because `LC_ALL=C` restricts POSIX `grep -i` case-folding to ASCII `A-Z` and drops uppercase UTF-8 Lithuanian diacritic matches.

```sh
if [ -f "./bundle/index.md" ]; then
  BUNDLE_DIR="./bundle"
else
  BUNDLE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/lt-open-data-okf/bundle"
fi
PATTERN="${PATTERN:-type: Table}"

python3 -X utf8 -c '
import pathlib, re, sys
root = pathlib.Path(sys.argv[1])
rx = re.compile(sys.argv[2], re.IGNORECASE)
for p in sorted(root.rglob("*.md")):
    if p.name in ("index.md", "log.md"):
        continue
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if rx.search(line):
            print(f"{p.relative_to(root)}:{n}:{line}")
' "$BUNDLE_DIR" "$PATTERN"
```

## 5. Restricted and No-Shell Sandbox Fallback (Raw HTTPS)

- Traverse progressive disclosure directly over HTTPS at `https://raw.githubusercontent.com/kestutisd/lt-open-data-okf/main/bundle/<path>` when local files, shell access, and `git` are unavailable:
  1. Fetch `bundle/index.md` (`# Subdirectories`) and `bundle/<namespace>/index.md` to locate the target provider path.
  2. Fetch `bundle/<dataset>.md` (`type: Dataset`) to check frontmatter `resource:` and the `# Tables` inventory.
  3. Fetch `bundle/<dataset>/<Model>.md` (`type: Table`) to read introductory prose, `# Schema`, `# Enumerations`, `# Translations`, `# Prefixes`, and `# Comments`.
- Never fetch `bundle/viz.html` over HTTPS in an agent session because it contains visualization code rather than additional schema data.
