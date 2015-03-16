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

%description
Grabserial reads a serial port and writes the data to standard output.The main 
purpose of this tool is to collect messages written to the serial console from
a target board running Linux, and save the messages on a host machine. 

%prep
%setup -qn %{realname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/*.egg-info
%{_bindir}/grabserial
%doc README
%license LICENSE

%changelog
* Sun Mar 15 2015 Sinny Kumari <ksinny@gmail.com> - 1.7.1-1
- Initial Fedora packaging of grabserial
