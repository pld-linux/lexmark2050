Summary:	PBM to Lexmark2050 printer converter.
Summary(pl):	Konwerter z formatu PBM do formatu drukarki Lexmark2050.
Name:		lexmark2050
Version:	0.1
Release:	1
Group:		Applications/Printing
Group(de):	Applikationen/Drucken
Group(pl):	Aplikacje/Drukowanie
License:	GPL
Source0:	http://www.prato.linux.it/~mnencia/%{name}/c2050-%{version}.tar.gz
URL:		http://www.prato.linux.it/~mnencia/lexmark2050
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a PBM to Lexmark2050 printer format converter,
that allows to use this printer under Linux.

%description -l pl
Ten pakiet zawiera konwerter z formatu PBM na format drukarki
Lexmark2050, który umo¿liwia wykorzystanie tej drukarki pod Linuxem.

%prep
%setup -q -n c2050-%{version}
#%patch0 -p1

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/lpfilters

install c2050 $RPM_BUILD_ROOT%{_libdir}/pbm2lexmark2050
install ps2lexmark $RPM_BUILD_ROOT%{_libdir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lpfilters/*
