### Python

`pip install biostream-schemas`

then in code (example):

```
from bmeg import phenotype_pb2, rna_pb2
drug = phenotype_pb2.Compound()
drug.id = "Obatantib"
```

### Go

`go get github.com/biostream/schemas/go/bmeg`
