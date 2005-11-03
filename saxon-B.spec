%define		ver		8.5.1
%define		_ver		8-5-1

Summary:	XSLT Processor in Java
Summary(pl):	Procesor XSLT napisany w Javie
Name:		saxon
Version:	%{ver}
Release:	1
Vendor:		Michael Kay
License:	unknown
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/saxon/%{name}b%{_ver}.zip
# Source0-md5:	d2a6ebbfd097e4cd158bb2e23b138fd7
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

install %{name}*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc
%{_javalibdir}/*.jar
