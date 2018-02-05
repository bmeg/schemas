all: schemas

schemas:
	go get github.com/golang/protobuf/protoc-gen-go
	cd proto && \
	protoc \
	-I . \
	--python_out=../python/ \
	--go_out=../go/ \
	bmeg/rna.proto \
	bmeg/clinical.proto \
	bmeg/cna.proto \
	bmeg/phenotype.proto \
	bmeg/genome.proto \
	bmeg/variants.proto
