%global debug_package %{nil}

Name:       ags
Version:    2.3.0
Release:    1
URL:		https://github.com/aylur/ags
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    ags-2.3.0-vendor.tar.gz
Summary:    Building blocks for creating custom desktop shells
License:    LGPL-2.1-only
Group:      Graphical desktop/ Other

BuildRequires:  go
BuildRequires:  pkgconfig(astal-gjs)

Requires:       astal-gjs
Requires:       lib64astal-libs
Requires:       pkgconfig(gtk4-layer-shell-0)

Supplements:    lib64astal-gtk3
Recommends:     lib64astal-gtk4

%description
%summary

%prep
%autosetup -p1
tar -xzf %{SOURCE1}

%build
%define currentgoldflags %{shrink:-X ags/main.gtk4LayerShell=/usr/lib64/libgtk4-layer-shell.so.0
                          -X ags/main.astalGjs=$(pkg-config --variable=srcdir astal-gjs)}
go build -o %{builddir}/bin/ags ags

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{builddir}/bin/* %{buildroot}%{_bindir}/

%files
%{_bindir}/ags
