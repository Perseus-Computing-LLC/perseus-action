from pathlib import Path

ROOT = Path(__file__).parents[1]
ACTION = (ROOT / "action.yml").read_text()
README = (ROOT / "README.md").read_text()


def test_dangerous_execution_is_explicitly_opt_in():
    assert "allow_dangerous:" in ACTION
    assert "default: 'false'" in ACTION
    assert "ALLOW_DANGEROUS_INPUT: ${{ inputs.allow_dangerous }}" in ACTION
    assert 'true) export PERSEUS_ALLOW_DANGEROUS=1' in ACTION
    assert 'false) unset PERSEUS_ALLOW_DANGEROUS' in ACTION
    assert 'dangerous_enabled": allow_dangerous == "true"' in ACTION


def test_context_dependency_is_pinned_and_render_has_provenance_output():
    assert "perseus_ctx_version:" in ACTION
    assert 'perseus-ctx==${PERSEUS_CTX_VERSION}' in ACTION
    assert "provenance:" in ACTION
    assert "render_sha256" in ACTION
    assert "source_sha256" in ACTION
    assert "workspace_sha256" in ACTION
    assert 'resolved.relative_to(workspace)' in ACTION
    assert 'workspace must be an existing directory' in ACTION
    assert 'perseus render "$SOURCE_PATH" --output "$OUTPUT_PATH" --strict' in ACTION
    assert '--workspace "${{ inputs.workspace }}"' not in ACTION
    assert 'perseus render "${{ inputs.source }}"' not in ACTION


def test_public_examples_use_canonical_repository():
    assert "tcconnally/" not in ACTION
    assert "tcconnally/" not in README
    assert "Perseus-Computing-LLC/perseus-action" in README
