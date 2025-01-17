Name:           nouveau-fw-gsp
Version:        565.57.01
Release:        1%{?dist}
Summary:        NVIDIA GSP (Turing+) firmware for the latest GSP kernel code

License:        MIT and LicenseRef-NVIDIA
URL:            https://download.nvidia.com/XFree86/Linux-x86_64/%{version}/README/gsp.html
Source0:        https://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}.run
Source1:        https://github.com/NVIDIA/open-gpu-kernel-modules/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3
Requires:       kernel-firmware

%description
This package contains the NVIDIA GSP firmware blobs (Turing and newer),
necessary for the latest kernel with GSP support to function.

%prep
%setup -q -n open-gpu-kernel-modules-%{version} -a1

# Extract NVIDIA .run file
mkdir -p %{_builddir}/nvidia
sh %{SOURCE0} --extract-only --target %{_builddir}/nvidia

%build
# Extract firmware using NVIDIA-provided script
python3 nouveau/extract-firmware-nouveau.py -s -d %{_builddir}/nvidia

%install
# Install the firmware blobs
install -d %{buildroot}/usr/lib/firmware
cp -a _out/nvidia/* %{buildroot}/usr/lib/firmware/

# Install licenses
install -d %{buildroot}/usr/share/licenses/%{name}
install -m 644 COPYING %{buildroot}/usr/share/licenses/%{name}/LICENSE.expat
install -m 644 %{_builddir}/nvidia/LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE.nvidia

%files
%license /usr/share/licenses/%{name}/LICENSE.expat
%license /usr/share/licenses/%{name}/LICENSE.nvidia
/usr/lib/firmware/*

%changelog
* Fri Jan 17 2025 Danayer <Danayerofficial@yandex.ru> - 565.57.01-1
- Initial release for Fedora Copr
