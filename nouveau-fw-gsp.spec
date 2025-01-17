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
# Извлекаем исходники ядра NVIDIA
%setup -q -n open-gpu-kernel-modules-%{version} -a1

# Извлекаем содержимое .run файла NVIDIA
mkdir -p nvidia_extracted
sh %{SOURCE0} --extract-only --target nvidia_extracted

%build
# Извлечение прошивок с использованием скрипта NVIDIA
python3 nouveau/extract-firmware-nouveau.py -s -d nvidia_extracted

%install
# Устанавливаем прошивки
install -d %{buildroot}/usr/lib/firmware
cp -a _out/nvidia/* %{buildroot}/usr/lib/firmware/

# Устанавливаем лицензии
install -d %{buildroot}/usr/share/licenses/%{name}
install -m 644 COPYING %{buildroot}/usr/share/licenses/%{name}/LICENSE.expat
install -m 644 nvidia_extracted/LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE.nvidia

%files
%license /usr/share/licenses/%{name}/LICENSE.expat
%license /usr/share/licenses/%{name}/LICENSE.nvidia
/usr/lib/firmware/*

%changelog
* Fri Jan 17 2025 Danayer <Danayerofficial@yandex.ru> - 565.57.01-1
- Initial release for Fedora Copr
