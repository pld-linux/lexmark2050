Summary:	PBM to Lexmark2050 printer converter
Summary(pl.UTF-8):	Konwerter z formatu PBM do formatu drukarki Lexmark2050
Name:		lexmark2050
Version:	0.3
Release:	1
Group:		Applications/Printing
License:	GPL
Source0:	http://www.prato.linux.it/~mnencia/lexmark2050/c2050-%{version}.tar.gz
# Source0-md5:	925ddd5456971dad1d59ff3772efec86
URL:		http://www.prato.linux.it/~mnencia/lexmark2050/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a PBM to Lexmark2050 printer format converter,
that allows to use this printer under Linux.

%description -l pl.UTF-8
Ten pakiet zawiera konwerter z formatu PBM na format drukarki
Lexmark2050, który umożliwia wykorzystanie tej drukarki pod Linuksem.

%prep
%setup -q -n c2050-%{version}

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/lpfilters

install c2050 $RPM_BUILD_ROOT%{_libdir}/lpfilters/pbm2lexmark2050
install ps2lexmark $RPM_BUILD_ROOT%{_libdir}/lpfilters

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lpfilters/*
