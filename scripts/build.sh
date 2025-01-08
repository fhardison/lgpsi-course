pandoc -s ../src/index.md -o ../docs/index.html --metadata title="LGPSI with addiitons" --css simple-v1.css

uv run text-loom.py ../src/chapter_01.md ../src/paratext.txt | pandoc -s -o ../docs/chapter_01.html -f markdown+raw_html --metadata title="LGPSI 1" --css simple-v1.css
