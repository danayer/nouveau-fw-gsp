Name:           nouveau-fw-gsp
Version:        565.57.01
Release:        1%{?dist}
Summary:        Nouveau GSP firmware

License:        MIT
URL:            https://www.nvidia.com
Source0:        https://download.nvidia.com/XFree86/Linux-x86_64/565.57.01/NVIDIA-Linux-x86_64-565.57.01.run

BuildArch:      noarch

%description
Nouveau firmware for GSP support.

%prep
set -x
mkdir -p nvidia_extracted
sh %{SOURCE0} --extract-only --target ./nvidia_extracted

%build
# Если нужно добавить шаги сборки

%install
mkdir -p %{buildroot}/usr/lib/firmware/nouveau
cp -a ./nvidia_extracted/* %{buildroot}/usr/lib/firmware/nouveau

%files
/usr/lib/firmware/nouveau

%changelog
* Fri Jan 17 2025 Danayer <Danayerofficial@yandex.ru> - 565.57.01-1
- Initial release for Fedora Copr
