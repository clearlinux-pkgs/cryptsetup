#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : cryptsetup
Version  : 2.0.1
Release  : 21
URL      : https://www.kernel.org/pub/linux/utils/cryptsetup/v2.0/cryptsetup-2.0.1.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/cryptsetup/v2.0/cryptsetup-2.0.1.tar.xz
Summary  : cryptsetup library
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1
Requires: cryptsetup-bin
Requires: cryptsetup-python3
Requires: cryptsetup-config
Requires: cryptsetup-lib
Requires: cryptsetup-locales
Requires: cryptsetup-doc
Requires: cryptsetup-python
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkgconfig(devmapper)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pwquality)
BuildRequires : popt-dev
BuildRequires : python3-dev
Patch1: 0001-pycryptsetup-test.py-change-python-interpreter.patch

%description
cryptsetup
setup cryptographic volumes for dm-crypt (including LUKS extension)
WEB PAGE:

%package bin
Summary: bin components for the cryptsetup package.
Group: Binaries
Requires: cryptsetup-config

%description bin
bin components for the cryptsetup package.


%package config
Summary: config components for the cryptsetup package.
Group: Default

%description config
config components for the cryptsetup package.


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
Requires: cryptsetup-python3

%description python
python components for the cryptsetup package.


%package python3
Summary: python3 components for the cryptsetup package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cryptsetup package.


%prep
%setup -q -n cryptsetup-2.0.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517679566
%configure  --enable-python --with-python_version=3 --enable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517679566
rm -rf %{buildroot}
%make_install
%find_lang cryptsetup

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cryptsetup
/usr/bin/cryptsetup-reencrypt
/usr/bin/integritysetup
/usr/bin/veritysetup

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/cryptsetup.conf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.a
/usr/lib64/libcryptsetup.so
/usr/lib64/pkgconfig/libcryptsetup.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcryptsetup.so.12
/usr/lib64/libcryptsetup.so.12.1.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f cryptsetup.lang
%defattr(-,root,root,-)

