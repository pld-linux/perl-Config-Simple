#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Simple
Summary:	Config::Simple - simple configuration file class
Summary(pl):	Config::Simple - prosta klasa do obs³ugi plików konfiguracyjnych
Name:		perl-Config-Simple
Version:	4.55
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7ce4d142bbb399a838e5370f2c1c1b4a
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::Simple is a class representing configuration file object. It
supports several configuration file syntax and tries to identify the
file syntax to parse them accordingly. Library supports parsing,
updating and creating configuration files.

%description -l pl
Config::Simple stanowi klasê reprezentuj±c± obiekty plików
konfiguracyjnych. Zawiera wsparcie dla kilku sk³adni plików
konfiguracyjnych a próbuje zidentyfikowaæ rodzaj u¿ywanej w danym
pliku sk³adni poprzez kolejne próby ich analizy. Biblioteka wspiera
analizê, aktualizacjê i tworzenie plików konfiguracyjnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Config/Simple.pm
%{perl_vendorlib}/auto/Config/Simple
%{_mandir}/man3/*
