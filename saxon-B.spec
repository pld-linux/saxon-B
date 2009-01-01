%define		ver		9.1.0.5
%define		_ver		9-1-0-5j

Summary:	XSLT Processor in Java
Summary(pl.UTF-8):	Procesor XSLT napisany w Javie
Name:		saxon-B
Version:	%{ver}
Release:	1
License:	MPL 1.0
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/saxon/saxonb%{_ver}.zip
# Source0-md5:	898f4aa68a1c0a8c1bd5f9f723272443
URL:		http://saxon.sourceforge.net/
BuildRequires:	unzip
Requires:	jaxp_parser_impl
Requires:	jre
Requires:	xml-commons
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
XSLT Processor in Java.

%description -l pl.UTF-8
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
