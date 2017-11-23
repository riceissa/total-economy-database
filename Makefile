ted.sql:
	for file in proc_*; do ./$$file >> ted.sql; done

.PHONY: read
read:
	mysql devecondata < ted.sql

.PHONY: clean
clean:
	rm -f ted.sql
