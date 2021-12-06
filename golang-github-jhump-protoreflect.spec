# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/jhump/protoreflect
%global goipath         github.com/jhump/protoreflect
Version:                1.10.1

%gometa

%global common_description %{expand:
Reflection (Rich Descriptors) for Go Protocol Buffers.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Reflection (Rich Descriptors) for Go Protocol Buffers

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/jsonpb)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/plugin)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(google.golang.org/genproto/protobuf/api)
BuildRequires:  golang(google.golang.org/genproto/protobuf/field_mask)
BuildRequires:  golang(google.golang.org/genproto/protobuf/ptype)
BuildRequires:  golang(google.golang.org/genproto/protobuf/source_context)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/reflection/grpc_reflection_v1alpha)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoiface)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)

%if %{with check}
# Tests
BuildRequires:  golang(google.golang.org/grpc/reflection)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d desc/builder -d desc/protoparse
%endif

%gopkgfiles

%changelog
%autochangelog
