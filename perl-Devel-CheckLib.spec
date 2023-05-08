#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-CheckLib
Version  : 1.16
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/M/MA/MATTN/Devel-CheckLib-1.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MATTN/Devel-CheckLib-1.16.tar.gz
Summary  : 'check that a library is available'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Devel-CheckLib-bin = %{version}-%{release}
Requires: perl-Devel-CheckLib-man = %{version}-%{release}
Requires: perl-Devel-CheckLib-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(Mock::Config)

%description
This module provides a way of checking whether a particular library and
its headers are available, by attempting to compile a simple program and
link against it.

%package bin
Summary: bin components for the perl-Devel-CheckLib package.
Group: Binaries

%description bin
bin components for the perl-Devel-CheckLib package.


%package dev
Summary: dev components for the perl-Devel-CheckLib package.
Group: Development
Requires: perl-Devel-CheckLib-bin = %{version}-%{release}
Provides: perl-Devel-CheckLib-devel = %{version}-%{release}
Requires: perl-Devel-CheckLib = %{version}-%{release}

%description dev
dev components for the perl-Devel-CheckLib package.


%package man
Summary: man components for the perl-Devel-CheckLib package.
Group: Default

%description man
man components for the perl-Devel-CheckLib package.


%package perl
Summary: perl components for the perl-Devel-CheckLib package.
Group: Default
Requires: perl-Devel-CheckLib = %{version}-%{release}

%description perl
perl components for the perl-Devel-CheckLib package.


%prep
%setup -q -n Devel-CheckLib-1.16
cd %{_builddir}/Devel-CheckLib-1.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/use-devel-checklib

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::CheckLib.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/use-devel-checklib.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
