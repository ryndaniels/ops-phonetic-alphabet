json:
	ruby -ryaml -rjson -e 'puts JSON.pretty_generate(YAML.load(ARGF))' < alphabet.yml > alphabet.json

test: json
	python test_alphabet.py
