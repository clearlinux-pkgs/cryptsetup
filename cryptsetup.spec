#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cryptsetup
Version  : 1.7.5
Release  : 14
URL      : https://www.kernel.org/pub/linux/utils/cryptsetup/v1.7/cryptsetup-1.7.5.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/cryptsetup/v1.7/cryptsetup-1.7.5.tar.xz
Summary  : cryptsetup library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: cryptsetup-bin
Requires: cryptsetup-python
Requires: cryptsetup-lib
Requires: cryptsetup-locales
Requires: cryptsetup-doc
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkgconfig(devmapper)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pwquality)
BuildRequires : popt-dev
BuildRequires : python-dev
BuildRequires : python3

%description
cryptsetup
setup cryptographic volumes for dm-crypt (including LUKS extension)
WEB PAGE:

%package bin
Summary: bin components for the cryptsetup package.
Group: Binaries

%description bin
bin components for the cryptsetup package.


%package dev
Summary: dev components for the cryptsetup package.
Group: Development
Requires: cryptsetup-lib
Requires: cryptsetup-bin
Provides: cryptsetup-devel

%description dev
dev components for the cryptsetup package.


%package doc
Summary: doc components for the cryptsetup package.
Group: Documentation

%description doc
doc components for the cryptsetup package.


%package lib
Summary: lib components for the cryptsetup package.
Group: Libraries

%description lib
lib components for the cryptsetup package.


%package locales
Summary: locales components for the cryptsetup package.
Group: Default

%description locales
locales components for the cryptsetup package.


%package python
Summary: python components for the cryptsetup package.
Group: Default

%description python
python components for the cryptsetup package.


%prep
%setup -q -n cryptsetup-1.7.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503437280
%configure --disable-static --enable-python
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1503437280
rm -rf %{buildroot}
%make_install
%find_lang cryptsetup

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cryptsetup
/usr/bin/veritysetup

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libcryptsetup.so
/usr/lib64/pkgconfig/libcryptsetup.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcryptsetup.so.4
/usr/lib64/libcryptsetup.so.4.7.0

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files locales -f cryptsetup.lang
%defattr(-,root,root,-)

