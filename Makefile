MODULE := kpi_dashapp_demo

run:
	@python -m $(MODULE)

test:
	@pytest

.PHONY:
	test clean

clean:
	rm -rf .pytest_cache .coverage .coverage.xml


	