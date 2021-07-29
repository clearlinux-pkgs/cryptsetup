#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : cryptsetup
Version  : 2.3.6
Release  : 63
URL      : https://mirrors.kernel.org/pub/linux/utils/cryptsetup/v2.3/cryptsetup-2.3.6.tar.xz
Source0  : https://mirrors.kernel.org/pub/linux/utils/cryptsetup/v2.3/cryptsetup-2.3.6.tar.xz
Summary  : cryptsetup library
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1
Requires: cryptsetup-bin = %{version}-%{release}
Requires: cryptsetup-config = %{version}-%{release}
Requires: cryptsetup-lib = %{version}-%{release}
Requires: cryptsetup-license = %{version}-%{release}
Requires: cryptsetup-locales = %{version}-%{release}
Requires: cryptsetup-man = %{version}-%{release}
Requires: LVM2
Requires: LVM2-extras
BuildRequires : LVM2
BuildRequires : keyutils-dev
BuildRequires : libgcrypt-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(devmapper)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pwquality)
BuildRequires : popt-dev
BuildRequires : python3-dev

%description
cryptsetup
setup cryptographic volumes for dm-crypt (including LUKS extension)
WEB PAGE:

%package bin
Summary: bin components for the cryptsetup package.
Group: Binaries
Requires: cryptsetup-config = %{version}-%{release}
Requires: cryptsetup-license = %{version}-%{release}

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
Requires: cryptsetup-lib = %{version}-%{release}
Requires: cryptsetup-bin = %{version}-%{release}
Provides: cryptsetup-devel = %{version}-%{release}
Requires: cryptsetup = %{version}-%{release}

%description dev
dev components for the cryptsetup package.


%package lib
Summary: lib components for the cryptsetup package.
Group: Libraries
Requires: cryptsetup-license = %{version}-%{release}

%description lib
lib components for the cryptsetup package.


%package license
Summary: license components for the cryptsetup package.
Group: Default

%description license
license components for the cryptsetup package.


%package locales
Summary: locales components for the cryptsetup package.
Group: Default

%description locales
locales components for the cryptsetup package.


%package man
Summary: man components for the cryptsetup package.
Group: Default

%description man
man components for the cryptsetup package.


%package staticdev
Summary: staticdev components for the cryptsetup package.
Group: Default
Requires: cryptsetup-dev = %{version}-%{release}

%description staticdev
staticdev components for the cryptsetup package.


%prep
%setup -q -n cryptsetup-2.3.6
cd %{_builddir}/cryptsetup-2.3.6
pushd ..
cp -a cryptsetup-2.3.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623278132
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure  --with-crypto_backend=gcrypt --enable-python --with-python_version=3 --enable-static --enable-pwquality
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export FFLAGS="$FFLAGS -m64 -march=haswell"
export FCFLAGS="$FCFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure  --with-crypto_backend=gcrypt --enable-python --with-python_version=3 --enable-static --enable-pwquality
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1623278132
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cryptsetup
cp %{_builddir}/cryptsetup-2.3.6/COPYING %{buildroot}/usr/share/package-licenses/cryptsetup/c0d79c59a1dae23cf8331a810a5df9f5ab6a709d
cp %{_builddir}/cryptsetup-2.3.6/COPYING.LGPL %{buildroot}/usr/share/package-licenses/cryptsetup/6ce6cfc2dfacf60e153e5f61c4c8accc999d322d
cp %{_builddir}/cryptsetup-2.3.6/lib/crypto_backend/argon2/LICENSE %{buildroot}/usr/share/package-licenses/cryptsetup/af3048995149ba8dc2597f61e8fb05b978fd217c
pushd ../buildavx2/
%make_install_avx2
popd
%make_install
%find_lang cryptsetup
## Remove excluded files
rm -f %{buildroot}/usr/lib64/haswell/libcryptsetup.a

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cryptsetup
/usr/bin/cryptsetup-reencrypt
/usr/bin/haswell/cryptsetup
/usr/bin/haswell/cryptsetup-reencrypt
/usr/bin/haswell/integritysetup
/usr/bin/haswell/veritysetup
/usr/bin/integritysetup
/usr/bin/veritysetup

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/cryptsetup.conf

%files dev
%defattr(-,root,root,-)
/usr/include/libcryptsetup.h
/usr/lib64/haswell/libcryptsetup.so
/usr/lib64/libcryptsetup.so
/usr/lib64/pkgconfig/libcryptsetup.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libcryptsetup.so.12
/usr/lib64/haswell/libcryptsetup.so.12.6.0
/usr/lib64/libcryptsetup.so.12
/usr/lib64/libcryptsetup.so.12.6.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cryptsetup/6ce6cfc2dfacf60e153e5f61c4c8accc999d322d
/usr/share/package-licenses/cryptsetup/af3048995149ba8dc2597f61e8fb05b978fd217c
/usr/share/package-licenses/cryptsetup/c0d79c59a1dae23cf8331a810a5df9f5ab6a709d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/cryptsetup-reencrypt.8
/usr/share/man/man8/cryptsetup.8
/usr/share/man/man8/integritysetup.8
/usr/share/man/man8/veritysetup.8

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libcryptsetup.a

%files locales -f cryptsetup.lang
%defattr(-,root,root,-)

