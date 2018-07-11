Name:	    modsecurity
Version:	3.0
Release:	1%{?dist}
License:  None
Summary:	ModSecurity built on Centos 7.x.
Source: modsecurity.tar.gz

%description
ModSecurity built from source on Centos 7.x.

%prep
rm -rf $RPM_BUILD_ROOT/*
tar zxf $RPM_SOURCE_DIR/modsecurity.tar.gz -C $RPM_BUILD_DIR

%install
mkdir -p $RPM_BUILD_ROOT/usr/local
cp -r $RPM_BUILD_DIR/%{name} $RPM_BUILD_ROOT/usr/local

%files
/usr/local/%{name}
