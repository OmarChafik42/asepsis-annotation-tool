#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${SOURCE_DIR:-$SCRIPT_DIR/public-docs}"
OUTPUT_DIR="${OUTPUT_DIR:-$SCRIPT_DIR/data-public}"
BACKEND="${MINERU_BACKEND:-pipeline}"
LANGUAGE="${MINERU_LANG:-}"

# Keep OCR's peak memory bounded on machines with limited RAM/VRAM. These
# remain configurable for machines that can safely process larger batches.
export MINERU_PROCESSING_WINDOW_SIZE="${MINERU_PROCESSING_WINDOW_SIZE:-8}"
export MINERU_API_MAX_CONCURRENT_REQUESTS="${MINERU_API_MAX_CONCURRENT_REQUESTS:-1}"
export MINERU_DEVICE_MODE="${MINERU_DEVICE_MODE:-cpu}"

if [[ ! -d "$SOURCE_DIR" ]]; then
    echo "Source directory does not exist: $SOURCE_DIR" >&2
    exit 1
fi

if [[ -n "${MINERU_BIN:-}" ]]; then
    mineru_bin="$MINERU_BIN"
elif command -v mineru >/dev/null 2>&1; then
    mineru_bin="$(command -v mineru)"
    if [[ "$mineru_bin" == */.pyenv/shims/* ]] && command -v pyenv >/dev/null 2>&1; then
        mineru_bin="$(pyenv which mineru 2>/dev/null || printf '%s' "$mineru_bin")"
    fi
elif [[ -x "$SCRIPT_DIR/.venv/bin/mineru" ]]; then
    mineru_bin="$SCRIPT_DIR/.venv/bin/mineru"
elif [[ -x "$SCRIPT_DIR/.venv-rocm/bin/mineru" ]]; then
    mineru_bin="$SCRIPT_DIR/.venv-rocm/bin/mineru"
elif command -v pyenv >/dev/null 2>&1 && pyenv which mineru >/dev/null 2>&1; then
    mineru_bin="$(pyenv which mineru)"
else
    echo "Could not find MinerU. Activate its environment or set MINERU_BIN." >&2
    exit 1
fi

mapfile -t pdfs < <(find "$SOURCE_DIR" -maxdepth 1 -type f -iname '*.pdf' -print | sort)
total=${#pdfs[@]}
if (( total == 0 )); then
    echo "No PDF files found in $SOURCE_DIR"
    exit 0
fi

mkdir -p "$OUTPUT_DIR"
skipped=0
errors=0

for index in "${!pdfs[@]}"; do
    pdf="${pdfs[$index]}"
    name="$(basename "$pdf")"
    name="${name%.*}"
    document_dir="$OUTPUT_DIR/$name"
    auto_dir="$document_dir/auto"
    md_file="$auto_dir/$name.md"
    model_file="$auto_dir/${name}_model.json"
    origin_file="$auto_dir/${name}_origin.pdf"
    number=$((index + 1))

    if [[ -f "$md_file" && -f "$model_file" && -f "$origin_file" ]]; then
        skipped=$((skipped + 1))
        echo "[$number/$total] Skipping (already complete): $name"
        continue
    fi

    echo "[$number/$total] Converting: $name"
    mineru_args=(-p "$pdf" -o "$OUTPUT_DIR" --backend "$BACKEND")
    if [[ -n "$LANGUAGE" ]]; then
        mineru_args+=(-l "$LANGUAGE")
    fi

    if ! "$mineru_bin" "${mineru_args[@]}"; then
        echo "WARN: MinerU failed: $name" >&2
        errors=$((errors + 1))
        continue
    fi

    # MinerU normally creates these files under <output>/<name>/auto. Copy the
    # immutable source PDF explicitly because the annotation tool requires it.
    mkdir -p "$auto_dir"
    if [[ ! -f "$origin_file" ]]; then
        cp -p "$pdf" "$origin_file"
    fi

    missing=()
    [[ -f "$md_file" ]] || missing+=("$md_file")
    [[ -f "$model_file" ]] || missing+=("$model_file")
    if (( ${#missing[@]} > 0 )); then
        printf 'WARN: MinerU completed but required output is missing: %s\n' \
            "${missing[*]}" >&2
        errors=$((errors + 1))
    else
        echo "Done: $name"
    fi
done

echo "All done: $total total, $skipped skipped, $errors errors."
(( errors == 0 ))
