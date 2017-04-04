Name:       zuul-swift-upload
Version:    0.1
Release:    2%{?dist}
Summary:    The zuul-swift-upload utility

License:    ASL 2.0
URL:        https://docs.openstack.org/infra/system-config/
Source0:    https://raw.githubusercontent.com/openstack-infra/project-config/f91ec9fd3bfbd071a755ddc51fdbde502cf10db1/jenkins/scripts/zuul_swift_upload.py

BuildArch:  noarch

Requires:   python-magic
Requires:   python2-glob2
Requires:   python2-requestsexceptions
Requires:   python-requests

%description
The zuul-swift-upload utility

%prep

%install
install -p -D -m 0755 %{SOURCE0} %{buildroot}/usr/bin/zuul-swift-upload

%files
/usr/bin/zuul-swift-upload

%changelog
* Tue Apr 04 2017 Tristan Cacqueray - 0.1-2
- Requires python2-glob2 instead of python-glob2

* Thu Feb 23 2017 Tristan Cacqueray - 0.1-1
- Initial package
