#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bmon
Version  : 4.0
Release  : 2
URL      : https://github.com/tgraf/bmon/releases/download/v4.0/bmon-4.0.tar.gz
Source0  : https://github.com/tgraf/bmon/releases/download/v4.0/bmon-4.0.tar.gz
Summary  : bandwidth monitor and rate estimator
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: bmon-bin = %{version}-%{release}
Requires: bmon-license = %{version}-%{release}
Requires: bmon-man = %{version}-%{release}
BuildRequires : pkgconfig(libconfuse)
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(libnl-route-3.0)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)

%description
# bmon - Bandwidth Monitor
[![Build Status](https://travis-ci.org/tgraf/bmon.svg?branch=master)](https://travis-ci.org/tgraf/bmon)
[![Coverity Status](https://scan.coverity.com/projects/2864/badge.svg)](https://scan.coverity.com/projects/2864)

%package bin
Summary: bin components for the bmon package.
Group: Binaries
Requires: bmon-license = %{version}-%{release}

%description bin
bin components for the bmon package.


%package doc
Summary: doc components for the bmon package.
Group: Documentation
Requires: bmon-man = %{version}-%{release}

%description doc
doc components for the bmon package.


%package license
Summary: license components for the bmon package.
Group: Default

%description license
license components for the bmon package.


%package man
Summary: man components for the bmon package.
Group: Default

%description man
man components for the bmon package.


%prep
%setup -q -n bmon-4.0
cd %{_builddir}/bmon-4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605120232
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1605120232
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bmon
cp %{_builddir}/bmon-4.0/LICENSE.BSD %{buildroot}/usr/share/package-licenses/bmon/d0f83c8198fdd5464d2373015b7b64ce7cae607e
cp %{_builddir}/bmon-4.0/LICENSE.MIT %{buildroot}/usr/share/package-licenses/bmon/8570a5c766d8b7eda6fa171a7f6674e335b50c5e
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bmon

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/bmon/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bmon/8570a5c766d8b7eda6fa171a7f6674e335b50c5e
/usr/share/package-licenses/bmon/d0f83c8198fdd5464d2373015b7b64ce7cae607e

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/bmon.8
