Name: slingshot
Version: 20241109
Release: 1
Summary: Create the ultimate Linux set-up.
License: AGPLv3+
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%define _binary_payload w3T.xzdio
%define _sourcedir %(echo $PWD)
%define _rpmdir %(echo $PWD/build)

%description
Welcome to the real world.

%post
if [ -f /usr/bin/dconf ]; then dconf update; fi;
echo "Please pepper your /etc/fstab like so:";
echo "- / can have discard,noatime";
echo "- /boot can have discard,noatime,nodev,nosuid,noexec";
echo "- /boot/efi can have discard,noatime,nodev,nosuid,noexec";
echo "- /home can have discard,noatime,nodev,nosuid";

%postun
if [ -f /usr/bin/dconf ]; then dconf update; fi;

%install
install -Dm644 %{_sourcedir}/slingshot/etc/chrony.slingshot.conf %{buildroot}/etc/chrony.slingshot.conf;
install -Dm644 %{_sourcedir}/slingshot/etc/dconf/db/local.d/00-brace-cinnamon %{buildroot}/etc/dconf/db/local.d/00-brace-cinnamon;
install -Dm644 %{_sourcedir}/slingshot/etc/dconf/db/local.d/00-brace-extra %{buildroot}/etc/dconf/db/local.d/00-brace-extra;
install -Dm644 %{_sourcedir}/slingshot/etc/dconf/db/local.d/00-slingshot-gnome %{buildroot}/etc/dconf/db/local.d/00-slingshot-gnome;
install -Dm644 %{_sourcedir}/slingshot/etc/dconf/db/local.d/00-brace-mate %{buildroot}/etc/dconf/db/local.d/00-brace-mate;
install -Dm644 %{_sourcedir}/slingshot/etc/dconf/db/local.d/00-brace-pantheon %{buildroot}/etc/dconf/db/local.d/00-brace-pantheon;
mkdir -p %{buildroot}/etc/dconf/db/local.d/locks;
install -Dm644 %{_sourcedir}/slingshot/etc/dconf/db/local.d/locks/automount-disable %{buildroot}/etc/dconf/db/local.d/locks/automount-disable;
install -Dm644 %{_sourcedir}/slingshot/etc/dconf/db/local.d/locks/privacy %{buildroot}/etc/dconf/db/local.d/locks/privacy;
install -Dm644 %{_sourcedir}/slingshot/etc/dconf/profile/user-full %{buildroot}/etc/dconf/profile/user;
install -Dm644 %{_sourcedir}/slingshot/etc/machine-id %{buildroot}/etc/machine-id;
install -Dm644 %{_sourcedir}/slingshot/etc/profile.d/slingshot-env-overrides.sh %{buildroot}/etc/profile.d/slingshot-env-overrides.sh;
install -Dm644 %{_sourcedir}/slingshot/etc/profile.d/slingshot-helpers.sh %{buildroot}/etc/profile.d/slingshot-helpers.sh;
install -Dm644 %{_sourcedir}/slingshot/etc/security/limits.d/30-disable-coredump.conf %{buildroot}/etc/security/limits.d/30-disable-coredump.conf;
install -Dm644 %{_sourcedir}/slingshot/etc/ssh/ssh_config.d/10-custom.conf %{buildroot}/etc/ssh/ssh_config.d/10-custom.conf;
mkdir -p %{buildroot}/etc/systemd/coredump.conf.d;
install -Dm644 %{_sourcedir}/slingshot/etc/systemd/coredump.conf.d/disable.conf %{buildroot}/etc/systemd/coredump.conf.d/disable.conf;
install -Dm644 %{_sourcedir}/slingshot/etc/tlp.d/00-brace.conf %{buildroot}/etc/tlp.d/00-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/modprobe.d/slingshot.conf %{buildroot}/usr/lib/modprobe.d/slingshot.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/modprobe.d/wireless-perf.conf %{buildroot}/usr/lib/modprobe.d/wireless-perf.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/NetworkManager/conf.d/30-nm-privacy.conf %{buildroot}/usr/lib/NetworkManager/conf.d/30-nm-privacy.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/NetworkManager/conf.d/01-transient-hostname.conf %{buildroot}/usr/lib/NetworkManager/conf.d/01-transient-hostname.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/sysctl.d/60-restrict.conf %{buildroot}/usr/lib/sysctl.d/60-restrict.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/resolved.conf.d/brace.conf %{buildroot}/usr/lib/systemd/resolved.conf.d/brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/chronyd.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/chronyd.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/ejabberd.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/ejabberd.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/httpd.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/httpd.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/irqbalance.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/irqbalance.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/minetest@.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/minetest@.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/ModemManager.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/ModemManager.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/murmur.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/murmur.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/NetworkManager.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/NetworkManager.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/php-fpm.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/php-fpm.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/radiusd.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/radiusd.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/rngd.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/rngd.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/tor.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/tor.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/system/wpa_supplicant.service.d/99-brace.conf %{buildroot}/usr/lib/systemd/system/wpa_supplicant.service.d/99-brace.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/user/restic-backup@.service %{buildroot}/usr/lib/systemd/user/restic-backup@.service;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/systemd/user/restic-backup@.timer %{buildroot}/usr/lib/systemd/user/restic-backup@.timer;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/tmpfiles.d/99-brace-proc.conf %{buildroot}/usr/lib/tmpfiles.d/99-brace-proc.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/tmpfiles.d/99-slingshot-sys.conf %{buildroot}/usr/lib/tmpfiles.d/99-slingshot-sys.conf;
install -Dm644 %{_sourcedir}/slingshot/usr/lib/udev/rules.d/50-usb-realtek-net-exceprt.rules %{buildroot}/usr/lib/udev/rules.d/50-usb-realtek-net-exceprt.rules;
install -Dm755 %{_sourcedir}/slingshot/usr/bin/slingshot %{buildroot}/usr/bin/slingshot;
install -Dm755 %{_sourcedir}/slingshot/usr/sbin/brace-audit %{buildroot}/usr/sbin/brace-audit;
install -Dm755 %{_sourcedir}/slingshot/usr/sbin/brace-fedora-enable-auto-updates %{buildroot}/usr/sbin/brace-enable-auto-updates;
install -Dm755 %{_sourcedir}/slingshot/usr/sbin/brace-fedora-enable-fapolicyd %{buildroot}/usr/sbin/brace-enable-fapolicyd;
install -Dm755 %{_sourcedir}/slingshot/usr/sbin/slingshot-fedora-repos %{buildroot}/usr/sbin/slingshot-fedora-repos;
install -Dm755 %{_sourcedir}/slingshot/usr/sbin/slingshot-android %{buildroot}/usr/sbin/slingshot-android;
install -Dm755 %{_sourcedir}/slingshot/usr/sbin/slingshot-brave %{buildroot}/usr/sbin/slingshot-brave;
install -Dm755 %{_sourcedir}/slingshot/usr/sbin/brace-fedora-update-system %{buildroot}/usr/sbin/brace-update-system;
install -Dm755 %{_sourcedir}/slingshot/usr/sbin/slingshot-installer %{buildroot}/usr/sbin/slingshot-installer;
install -Dm755 %{_sourcedir}/slingshot/usr/sbin/brace-rpm-verify %{buildroot}/usr/sbin/brace-rpm-verify;
mkdir -p %{buildroot}/usr/share/doc/slingshot;
install -Dm644 %{_sourcedir}/README.md %{buildroot}/usr/share/doc/slingshot/README.md;

%files
/etc/chrony.slingshot.conf
/etc/dconf/db/local.d/00-brace-cinnamon
/etc/dconf/db/local.d/00-brace-extra
/etc/dconf/db/local.d/00-slingshot-gnome
/etc/dconf/db/local.d/00-brace-mate
/etc/dconf/db/local.d/00-brace-pantheon
/etc/dconf/db/local.d/locks/automount-disable
/etc/dconf/db/local.d/locks/privacy
/etc/dconf/profile/user
/etc/machine-id
/etc/profile.d/slingshot-env-overrides.sh
/etc/profile.d/slingshot-helpers.sh
/etc/security/limits.d/30-disable-coredump.conf
/etc/ssh/ssh_config.d/10-custom.conf
/etc/systemd/coredump.conf.d/disable.conf
/etc/tlp.d/00-brace.conf
/usr/lib/modprobe.d/slingshot.conf
/usr/lib/modprobe.d/wireless-perf.conf
/usr/lib/NetworkManager/conf.d/01-transient-hostname.conf
/usr/lib/NetworkManager/conf.d/30-nm-privacy.conf
/usr/lib/sysctl.d/60-restrict.conf
/usr/lib/systemd/resolved.conf.d/brace.conf
/usr/lib/systemd/system/chronyd.service.d/99-brace.conf
/usr/lib/systemd/system/ejabberd.service.d/99-brace.conf
/usr/lib/systemd/system/httpd.service.d/99-brace.conf
/usr/lib/systemd/system/irqbalance.service.d/99-brace.conf
/usr/lib/systemd/system/minetest@.service.d/99-brace.conf
/usr/lib/systemd/system/ModemManager.service.d/99-brace.conf
/usr/lib/systemd/system/murmur.service.d/99-brace.conf
/usr/lib/systemd/system/NetworkManager.service.d/99-brace.conf
/usr/lib/systemd/system/php-fpm.service.d/99-brace.conf
/usr/lib/systemd/system/radiusd.service.d/99-brace.conf
/usr/lib/systemd/system/rngd.service.d/99-brace.conf
/usr/lib/systemd/system/tor.service.d/99-brace.conf
/usr/lib/systemd/system/wpa_supplicant.service.d/99-brace.conf
/usr/lib/systemd/user/restic-backup@.service
/usr/lib/systemd/user/restic-backup@.timer
/usr/lib/tmpfiles.d/99-brace-proc.conf
/usr/lib/tmpfiles.d/99-slingshot-sys.conf
/usr/lib/udev/rules.d/50-usb-realtek-net-exceprt.rules
/usr/bin/slingshot
/usr/sbin/brace-audit
/usr/sbin/brace-enable-auto-updates
/usr/sbin/brace-enable-fapolicyd
/usr/sbin/slingshot-fedora-repos
/usr/sbin/slingshot-android
/usr/sbin/slingshot-brave
/usr/sbin/brace-update-system
/usr/sbin/slingshot-installer
/usr/sbin/brace-rpm-verify
/usr/share/doc/slingshot/README.md
