Name: p7zip

Summary: 7-zip file archiver (7zr)
Version: 16.02
Release: 1
Group: Applications/Archiving
License: LGPLv2
Source0: %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(Qt5Core)

%description
%{summary}. 7zr is a "light-version" of 7za that only handles 7z archives.

%package full
Summary: 7-zip file archiver (7z, 7za)
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description full
%{summary}. 7z and 7za are the full versions of the 7-Zip executables. They
support 7z, ZIP, CAB, ARJ, GZIP, BZIP2, TAR, CPIO, RPM and DEB archives.

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%qmake5_install

# Make all scripts in bindir executable
chmod 755 %{buildroot}%{_bindir}/*

%post full -p /sbin/ldconfig

%postun full -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/7zr
%dir %{_libexecdir}/p7zip
%{_libexecdir}/p7zip/7zr

%files full
%defattr(-,root,root,-)
%{_bindir}/7za
%{_bindir}/7z
%dir %{_libexecdir}/p7zip
%{_libexecdir}/p7zip/7za
%{_libexecdir}/p7zip/7z
%{_libexecdir}/p7zip/lib*.so*

