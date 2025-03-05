pandoc -s ../src/index.md -o ../docs/index.html --metadata title="LGPSI with additions" --css simple-v1.css
pandoc -s ../src/class_notes.md -o ../docs/class_notes.html --metadata title="Class notes" --css simple-v1.css

uv run text-loom.py ../src/chapter_01.md ../src/paratext.txt | pandoc -s -o ../docs/chapter_01.html -f markdown+raw_html --metadata title="LGPSI 1" --css simple-v1.css
uv run text-loom.py ../src/chapter_02.md ../src/paratext.txt | pandoc -s -o ../docs/chapter_02.html -f markdown+raw_html --metadata title="LGPSI 2" --css simple-v1.css
uv run text-loom.py ../src/chapter_03.md ../src/paratext.txt | pandoc -s -o ../docs/chapter_03.html -f markdown+raw_html --metadata title="LGPSI 3" --css simple-v1.css
uv run text-loom.py ../src/chapter_04.md ../src/paratext.txt | pandoc -s -o ../docs/chapter_04.html -f markdown+raw_html --metadata title="LGPSI 4" --css simple-v1.css
uv run text-loom.py ../src/chapter_05.md ../src/paratext.txt | pandoc -s -o ../docs/chapter_05.html -f markdown+raw_html --metadata title="LGPSI 5" --css simple-v1.css
