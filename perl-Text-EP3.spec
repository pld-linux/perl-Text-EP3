%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	EP3
Summary:	Text::EP3 perl module
Summary(pl):	Modu³ perla Text::EP3
Name:		perl-Text-EP3
Version:	1.00
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::EP3 - The Extensible Perl PreProcessor.

%description -l pl
Text::EP3 - Rozszerzalny preprocesor dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/ep3
%{perl_vendorlib}/Text/EP3.pm
%{perl_vendorlib}/auto/Text/EP3
%{_mandir}/man3/*
