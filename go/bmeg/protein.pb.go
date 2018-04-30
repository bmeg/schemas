// Code generated by protoc-gen-go. DO NOT EDIT.
// source: bmeg/protein.proto

package bmeg

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

type Protein struct {
	UniprotId         string   `protobuf:"bytes,1,opt,name=uniprot_id,json=uniprotId" json:"uniprot_id,omitempty"`
	Name              string   `protobuf:"bytes,2,opt,name=name" json:"name,omitempty"`
	Accession         []string `protobuf:"bytes,3,rep,name=accession" json:"accession,omitempty"`
	EnsemblGene       string   `protobuf:"bytes,4,opt,name=ensembl_gene,json=ensemblGene" json:"ensembl_gene,omitempty"`
	EnsemblTranscript string   `protobuf:"bytes,5,opt,name=ensembl_transcript,json=ensemblTranscript" json:"ensembl_transcript,omitempty"`
	EnsemblProtein    string   `protobuf:"bytes,6,opt,name=ensembl_protein,json=ensemblProtein" json:"ensembl_protein,omitempty"`
	Pubmed            []string `protobuf:"bytes,7,rep,name=pubmed" json:"pubmed,omitempty"`
	Pdb               []string `protobuf:"bytes,8,rep,name=pdb" json:"pdb,omitempty"`
}

func (m *Protein) Reset()                    { *m = Protein{} }
func (m *Protein) String() string            { return proto.CompactTextString(m) }
func (*Protein) ProtoMessage()               {}
func (*Protein) Descriptor() ([]byte, []int) { return fileDescriptor8, []int{0} }

func (m *Protein) GetUniprotId() string {
	if m != nil {
		return m.UniprotId
	}
	return ""
}

func (m *Protein) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *Protein) GetAccession() []string {
	if m != nil {
		return m.Accession
	}
	return nil
}

func (m *Protein) GetEnsemblGene() string {
	if m != nil {
		return m.EnsemblGene
	}
	return ""
}

func (m *Protein) GetEnsemblTranscript() string {
	if m != nil {
		return m.EnsemblTranscript
	}
	return ""
}

func (m *Protein) GetEnsemblProtein() string {
	if m != nil {
		return m.EnsemblProtein
	}
	return ""
}

func (m *Protein) GetPubmed() []string {
	if m != nil {
		return m.Pubmed
	}
	return nil
}

func (m *Protein) GetPdb() []string {
	if m != nil {
		return m.Pdb
	}
	return nil
}

type PFAMFamily struct {
	Id          string   `protobuf:"bytes,1,opt,name=id" json:"id,omitempty"`
	Accession   string   `protobuf:"bytes,2,opt,name=accession" json:"accession,omitempty"`
	Type        string   `protobuf:"bytes,3,opt,name=type" json:"type,omitempty"`
	GoTerms     []string `protobuf:"bytes,4,rep,name=go_terms,json=goTerms" json:"go_terms,omitempty"`
	Clans       []string `protobuf:"bytes,5,rep,name=clans" json:"clans,omitempty"`
	Description string   `protobuf:"bytes,6,opt,name=description" json:"description,omitempty"`
	Comments    string   `protobuf:"bytes,7,opt,name=comments" json:"comments,omitempty"`
}

func (m *PFAMFamily) Reset()                    { *m = PFAMFamily{} }
func (m *PFAMFamily) String() string            { return proto.CompactTextString(m) }
func (*PFAMFamily) ProtoMessage()               {}
func (*PFAMFamily) Descriptor() ([]byte, []int) { return fileDescriptor8, []int{1} }

func (m *PFAMFamily) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *PFAMFamily) GetAccession() string {
	if m != nil {
		return m.Accession
	}
	return ""
}

func (m *PFAMFamily) GetType() string {
	if m != nil {
		return m.Type
	}
	return ""
}

func (m *PFAMFamily) GetGoTerms() []string {
	if m != nil {
		return m.GoTerms
	}
	return nil
}

func (m *PFAMFamily) GetClans() []string {
	if m != nil {
		return m.Clans
	}
	return nil
}

func (m *PFAMFamily) GetDescription() string {
	if m != nil {
		return m.Description
	}
	return ""
}

func (m *PFAMFamily) GetComments() string {
	if m != nil {
		return m.Comments
	}
	return ""
}

func init() {
	proto.RegisterType((*Protein)(nil), "bmeg.Protein")
	proto.RegisterType((*PFAMFamily)(nil), "bmeg.PFAMFamily")
}

func init() { proto.RegisterFile("bmeg/protein.proto", fileDescriptor8) }

var fileDescriptor8 = []byte{
	// 300 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x54, 0x91, 0x4d, 0x4b, 0xc3, 0x40,
	0x10, 0x86, 0x49, 0x93, 0x36, 0xed, 0x54, 0xaa, 0x0e, 0x22, 0xa3, 0x28, 0xd4, 0x5e, 0xf4, 0xa2,
	0x1e, 0xfc, 0x05, 0x5e, 0x2a, 0x1e, 0x84, 0x22, 0xbd, 0x97, 0x7c, 0x0c, 0x61, 0xa1, 0xbb, 0x1b,
	0xb2, 0xdb, 0x43, 0x7f, 0x9c, 0xbf, 0x4d, 0xd9, 0x8f, 0x84, 0x7a, 0xca, 0xcc, 0xf3, 0xbe, 0xcb,
	0xe6, 0x49, 0x00, 0x4b, 0xc9, 0xcd, 0x6b, 0xdb, 0x69, 0xcb, 0x42, 0xbd, 0xb8, 0xa7, 0xc6, 0xcc,
	0xb1, 0xd5, 0x6f, 0x02, 0xf9, 0x26, 0x70, 0xbc, 0x07, 0x38, 0x28, 0xe1, 0xd2, 0x9d, 0xa8, 0x29,
	0x59, 0x26, 0x4f, 0xb3, 0xef, 0x59, 0x24, 0x9f, 0x35, 0x22, 0x64, 0xaa, 0x90, 0x4c, 0x23, 0x1f,
	0xf8, 0x19, 0xef, 0x60, 0x56, 0x54, 0x15, 0x1b, 0x23, 0xb4, 0xa2, 0x74, 0x99, 0xba, 0x13, 0x03,
	0xc0, 0x07, 0x38, 0x63, 0x65, 0x58, 0x96, 0xfb, 0x5d, 0xc3, 0x8a, 0x29, 0xf3, 0x27, 0xe7, 0x91,
	0x7d, 0xb0, 0x62, 0x7c, 0x06, 0xec, 0x2b, 0xb6, 0x2b, 0x94, 0xa9, 0x3a, 0xd1, 0x5a, 0x1a, 0xfb,
	0xe2, 0x65, 0x4c, 0xb6, 0x43, 0x80, 0x8f, 0x70, 0xde, 0xd7, 0xa3, 0x0d, 0x4d, 0x7c, 0x77, 0x11,
	0x71, 0xef, 0x72, 0x0d, 0x93, 0xf6, 0x50, 0x4a, 0xae, 0x29, 0xf7, 0x6f, 0x15, 0x37, 0xbc, 0x80,
	0xb4, 0xad, 0x4b, 0x9a, 0x7a, 0xe8, 0xc6, 0xd5, 0x4f, 0x02, 0xb0, 0x59, 0xbf, 0x7f, 0xad, 0x0b,
	0x29, 0xf6, 0x47, 0x5c, 0xc0, 0x68, 0x90, 0x1f, 0x89, 0xfa, 0xbf, 0x61, 0x50, 0x3f, 0x31, 0x44,
	0xc8, 0xec, 0xb1, 0x65, 0x4a, 0xc3, 0x37, 0x71, 0x33, 0xde, 0xc0, 0xb4, 0xd1, 0x3b, 0xcb, 0x9d,
	0x34, 0x94, 0xf9, 0x7b, 0xf2, 0x46, 0x6f, 0xdd, 0x8a, 0x57, 0x30, 0xae, 0xf6, 0x85, 0x32, 0x34,
	0xf6, 0x3c, 0x2c, 0xb8, 0x84, 0x79, 0xcd, 0x41, 0xd0, 0x5d, 0x12, 0x84, 0x4e, 0x11, 0xde, 0xc2,
	0xb4, 0xd2, 0x52, 0xb2, 0xb2, 0x86, 0x72, 0x1f, 0x0f, 0x7b, 0x39, 0xf1, 0xbf, 0xf3, 0xed, 0x2f,
	0x00, 0x00, 0xff, 0xff, 0x81, 0x5d, 0x2a, 0xb5, 0xe4, 0x01, 0x00, 0x00,
}
