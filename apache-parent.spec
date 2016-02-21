%global pkg_name apache-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        10
Release:        14.14%{?dist}
Summary:        Parent pom file for Apache projects
License:        ASL 2.0
URL:            http://apache.org/
Source0:        http://svn.apache.org/repos/asf/maven/pom/tags/apache-10/pom.xml
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix}apache-resource-bundles
BuildRequires:  %{?scl_prefix}maven-remote-resources-plugin
BuildRequires:  %{?scl_prefix}maven-site-plugin

Requires:       %{?scl_prefix}apache-resource-bundles
Requires:       %{?scl_prefix}maven-site-plugin

%description
This package contains the parent pom file for apache projects.


%prep
%setup -n %{pkg_name}-%{version} -Tc
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

# This simplifies work with child projects that can use generics
cp %{SOURCE0} .
sed -i 's:<source>1.4</source>:<source>1.5</source>:' pom.xml
sed -i 's:<target>1.4</target>:<target>1.5</target>:' pom.xml

%pom_remove_plugin :maven-site-plugin

cp %{SOURCE1} LICENSE
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 10-14.14
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 10-14.13
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 10-14.12
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 10-14.11
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 10-14.10
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-14.9
- Mass rebuild 2014-05-26

* Fri Mar 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-14.8
- Remove maven-site-plugin from dependencies

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-14.7
- Mass rebuild 2014-02-19

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-14.6
- Rebuild to get rid of auto-requires on java-devel

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-14.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-14.4
- Add missing BR/R: maven-site-plugin

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-14.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-14.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-14.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 10-14
- Mass rebuild 2013-12-27

* Thu Dec 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-13
- Fix a typo in changelog

* Thu Aug 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-12
- Add missing R: apache-resource-bundles

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 10-11
- Migrate away from mvn-rpmbuild (Resolves: #997520)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 10-9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 18 2012 Michal Srb <msrb@redhat.com> - 10-8
- Added license (Resolves: #888287)

* Wed Nov 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 10-7
- Install patched pom not the original

* Fri Nov  2 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 10-6
- Add missing R: maven-remote-resources-plugin, apache-resource-bundles
- Add %%check to verify dependencies during build

* Thu Jul 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 10-5
- Make sure we generate 1.5 version bytecode

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Andy Grimm <agrimm@gmail.com> 10-2
- Follow suggestions in BZ #736069

* Mon Aug 29 2011 Andy Grimm <agrimm@gmail.com> 10-1
- Initial Build
