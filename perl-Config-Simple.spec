#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Simple
Summary:	Config::Simple - simple configuration file class
Summary(pl):	Config::Simple - prosta klasa do obs³ugi plików konfiguracyjnych
Name:		perl-Config-Simple
Version:	4.48
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
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
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Config/Simple.pm
%{perl_sitelib}/auto/Config/Simple
%{_mandir}/man3/*
