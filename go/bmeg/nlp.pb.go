// Code generated by protoc-gen-go. DO NOT EDIT.
// source: bmeg/nlp.proto

package bmeg

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

type Pubmed struct {
	Pmid     string   `protobuf:"bytes,1,opt,name=pmid" json:"pmid,omitempty"`
	Title    string   `protobuf:"bytes,2,opt,name=title" json:"title,omitempty"`
	Abstract string   `protobuf:"bytes,3,opt,name=abstract" json:"abstract,omitempty"`
	Text     string   `protobuf:"bytes,4,opt,name=text" json:"text,omitempty"`
	Date     string   `protobuf:"bytes,5,opt,name=date" json:"date,omitempty"`
	Author   []string `protobuf:"bytes,6,rep,name=author" json:"author,omitempty"`
	Citation []string `protobuf:"bytes,7,rep,name=citation" json:"citation,omitempty"`
}

func (m *Pubmed) Reset()                    { *m = Pubmed{} }
func (m *Pubmed) String() string            { return proto.CompactTextString(m) }
func (*Pubmed) ProtoMessage()               {}
func (*Pubmed) Descriptor() ([]byte, []int) { return fileDescriptor5, []int{0} }

func (m *Pubmed) GetPmid() string {
	if m != nil {
		return m.Pmid
	}
	return ""
}

func (m *Pubmed) GetTitle() string {
	if m != nil {
		return m.Title
	}
	return ""
}

func (m *Pubmed) GetAbstract() string {
	if m != nil {
		return m.Abstract
	}
	return ""
}

func (m *Pubmed) GetText() string {
	if m != nil {
		return m.Text
	}
	return ""
}

func (m *Pubmed) GetDate() string {
	if m != nil {
		return m.Date
	}
	return ""
}

func (m *Pubmed) GetAuthor() []string {
	if m != nil {
		return m.Author
	}
	return nil
}

func (m *Pubmed) GetCitation() []string {
	if m != nil {
		return m.Citation
	}
	return nil
}

func init() {
	proto.RegisterType((*Pubmed)(nil), "bmeg.Pubmed")
}

func init() { proto.RegisterFile("bmeg/nlp.proto", fileDescriptor5) }

var fileDescriptor5 = []byte{
	// 166 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x3c, 0x8e, 0x41, 0xca, 0xc2, 0x30,
	0x10, 0x46, 0xe9, 0xdf, 0x36, 0xbf, 0x9d, 0x85, 0x8b, 0x41, 0x64, 0x70, 0x55, 0x5c, 0x75, 0xa5,
	0x0b, 0x2f, 0x22, 0xbd, 0x41, 0xd2, 0x06, 0x0d, 0xb4, 0x4d, 0x88, 0x53, 0xf0, 0x4c, 0x9e, 0x52,
	0x26, 0x91, 0xee, 0xbe, 0xf7, 0x06, 0x1e, 0x03, 0x7b, 0x33, 0xdb, 0xc7, 0x75, 0x99, 0xc2, 0x25,
	0x44, 0xcf, 0x1e, 0x2b, 0xe1, 0xf3, 0xa7, 0x00, 0x75, 0x5f, 0xcd, 0x6c, 0x47, 0x44, 0xa8, 0xc2,
	0xec, 0x46, 0x2a, 0xda, 0xa2, 0x6b, 0xfa, 0xb4, 0xf1, 0x00, 0x35, 0x3b, 0x9e, 0x2c, 0xfd, 0x25,
	0x99, 0x01, 0x4f, 0xb0, 0xd3, 0xe6, 0xc5, 0x51, 0x0f, 0x4c, 0x65, 0x3a, 0x6c, 0x2c, 0x15, 0xb6,
	0x6f, 0xa6, 0x2a, 0x57, 0x64, 0x8b, 0x1b, 0x35, 0x5b, 0xaa, 0xb3, 0x93, 0x8d, 0x47, 0x50, 0x7a,
	0xe5, 0xa7, 0x8f, 0xa4, 0xda, 0xb2, 0x6b, 0xfa, 0x1f, 0x49, 0x7b, 0x70, 0xac, 0xd9, 0xf9, 0x85,
	0xfe, 0xd3, 0x65, 0x63, 0xa3, 0xd2, 0xe7, 0xb7, 0x6f, 0x00, 0x00, 0x00, 0xff, 0xff, 0x93, 0xc7,
	0x15, 0x41, 0xcb, 0x00, 0x00, 0x00,
}
