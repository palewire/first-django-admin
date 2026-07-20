UV := uv run

.PHONY: docs

docs:
	cd docs && $(UV) make livehtml
