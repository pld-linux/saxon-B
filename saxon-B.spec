%define		ver		8.7.1
%define		_ver		8-7-1j

Summary:	XSLT Processor in Java
Summary(pl):	Procesor XSLT napisany w Javie
Name:		saxon-B
Version:	%{ver}
Release:	1
Vendor:		Michael Kay
License:	unknown
Group:		Applications/Publishing/XML
Source0:	http://mesh.dl.sourceforge.net/saxon/saxonb%{_ver}.zip
# Source0-md5:	542bc57fc5dfd9b5c090d5db7bc6f3d6
URL:		http://saxon.sourceforge.net/
BuildRequires:	unzip
Requires:	jre
Requires:	xml-commons
Requires:	jaxp_parser_impl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
XSLT Processor in Java.

%description -l pl
Procesor XSLT napisany w Javie.

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}
chmod -R a+rX *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install saxon*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc
%{_javalibdir}/*.jar
