%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Simple
Summary:	Config::Simple - Simple Configuration File Class
Summary(pl):	Config::Simple - prosta klasa do obs³ugi plików konfiguracyjnych
Name:		perl-%{pdir}-%{pnam}
Version:	4.3
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::Simple - Simple Configuration File Class.

%description -l pl
Config::Simple - prosta klasa do obs³ugi plików konfiguracyjnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
