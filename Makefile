ted.sql:
	for file in proc_*; do ./$$file >> ted.sql; done

.PHONY: clean
clean:
	rm -f ted.sql