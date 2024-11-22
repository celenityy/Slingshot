# Maintainer: celenity
pkgname=Slingshot
pkgver=20241122
pkgrel=1
pkgdesc="At last, the ultimate Linux set-up!"
arch=('any')
license=('GPL3')
install=slingshot.install

build() {
	cp -r ../slingshot/ "$srcdir"/;
	cp ../README.md "$srcdir"/;
}

package() {
	install -Dm644 slingshot/etc/chrony.brace.conf "$pkgdir"/etc/chrony.brace.conf;
	install -Dm644 slingshot/etc/dconf/db/local.d/00-brace-cinnamon "$pkgdir"/etc/dconf/db/local.d/00-brace-cinnamon;
	install -Dm644 slingshot/etc/dconf/db/local.d/00-brace-extra "$pkgdir"/etc/dconf/db/local.d/00-brace-extra;
	install -Dm644 slingshot/etc/dconf/db/local.d/00-slingshot-gnome "$pkgdir"/etc/dconf/db/local.d/00-slingshot-gnome;
	install -Dm644 slingshot/etc/dconf/db/local.d/00-brace-mate "$pkgdir"/etc/dconf/db/local.d/00-brace-mate;
	install -Dm644 slingshot/etc/dconf/db/local.d/00-brace-pantheon "$pkgdir"/etc/dconf/db/local.d/00-brace-pantheon;
	mkdir -p "$pkgdir"/etc/dconf/db/local.d/locks;
	install -Dm644 slingshot/etc/dconf/db/local.d/locks/automount-disable "$pkgdir"/etc/dconf/db/local.d/locks/automount-disable;
	install -Dm644 slingshot/etc/dconf/db/local.d/locks/privacy "$pkgdir"/etc/dconf/db/local.d/locks/privacy;
	install -Dm644 slingshot/etc/dconf/profile/user "$pkgdir"/etc/dconf/profile/user;
	install -Dm755 slingshot/etc/default/grub.d/brace.cfg "$pkgdir"/etc/default/grub.d/brace.cfg;
	install -Dm644 slingshot/etc/profile.d/slingshot-env-overrides.sh "$pkgdir"/etc/profile.d/slingshot-env-overrides.sh;
	install -Dm644 slingshot/etc/profile.d/slingshot-helpers.sh "$pkgdir"/etc/profile.d/slingshot-helpers.sh;
	install -Dm644 slingshot/etc/security/limits.d/30-disable-coredump.conf "$pkgdir"/etc/security/limits.d/30-disable-coredump.conf;
	install -Dm644 slingshot/etc/ssh/ssh_config.d/10-custom.conf "$pkgdir"/etc/ssh/ssh_config.d/10-custom.conf;
	mkdir -p "$pkgdir"/etc/systemd/coredump.conf.d;
	install -Dm644 slingshot/etc/systemd/coredump.conf.d/disable.conf "$pkgdir"/etc/systemd/coredump.conf.d/disable.conf;
	install -Dm644 slingshot/etc/tlp.d/00-brace.conf "$pkgdir"/etc/tlp.d/00-brace.conf;
	install -Dm644 slingshot/usr/lib/modprobe.d/slingshot.conf "$pkgdir"/usr/lib/modprobe.d/slingshot.conf;
	install -Dm644 slingshot/usr/lib/modprobe.d/wireless-perf.conf "$pkgdir"/usr/lib/modprobe.d/wireless-perf.conf;
	install -Dm644 slingshot/usr/lib/NetworkManager/conf.d/30-nm-privacy.conf "$pkgdir"/usr/lib/NetworkManager/conf.d/30-nm-privacy.conf;
	install -Dm644 slingshot/usr/lib/NetworkManager/conf.d/01-transient-hostname.conf "$pkgdir"/usr/lib/NetworkManager/conf.d/01-transient-hostname.conf;
	install -Dm644 slingshot/usr/lib/sysctl.d/60-restrict.conf "$pkgdir"/usr/lib/sysctl.d/60-restrict.conf;
	install -Dm644 slingshot/usr/lib/systemd/resolved.conf.d/brace.conf "$pkgdir"/usr/lib/systemd/resolved.conf.d/brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/chronyd.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/chronyd.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/ejabberd.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/ejabberd.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/httpd.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/httpd.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/irqbalance.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/irqbalance.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/minetest@.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/minetest@.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/ModemManager.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/ModemManager.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/murmur.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/murmur.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/NetworkManager.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/NetworkManager.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/php-fpm.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/php-fpm.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/radiusd.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/radiusd.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/rngd.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/rngd.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/tor.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/tor.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/systemd/system/wpa_supplicant.service.d/99-brace.conf "$pkgdir"/usr/lib/systemd/system/wpa_supplicant.service.d/99-brace.conf;
	install -Dm644 slingshot/usr/lib/tmpfiles.d/99-brace-proc.conf "$pkgdir"/usr/lib/tmpfiles.d/99-brace-proc.conf;
	install -Dm644 slingshot/usr/lib/tmpfiles.d/99-slingshot-sys.conf "$pkgdir"/usr/lib/tmpfiles.d/99-slingshot-sys.conf;
	install -Dm644 slingshot/usr/lib/udev/rules.d/10-trim.rules "$pkgdir"/usr/lib/udev/rules.d/10-trim.rules;
	install -Dm644 slingshot/usr/lib/udev/rules.d/50-usb-realtek-net-exceprt.rules "$pkgdir"/usr/lib/udev/rules.d/50-usb-realtek-net-exceprt.rules;
	install -Dm644 slingshot/usr/lib/udev/rules.d/51-android.rules "$pkgdir"/usr/lib/udev/rules.d/51-android.rules;
	install -Dm644 slingshot/usr/lib/systemd/user/restic-backup@.service "$pkgdir"/usr/lib/systemd/user/restic-backup@.service;
	install -Dm644 slingshot/usr/lib/systemd/user/restic-backup@.timer "$pkgdir"/usr/lib/systemd/user/restic-backup@.timer;
	install -Dm755 slingshot/usr/bin/slingshot "$pkgdir"/usr/bin/slingshot;
	install -Dm755 slingshot/usr/bin/slingshot-auto "$pkgdir"/usr/bin/slingshot-auto;
	install -Dm755 slingshot/usr/sbin/brace-rpm-verify "$pkgdir"/usr/bin/brace-rpm-verify;
	install -Dm755 slingshot/usr/sbin/slingshot-install "$pkgdir"/usr/bin/slingshot-install;
	install -Dm755 slingshot/usr/sbin/slingshot-install-auto "$pkgdir"/usr/bin/slingshot-install-auto;
	mkdir -p "$pkgdir"/usr/share/doc/slingshot;
	install -Dm644 README.md "$pkgdir"/usr/share/doc/slingshot/README.md;
}
