MYSQL_ARGS=
DATABASE=devecondata

ted.sql:
	./print_header.py >> ted.sql
	for file in proc_*; do ./$$file >> ted.sql; done
	./print_footer.py >> ted.sql

.PHONY: read
read:
	mysql $(MYSQL_ARGS) $(DATABASE) < ted.sql

.PHONY: clean
clean:
	rm -f ted.sql
