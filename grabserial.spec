Name: grabserial
Version: 1.5.1
Release: 1%{?dist}
Summary: Reads a serial port and writes data to standard output

License: LGPLv2
URL: http://elinux.org/Grabserial
Source0: https://github.com/tbird20d/grabserial

BuildArch: noarch
BuildRequires: pyserial

%description
Grabserial reads a serial port and writes the data to standard output.The main 
purpose of this tool is to collect messages written to the serial console from
a target board running Linux, and save the messages on a host machine. 

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/grabserial.egg-info
%{python_sitelib}/grabserial
%doc README
%license LICENSE


%changelog
* Tue Feb 24 2015 Sinny Kumari <ksinny@gmail.com> - 1.5.1-1
