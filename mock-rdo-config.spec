Name:           mock-rdo-config
Version:        0.1%{?dist}
Release:        1%{?dist}
Summary:        Additional Mock configuration for RDO

License:        GPLv3
URL:            http://github.com/hguemar/mock-rdo-config
Source0:        LICENSE
Source1:        rdo-mitaka-el7.cfg
Source2:        rdo-liberty-el7.cfg
Source3:        rdo-kilo-el7.cfg


BuildArch:      noarch

Requires:       mock

%description
Additional Mock configuration for RDO

%prep
install -pm 644 %{SOURCE0} .


%build


%install
mkdir -p %{buildroot}%{_sysconfdir}/mock/
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/mock/
install -Dpm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/mock/
install -Dpm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/mock/


%files
%license LICENSE
%{_sysconfdir}/mock/*



%changelog
* Tue Jun  7 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1-1
- Initial package

