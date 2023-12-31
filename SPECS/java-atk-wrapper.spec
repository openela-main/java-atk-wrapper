%global major_version 0.33
%global minor_version 2
%global libver 5.0.0

Name:       java-atk-wrapper
Version:    %{major_version}.%{minor_version}
Release:    6%{?dist}
Summary:    Java ATK Wrapper

Group:      Development/Libraries
License:    LGPLv2+
URL:        http://git.gnome.org/browse/java-atk-wrapper
Source0:    http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
# this is a fedora-specific file
# needed to explain how to use java-atk-wrapper with different java runtimes
Source1:    README.fedora
Patch1:		removeNotExistingManifestInclusion.patch

BuildRequires:  java-devel

BuildRequires:  atk-devel
BuildRequires:  GConf2-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  xorg-x11-utils
BuildRequires:  gtk3-devel
BuildRequires:  at-spi2-atk-devel
BuildRequires:  at-spi2-core-devel


Requires:   java
Requires:   xorg-x11-utils

%description
Java ATK Wrapper is a implementation of ATK by using JNI technic. It
converts Java Swing events into ATK events, and send these events to
ATK-Bridge.

JAW is part of the Bonobo deprecation project. It will replaces the
former java-access-bridge.
By talking to ATK-Bridge, it keeps itself from being affected by the
change of underlying communication mechanism.

%prep
%setup -q
%patch1
# Source contains a pre-built AtkWrapper.java with incorrect path to xprop (should 
# be in /usr/bin/ not /opt/X11/bin/). The real source file is AtkWrapper.java.in, 
# so explicitly remove the pre-built file before building.
rm wrapper/org/GNOME/Accessibility/AtkWrapper.java

%build
%configure
make %{?_smp_mflags}
cp %{SOURCE1} .

%install
# java-atk-wrapper's make install is broken by design
# it installs to the current JDK_HOME. We want to install it to a central
# location and then allow all/any JRE's/JDK's to use it.
# make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p %{buildroot}%{_libdir}/%{name}

mv wrapper/java-atk-wrapper.jar %{buildroot}%{_libdir}/%{name}/
mv jni/src/.libs/libatk-wrapper.so.%{libver} %{buildroot}%{_libdir}/%{name}/
ln -s %{_libdir}/%{name}/libatk-wrapper.so.%{libver} \
    %{buildroot}%{_libdir}/%{name}/libatk-wrapper.so.0


%files
%doc AUTHORS
%doc COPYING.LESSER
%doc NEWS
%doc README
%doc README.fedora
%{_libdir}/%{name}/


%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 - Anirudhan Mukundank <amukunda@redhat.com> - 0.33.2-1
- Removed AtkWrapper.java before build in spec file

* Tue Sep 01 2015 - Jiri Vanek <jvanek@redhat.com> - 0.33.2-0
- updated t 0.33.2
- added patch to fix  addition of not existng manifest

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 - Jiri Vanek <jvanek@redhat.com> - 0.32.92-1
- first update ever
- to newest wrapper 32.92 with faith to fix some issues
- added build requirments of gtk3-devel, at-spi2-atk-devel and at-spi2-core-devel
- introduced libver macro to avoid duplicated entry

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 10 2012 - Omair Majid <omajid@redhat.com> - 0.30.4-1
- Added missing requires/buildrequires on xorg-x11-utils
- Added README.fedora

* Wed May 09 2012 - Omair Majid <omajid@redhat.com> - 0.30.4-1
- Initial packaging
