%global nvidia_ver 565.57.01
%global gsp_output _out/nvidia

Name:           nouveau-fw-gsp
Version:        %{nvidia_ver}
Release:        1%{?dist}
Summary:        NVIDIA GSP (Turing+) firmware for the latest GSP kernel code

License:        MIT AND NVIDIA
URL:            https://download.nvidia.com/XFree86/Linux-x86_64/%{version}/README/gsp.html
Source0:        https://github.com/NVIDIA/open-gpu-kernel-modules/archive/refs/tags/%{version}.tar.gz
Source1:        https://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}.run

BuildRequires:  git-core
BuildRequires:  python3
BuildArch:      noarch

%description
NVIDIA GSP firmware blobs required for Nouveau driver support on Turing and newer GPUs.

%prep
%autosetup -n open-gpu-kernel-modules-%{version}

%build
rm -rf %{gsp_output} || true
./nouveau/extract-firmware-nouveau.py -s -d %{SOURCE1}

%install
# Install firmware
install -dm755 %{buildroot}%{_prefix}/lib/firmware
cp -a %{gsp_output} %{buildroot}%{_prefix}/lib/firmware/

# Create temp dir for NVIDIA driver extraction
TMPDIR=$(mktemp -d)
cd "$TMPDIR"
sh %{SOURCE1} -x
cd NVIDIA-Linux-x86_64-%{version}

# Install licenses 
cd -
install -Dm644 %{_builddir}/open-gpu-kernel-modules-%{version}/COPYING %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.expat
install -Dm644 "$TMPDIR"/NVIDIA-Linux-x86_64-%{version}/LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.nvidia

rm -rf "$TMPDIR"

%files
%license %{_datadir}/licenses/%{name}/LICENSE.*
%{_prefix}/lib/firmware/nvidia/

%changelog
* Wed Feb 14 2024 Initial Release <aidas957@gmail.com> - 565.57.01-1
- Initial package
