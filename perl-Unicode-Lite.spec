#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Unicode
%define	pnam	Lite
Summary:	Unicode::Lite - Easy conversion between encodings
Summary(pl):	Unicode::Lite - ³atwa konwersja pomiêdzy kodowaniami
Name:		perl-Unicode-Lite
Version:	0.12
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f8fa78a8c113bf8b42cba6e3cb9b8797
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Unicode-Map
BuildRequires:	perl-enum
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::Lite includes string converting function from one and to
another charset.

%description -l pl
Unicode::Lite zawiera funkcje do konwersji ci±gów na ró¿ne kodowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
