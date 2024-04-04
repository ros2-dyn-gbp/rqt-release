%{?!ros_distro:%global ros_distro rolling}
%global pkg_name rqt_py_common
%global normalized_pkg_name %{lua:return (string.gsub(rpm.expand('%{pkg_name}'), '_', '-'))}

Name:           ros-rolling-rqt-py-common
Version:        1.5.0
Release:        2%{?dist}
Summary:        ROS %{pkg_name} package

License:        BSD
URL:            http://ros.org/wiki/rqt_py_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  bloom-rpm-macros
BuildRequires:  cmake

%{?bloom_package}

%description
rqt_py_common provides common functionality for rqt plugins written in Python.
Despite no plugin is provided, this package is part of the rqt_common_plugins
repository to keep refactoring generic functionality from these common plugins
into this package as easy as possible. Functionality included in this package
should cover generic ROS concepts and should not introduce any special
dependencies beside &quot;ros_base&quot;.


%package devel
Release:        %{release}%{?release_suffix}
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-runtime%{?_isa} = %{version}-%{release}

%description devel
rqt_py_common provides common functionality for rqt plugins written in Python.
Despite no plugin is provided, this package is part of the rqt_common_plugins
repository to keep refactoring generic functionality from these common plugins
into this package as easy as possible. Functionality included in this package
should cover generic ROS concepts and should not introduce any special
dependencies beside &quot;ros_base&quot;.


%package runtime
Release:        %{release}
Summary:        %{summary}

%description runtime
rqt_py_common provides common functionality for rqt plugins written in Python.
Despite no plugin is provided, this package is part of the rqt_common_plugins
repository to keep refactoring generic functionality from these common plugins
into this package as easy as possible. Functionality included in this package
should cover generic ROS concepts and should not introduce any special
dependencies beside &quot;ros_base&quot;.


%prep
%autosetup -p1


%generate_buildrequires
%bloom_buildrequires


%build
%cmake \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="%{bloom_prefix}" \
    -DAMENT_PREFIX_PATH="%{bloom_prefix}" \
    -DCMAKE_PREFIX_PATH="%{bloom_prefix}" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif

%cmake3_build


%install
%cmake_install


%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C %{__cmake_builddir} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
CTEST_OUTPUT_ON_FAILURE=1 \
    %cmake_build $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif


%files devel
%ghost %{bloom_prefix}/share/%{pkg_name}/package.xml


%files runtime
%{bloom_prefix}


%changelog
* Fri Mar 22 2024 Dharini Dutia <dharini@openrobotics.org> - 1.5.0-2
- Autogenerated by Bloom
