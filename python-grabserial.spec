%global with_python3 1
%global realname grabserial

Name: python-grabserial
Version: 1.7.1
Release: 1%{?dist}
Summary: Reads a serial port and writes data to standard output

License: LGPLv2
URL: http://elinux.org/Grabserial
Source0: https://github.com/tbird20d/grabserial/releases/download/v%{version}/%{realname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python-setuptools
BuildRequires: python2-devel
Requires: pyserial

%if 0%{?with_python3}
BuildRequires: python3-setuptools
BuildRequires: python3-devel
Requires: python3-pyserial
%endif

%description
Grabserial reads a serial port and writes the data to standard output.The main 
purpose of this tool is to collect messages written to the serial console from
a target board running Linux, and save the messages on a host machine. 

%if 0%{?with_python3}
%package -n python3-grabserial
Summary: Reads a serial port and writes data to standard output

%description -n python3-grabserial
Grabserial reads a serial port and writes the data to standard output.The main 
purpose of this tool is to collect messages written to the serial console from
a target board running Linux, and save the messages on a host machine. 
%endif

%prep
%setup -qn %{realname}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -ap . %{py3dir}
%endif

%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif

%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/*.egg-info
%{_bindir}/grabserial
%doc README
%license LICENSE

%if 0%{?with_python3}
%files -n python3-grabserial
%{python3_sitelib}/*.egg-info
%{_bindir}/grabserial
%doc README
%license LICENSE
%endif

%changelog
* Sun Mar 15 2015 Sinny Kumari <ksinny@gmail.com> - 1.7.1-1
- Initial Fedora packaging of grabserial
