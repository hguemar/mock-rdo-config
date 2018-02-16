Name:           mock-rdo-config
Version:        0.5
Release:        1%{?dist}
Summary:        Additional Mock configuration for RDO

License:        GPLv3
URL:            http://github.com/hguemar/mock-rdo-config
Source0:        LICENSE
Source1:        rdo-queens-el7.cfg
Source2:        rdo-pike-el7.cfg
Source3:        rdo-ocata-el7.cfg
Source4:        rdo-newton-el7.cfg
Source5:        rdo-mitaka-el7.cfg
Source6:        rdo-master-el7.cfg

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
install -Dpm 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/mock/
install -Dpm 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/mock/
install -Dpm 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/mock/


%files
%license LICENSE
%{_sysconfdir}/mock/*



%changelog
* Fri Feb 16 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.5-1
- Add Queens/Rocky config

* Mon Jul 24 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4-1
- Add pike config
- Drop Liberty, Kilo config

* Thu Feb 23 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.3-1
- Add ocata config
- Refactor a bit profiles for readability

* Tue Aug  2 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1-3
- Add newton config

* Thu Jun 16 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1-2
- Fix mock config files

* Tue Jun  7 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1-1
- Initial package

