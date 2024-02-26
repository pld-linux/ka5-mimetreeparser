#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		mimetreeparser
Summary:	mimetreeparser
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	687a06b1273d58cf6302c88e1c9048b6
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel >= 6.6.1
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Qml-devel
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Widgets-devel >= 6.6.1
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	gpgme-c++-devel >= 1.16.0
BuildRequires:	ka5-kmbox-devel >= 5.240.95
BuildRequires:	ka5-kmime-devel >= 5.240.95
BuildRequires:	ka5-libkleo-devel >= 5.240.95
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcalendarcore-devel
BuildRequires:	kf6-kcodecs-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-kwidgetsaddons-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.5.0
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mime tree parser.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKPim6MimeTreeParserCore.so.*.*
%ghost %{_libdir}/libKPim6MimeTreeParserCore.so.6
%attr(755,root,root) %{_libdir}/libKPim6MimeTreeParserWidgets.so.*.*
%ghost %{_libdir}/libKPim6MimeTreeParserWidgets.so.6
%dir %{_libdir}/qt6/qml/org/kde/pim/mimetreeparser
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/MailViewer.qml
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/libmimetreeparser_plugin.so
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/mimetreeparser_plugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/private
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/private/AttachmentDelegate.qml
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/private/Banner.qml
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/private/ErrorPart.qml
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/private/HtmlPart.qml
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/private/ICalPart.qml
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/private/MailPart.qml
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/private/MailPartModel.qml
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/private/MailPartView.qml
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/private/TextPart.qml
%{_libdir}/qt6/qml/org/kde/pim/mimetreeparser/qmldir
%{_datadir}/qlogging-categories6/mimetreeparser2.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPim6/MimeTreeParserCore
%{_includedir}/KPim6/MimeTreeParserWidgets
%{_libdir}/cmake/KPim6MimeTreeParserCore
%{_libdir}/cmake/KPim6MimeTreeParserWidgets
%{_libdir}/libKPim6MimeTreeParserCore.so
%{_libdir}/libKPim6MimeTreeParserWidgets.so
%{_libdir}/qt6/mkspecs/modules/qt_MimeTreeParserCore.pri
%{_libdir}/qt6/mkspecs/modules/qt_MimeTreeParserWidgets.pri
