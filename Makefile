all: schemas

schemas:
	cd proto && \
	protoc \
	-I . \
	--python_out=../ \
	bmeg/rna.proto \
	bmeg/clinical.proto \
	bmeg/cna.proto \
	bmeg/phenotype.proto \
	bmeg/genome.proto \
	bmeg/variants.proto
