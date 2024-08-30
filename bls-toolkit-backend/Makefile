run-dev:
	@poetry run uvicorn src.bl2.application.app:app --host 0.0.0.0 --port 8000 --reload
	
format:
	@poetry run isort src test
	@poetry run black src test
	@poetry run autoflake --in-place --remove-unused-variables --remove-all-unused-imports --recursive src/ test/
