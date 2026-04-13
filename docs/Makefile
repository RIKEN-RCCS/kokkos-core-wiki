init-ja:
	sphinx-build -b gettext ./source ./locale
	@find locale -name "*.pot" | while read pot; do \
	  rel=$${pot#locale/}; \
	  po="locale/ja/LC_MESSAGES/$${rel%.pot}.po"; \
	  mkdir -p "$$(dirname "$$po")"; \
	  if [ ! -f "$$po" ]; then \
	    echo "Created $$po"; \
	    msginit --locale=ja --input="$$pot" --output-file="$$po" --no-translator; \
	  fi; \
	done

# merge-ja:
# 	sphinx-build -b gettext ./source ./locale
# 	@find locale -name "*.pot" | while read pot; do \
# 	  rel=$${pot#locale/}; \
# 	  po="locale/ja/LC_MESSAGES/$${rel%.pot}.po"; \
# 	  printf "Merging $$po"; \
# 	  msgmerge --compendium="../../kokkos-core-wiki.ja/docs/$$po" --update --previous --backup=none "$$po" "$$pot"; \
# 	done

init-md-ja:
	@find source -name "*.md" | while read md; do \
	  translated="../../kokkos-core-wiki.ja/docs/$${md}"; \
	  rel=$${md#source/}; \
	  po="locale/ja/LC_MESSAGES/$${rel%.md}.po"; \
	  printf "Merging MD for $${rel%.md}.po\n"; \
	  md2po -t "$$md" "$$translated" -o "$$po" > /dev/null; \
	done

init-rst-ja:
	@find source -name "*.rst" | while read rst; do \
	  rel=$${rst#source/}; \
	  po="locale/ja/LC_MESSAGES/$${rel%.rst}.po"; \
	  translated="../../kokkos-core-wiki.ja/docs/locale/ja/LC_MESSAGES/$${rel%.rst}.po"; \
	  printf "Merging RST for $${rel%.rst}.po..."; \
	  po-merge.sh "$$po" "$$translated" "$${po}"; \
	done


update-ja:
	sphinx-build -b gettext ./source ./locale
	@find locale -name "*.pot" | while read pot; do \
	  rel=$${pot#locale/}; \
	  po="locale/ja/LC_MESSAGES/$${rel%.pot}.po"; \
	  tmp=$$(mktemp); \
	  msgmerge "$$po" "$$pot" 2>/dev/null | sed '1,/^$$/d' > "$$tmp"; \
	  sed '1,/^$$/d' "$$po" | cmp -s - "$$tmp" || { \
	    printf "Updating $$po"; \
	    msgmerge --update --previous --backup=none "$$po" "$$pot"; \
	  }; \
	  rm -f "$$tmp"; \
	done

html-ja:
	sphinx-build -b html -D language=ja ./source ./generated_docs/ja -W --keep-going
#	python3 ./source/edit_button_handler.py

html:
	sphinx-build -b html ./source/ ./generated_docs/ -W --keep-going
	python3 ./source/edit_button_handler.py

clean:
	rm -rf ./generated_docs/
