Name:           nouveau-fw-gsp
Version:        565.57.01
Release:        1%{?dist}
Summary:        NVIDIA GSP (Turing+) firmware for the latest GSP kernel code

License:        MIT and LicenseRef-NVIDIA
URL:            https://download.nvidia.com/XFree86/Linux-x86_64/%{version}/README/gsp.html
Source0:        https://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}.run
Source1:        https://github.com/NVIDIA/open-gpu-kernel-modules/archive/refs/tags/%{version}.tar.gz
BuildRequires:  git, python3

%global _nvidia NVIDIA-Linux-x86_64-%{version}
%global _gsp_output _out/nvidia

%description
This package provides NVIDIA GSP (Graphics System Processor) firmware for GPUs based on Turing architecture and later. It includes the early GSP blobs required for the Nouveau driver.

%prep
%autosetup -n open-gpu-kernel-modules-%{version} -a1

# Extract the NVIDIA run file
mkdir -p %{_builddir}/nvidia
sh %{SOURCE0} --extract-only --target %{_builddir}/nvidia

%build
# Compile the GSP blobs
rm -rf %{_gsp_output} || true
./nouveau/extract-firmware-nouveau.py -s -d %{_builddir}/nvidia

%install
# Create necessary directories and copy blobs
install -dm755 %{buildroot}/usr/lib/firmware
cp -a %{_gsp_output} %{buildroot}/usr/lib/firmware

# Install licenses
install -Dm644 COPYING %{buildroot}/usr/share/licenses/%{name}/LICENSE.expat
install -Dm644 %{_builddir}/nvidia/LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE.nvidia

%files
%license usr/share/licenses/%{name}/LICENSE.expat
%license usr/share/licenses/%{name}/LICENSE.nvidia
/usr/lib/firmware/*

%changelog
* Fri Jan 17 2025 Danayer <Danayerofficial@yandex.ru> - 565.57.01-1
- Initial release for Fedora Copr
