BuildRequires: systemd

Name:	    vault
Version:	0.10.3
Release:	1%{?dist}
License:  None
Summary:	Hashicorp Vault

Source0: https://releases.hashicorp.com/vault/%{version}/vault_%{version}_linux_amd64.zip
Source1: vault.service

%description
HashiCorp Vault secures, stores, and tightly controls access to tokens, passwords, certificates, API keys, and other secrets.

%prep
rm -rf $RPM_BUILD_ROOT/*
unzip $RPM_SOURCE_DIR/vault_%{version}_linux_amd64.zip -d $RPM_BUILD_DIR

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp -r $RPM_BUILD_DIR/%{name} $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/systemd/system
%{__install} -m644 %SOURCE1 $RPM_BUILD_ROOT/etc/systemd/system/%{name}.service

%files
/usr/bin/%{name}
/etc/systemd/system/vault.service

%post
/usr/bin/systemctl daemon-reload >/dev/null 2>&1

%preun
if [ $1 -eq 0 ]; then
  /usr/bin/systemctl disable %{name}.service >/dev/null 2>&1
  /usr/bin/systemctl stop %{name}.service >/dev/null 2>&1
fi
