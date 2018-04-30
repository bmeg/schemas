all: schemas

export GOPATH=$(shell pwd)
PATH := ${PATH}:${GOPATH}/bin
export PATH

schemas:
	go get github.com/golang/protobuf/protoc-gen-go
	go get github.com/golang/protobuf/ptypes
	cd proto && \
	protoc \
	-I . \
	-I $$GOPATH/src/github.com/golang/protobuf/ptypes/struct/ \
	-I $$GOPATH/src/github.com/golang/protobuf/ptypes/timestamp/ \
	--python_out=../python/ \
	--go_out=../go/ \
	bmeg/rna.proto \
	bmeg/clinical.proto \
	bmeg/cna.proto \
	bmeg/phenotype.proto \
	bmeg/genome.proto \
	bmeg/variants.proto \
	bmeg/methylation.proto \
	bmeg/vest.proto \
	bmeg/protein.proto \
	bmeg/pathway.proto
