# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global project felix
%global bundle org.apache.felix.framework
%global groupId org.apache.felix

Name:           %{project}-framework
Version:        4.2.1
Release:        5%{?dist}
Summary:        Apache Felix Framework

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://www.apache.org/dist/%{project}/%{bundle}-%{version}-source-release.tar.gz

BuildArch:      noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: maven-local
BuildRequires: maven-surefire-provider-junit4
BuildRequires: apache-rat-plugin
BuildRequires: felix-parent

%description
Apache Felix Framework Interfaces and Classes.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file : %{project}/%{bundle}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.2.1-5
- Mass rebuild 2013-12-27

* Thu Nov 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-4
- Fix artifact file names

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 4.2.1-3
- Migrate away from mvn-rpmbuild (Resolves: #997514)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 15 2013 Mat Booth <fedora@matbooth.co.uk> - 4.2.1-1
- Update to latest upstream version rhbz #951006.

* Thu Feb 21 2013 Mat Booth <fedora@matbooth.co.uk> - 4.2.0-1
- Update to latest upstream version rhbz #895404.
- No longer need to remove maven-compiler-plugin invocation.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 4.0.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Aug 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.2-4
- Remove maven-compiler-plugin invocation, resolves: #842591
- Remove unneeded BR: maven-invoker-plugin

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.2-3
- Install NOTICE files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Tomas Radej <tradej@redhat.com> - 4.0.2-1
- Updated to latest version
- Guidelines fixes

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 12 2010 Mat Booth <fedora@matbooth.co.uk> - 2.0.5-4
- Fix pom filename (Resolves rhbz#655798)
- Fix various packaging things according to new guidelines

* Tue Jul 13 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.0.5-3
- BR: maven-invoker-plugin required for maven-javadoc-plugin
- Use new names of the maven plgins
- Add license file to independent subpackage javadoc

* Tue Jul 13 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.0.5-2
- Use maven instead of ant

* Tue Jun 22 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.0.5-1
- Release 2.0.5
