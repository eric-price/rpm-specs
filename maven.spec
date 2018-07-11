Name:	     maven
Version:	 3.5.3
Release:	 1%{?dist}
Group:     Development/Tools
License:   ASL 2.0 and MIT and BSD
URL:       http://maven.apache.org/
Summary:	 Java project management and project comprehension tool binary
Source:    http://www-us.apache.org/dist/maven/maven-3/%{version}/binaries/apache-maven-%{version}-bin.tar.gz

Autoreq: 0

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%prep
rm -rf $RPM_BUILD_ROOT/*
rm -rf $RPM_BUILD_DIR/*
tar zxf $RPM_SOURCE_DIR/apache-maven-%{version}-bin.tar.gz -C $RPM_BUILD_DIR
mv $RPM_BUILD_DIR/apache-maven-%{version} $RPM_BUILD_DIR/%{name}

%install
mkdir -p $RPM_BUILD_ROOT/usr/share
cp -r $RPM_BUILD_DIR/%{name} $RPM_BUILD_ROOT/usr/share

%files
/usr/share/%{name}
