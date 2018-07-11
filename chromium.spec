%define LASTCHANGE_URL https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2FLAST_CHANGE?alt=media
%define REVISION $(curl -s -S %{LASTCHANGE_URL})
%define ZIP_URL https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F%{REVISION}%2Fchrome-linux.zip?alt=media
%define ZIP_FILE 547058-chrome-linux.zip
%define common_require pango, libXcomposite, libXcursor, libXdamage, libXext, libXi, libXtst, cups-libs, libXScrnSaver, libXrandr, GConf2, alsa-lib, atk, gtk3, ipa-gothic-fonts, xorg-x11-fonts-100dpi, xorg-x11-fonts-75dpi, xorg-x11-utils, xorg-x11-fonts-cyrillic, xorg-x11-fonts-Type1, xorg-x11-fonts-misc

Name:	    chromium
Version:	1.0
Release:	2%{?dist}
License:  None
Summary:	Chromium built on Centos 7.x.
Requires: %{common_require}

%description
Chromium built for Centos 7.x.

%prep
rm -rf $RPM_BUILD_DIR/*
rm -rf $RPM_BUILD_ROOT/*
curl %{ZIP_URL} > $RPM_SOURCE_DIR/%{ZIP_FILE}
unzip $RPM_SOURCE_DIR/%{ZIP_FILE} -d $RPM_BUILD_DIR
mv $RPM_BUILD_DIR/chrome-linux $RPM_BUILD_DIR/%{name}

%install
mkdir -p $RPM_BUILD_ROOT/usr/local
cp -r $RPM_BUILD_DIR/%{name} $RPM_BUILD_ROOT/usr/local
chmod -R 755 $RPM_BUILD_ROOT/usr/local/%{name}
chmod 4755 $RPM_BUILD_ROOT/usr/local/%{name}/chrome_sandbox

%files
/usr/local/%{name}
