# Hierarchical Document Ingestion for Retrieval Based on Tree Navigation

This repository contains the ingestion pipeline, annotation tooling, reproducibility artifacts, and corrected document outputs used for hierarchical document ingestion and retrieval based on tree navigation.

## Repository Structure

```text
annotation_tool/     Human-in-the-loop annotation and correction tool
better_ingester/     Document ingestion pipeline and reproducibility artifacts
corrected-docs/      Human-reviewed clinical guideline outputs
data/                Local working data for the annotation tool
```

Detailed instructions for each component are available in their respective READMEs:

- [Annotation Tool](annotation_tool/README.md)
- [BetterIngester](better_ingester/README.md)

## BetterIngester

`better_ingester/` contains the document-ingestion pipeline together with the code and artifacts used for its evaluation and reproducibility.

For installation, usage, benchmarks, and reproduction instructions, see [better_ingester/README.md](better_ingester/README.md).

## Annotation and Correction Tool

For PDFs without an available structured source representation, such as clinical guidelines, we provide a human-in-the-loop annotation tool for visually verifying and correcting the ingestion pipeline's output against the source PDF.

The tool records the initial machine output, every committed human edit, and the final approved state. This makes it both a quality-control interface and a way to measure ingestion quality through the corrections required from human reviewers.

To run the annotation tool from the repository root:

```bash
pip install -r requirements.txt
python run.py --data-dir data
```

Then open:

```text
http://127.0.0.1:8765
```

The expected input layout is:

```text
data/
└── <document>/
    └── auto/
        ├── <document>_origin.pdf
        └── <document>_model.json
```

For complete setup, data-format, session, and Docker instructions, see [annotation_tool/README.md](annotation_tool/README.md).

## Corrected Clinical Guidelines

The annotation workflow was used to review **six clinical guideline PDFs**, producing corrected, retrieval-ready document outputs.

These are provided in:

```text
corrected-docs/
```

## Workflow

```text
Source PDF
    ↓
BetterIngester
    ↓
Machine-generated document structure
    ↓
Annotation and visual verification
    ↓
Human corrections and edit history
    ↓
Corrected retrieval-ready documents
```

## License

The corrected document data in [`corrected-docs/`](corrected-docs/) is released under the [Open Data Commons Attribution License (ODC-BY 1.0)](https://opendatacommons.org/licenses/by/1-0/).

Third-party and vendored software retains its original license. Refer to the corresponding license files within the repository for those components.
