#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Sphinx API for Web Apps
Summary(pl.UTF-8):	API Sphinksa dla aplikacji WWW
Name:		python3-sphinxcontrib-websupport
Version:	1.2.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-websupport/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-websupport/sphinxcontrib-websupport-%{version}.tar.gz
# Source0-md5:	4fe4d07afe1556c65182d0437228d7bb
URL:		https://pypi.org/project/sphinxcontrib-websupport/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.8
BuildRequires:	python3-pytest
BuildRequires:	python3-six
BuildRequires:	python3-sqlalchemy
BuildRequires:	python3-whoosh
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
Requires:	python3-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinxcontrib-websupport provides a Python API to easily integrate
Sphinx documentation into your Web application.

%description -l pl.UTF-8
sphinxcontrib-websupport dostarcza pythonowe API do łatwej integracji
dokumentacji tworzonej z użyciem Sphinksa w aplikacji WWW.

%prep
%setup -q -n sphinxcontrib-websupport-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/websupport
%{py3_sitescriptdir}/sphinxcontrib_websupport-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_websupport-%{version}-py*-nspkg.pth
