#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	EP3
Summary:	Text::EP3 - the extensible Perl preprocessor
Summary(pl):	Text::EP3 - rozszerzalny preprocesor dla Perla
Name:		perl-Text-EP3
Version:	1.00
Release:	11
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e5c4b5fe376fb9f76a52a2b374ff7dcc
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::EP3 is a Perl program that preprocesses STDIN or some set of
input files and produces an output file.  EP3 only works on input
files and produces output files.  The main difference between EP3 and
other preprocessors is its built-in extensibility.  Every directive in
EP3 is really a method defined in EP3, one of its submodules, or
embedded in the file that is being processed.  By linking the
directive name to the associated methods, other methods could be
added, thus extending the preprocessor.

%description -l pl
Text::EP3 jest programem w Perlu, który przetwarza STDIN lub pewien
zbiów plików wej¶ciowych, tworz±c plik wyj¶ciowy. Dzia³a on jedynie na
plikach wej¶ciowych, tworz±c pliki wyj¶ciowe. G³ówn± ró¿nic± pomiêdzy
EP3 i innymi preprocesorami jest wbudowana rozszerzalno¶æ. Ka¿da
dyrektywa EP3 jest w rzeczywisto¶ci metod± zdefiniowan± w EP3, jednym
z jego podmodu³ów lub w przetwarzanym pliku. Powi±zanie nazwy
dyrektywy ze stowarzyson± metod± umo¿liwia dodawanie innych metod, co
jest rozszerzaniem preprocesora.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/ep3
%{perl_vendorlib}/Text/EP3.pm
%{perl_vendorlib}/auto/Text/EP3
%{_mandir}/man3/*
