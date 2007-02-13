#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	EP3
Summary:	Text::EP3 - the extensible Perl preprocessor
Summary(pl.UTF-8):	Text::EP3 - rozszerzalny preprocesor dla Perla
Name:		perl-Text-EP3
Version:	1.10
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2081ba6bf87e59bdfc937b8a17d0f3d9
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Text::EP3 jest programem w Perlu, który przetwarza STDIN lub pewien
zbiów plików wejściowych, tworząc plik wyjściowy. Działa on jedynie na
plikach wejściowych, tworząc pliki wyjściowe. Główną różnicą pomiędzy
EP3 i innymi preprocesorami jest wbudowana rozszerzalność. Każda
dyrektywa EP3 jest w rzeczywistości metodą zdefiniowaną w EP3, jednym
z jego podmodułów lub w przetwarzanym pliku. Powiązanie nazwy
dyrektywy ze stowarzyszoną metodą umożliwia dodawanie innych metod, co
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
