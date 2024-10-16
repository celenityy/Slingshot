Slingshot
=====

Overview
--------
Slingshot is a configuration utility for GNU/Linux Systems with an emphasis on improving privacy, security, & freedom - as well as performance, & usability where possible. It is based on the excellent [Brace](https://codeberg.org/divested/brace) project, but with additions from TommmyTran732's [Linux-Setup-Scripts](https://github.com/TommyTran732/Linux-Setup-Scripts), as well as my own personal tweaks & changes.

Compatibility
-------------
- Arch Linux
- CentOS 9/Stream
- Debian 12
- Fedora 39/40 (preferred)
- openSUSE Tumbleweed

License
-------
AGPL-3.0-or-later where applicable

Prebuilts
---------
- Fedora via COPR: (N/A)
- Fedora via CI: (N/A)
- Arch via CI: (N/A)
- Debian via CI: (N/A)

Building
--------
- git clone [THIS REPO]
- Arch Linux: makepkg
- CentOS: rpmbuild -ba slingshot.spec
- Debian: dpkg-deb --root-owner-group --build slingshot
- Fedora: rpmbuild -ba slingshot.spec

Features
--------

**NOTE:** This list is **not** comprehensive. It is simply a list of notable features & enhancements, but there are many more not documented here!

* Hardens the Linux kernel through various [sysctl settings](slingshot/usr/lib/sysctl.d/60-restrict.conf) & [boot parameters](slingshot/etc/default/grub.d/brace.cfg)
* Installs & configures [hardened_malloc](https://github.com/GrapheneOS/hardened_malloc) for protection against heap corruption vulnerabilities & for reducing the lifetime of sensitive data in memory.
* Switches Flathub from acting on the system level to the user level, allowing for easier control & enhanced privacy.
* Installs [Flatseal](https://github.com/tchx84/Flatseal) & [significantly hardens default Flatpak permissions](slingshot/usr/bin/slingshot#L174) to provide app sandboxing.
* Installs & configures [Firejail](https://github.com/netblue30/firejail) to provide sandboxing for Web browsers, Electron apps, & apps unavailable as Flatpaks.
* Installs [ClamAV](https://github.com/Cisco-Talos/clamav) for protection against malicious software.
* Gives the option to easily replace built-in system apps with the Flatpak variants, for an improvement in privacy & security via Flatpak's sandboxing, & quicker updates.
* Installs [real-ucode](https://github.com/divestedcg/real-ucode) to install latest CPU microcodes to improve security & include the latest fixes.
* Automatically installs & configures the [RPM Fusion Free](https://rpmfusion.org/FAQ#Free_repository), [RPM Fusion Free - Tainted](https://rpmfusion.org/FAQ#Free_Tainted), [RPM Fusion Nonfree](https://rpmfusion.org/FAQ#Nonfree_repository), [RPM Fusion Nonfree - Tainted](https://rpmfusion.org/FAQ#Nonfree_Tainted), & [divested-release](https://gitlab.com/divested/divested-release) software repositories.
* Enforces that DNF repos use HTTPS.
* Disables DNF [Countme](https://dnf.readthedocs.io/en/latest/conf_ref.html#countme-label).
* Increases DNF's max parallel downloads to heavily improve performance.
* Enforces that FWUPD uses HTTPS.
* Sets Firewalld to prevent incoming connections.
* Enables [Firewalld Lockdown](https://fedoraproject.org/wiki/Features/FirewalldLockdown) to prevent apps from editing the firewall configuration.
* Installs firewall-config to allow easily modifying Firewalld through a GUI.
* Hardens [crypto policies](https://jfearn.fedorapeople.org/fdocs/en-US/Fedora/20/html/Security_Guide/Security_Guide-Encryption-CryptoPolicy.html).
* Disables [null/empty passwords](https://networklogician.com/2021/04/11/disable-null-passwords/)
* Sets the device hostname to `localhost` & prevents broadcasting it.
* Automatically installs codecs for media playback
* Sets a generic [Machine ID](https://www.man7.org/linux/man-pages/man5/machine-id.5.html)

GNOME specific:

* Disables system animations by default to improve performance & snappiness
* Enables minimize & maximize buttons by default
* Disables automounting & auto-running media
* Disables lockscreen notifications
* Disables File & App History
* Disables Problem Reporting
* Disables Camera & Microphone by default
* Disables Location Services
* Automatically deletes trash & temporary files
* Disables Remote Desktop & Remote Access functionality
* Disables external Search Providers
* Enables the "delete permanently" option for Nautilus (GNOME Files)

Contents
--------

- /etc/apt/apt.conf.d/90-brace					= apt: enable seccomp filter during package install
- /etc/dconf/db/local.d/00-brace-*				= GNOME/Cinnamon/MATE: change default settings
- /etc/dconf/profile/user					= Fixup dconf overrides on select distros
- /etc/profile.d/brace-env-overrides.sh				= profile: sets some environment overrides (eg. umask)
- /etc/profile.d/brace-helpers.sh				= profile: adds helper aliases (eg. cleaning functions)
- /etc/tlp.d/00-brace.conf					= TLP: allow for better power savings on AC too
- /usr/lib/modprobe.d/brace.conf				= kernel: disable/block unsafe modules
- /usr/lib/modprobe.d/wireless-perf.conf			= kernel: increase Wi-Fi performance for b43 and iwlwifi
- /usr/lib/NetworkManager/conf.d/30-nm-privacy.conf		= NetworkManager: enables MAC randomization and IPv6 privacy extensions and disables connectivity checks
- /usr/lib/sysctl.d/60-restrict.conf				= sysctl: set more restrictive defaults (dmesg, ptrace)
- /usr/lib/systemd/system/*.service.d/99-brace.conf		= systemd service unit sandboxing
- /usr/lib/systemd/user/restic-backup@.*			= systemd user unit for restic backups
- /usr/lib/tmpfiles.d/99-brace-proc.conf			= /proc: harden permissions
- /usr/lib/tmpfiles.d/99-slingshot-sys.conf				= /sys: harden permissions
- /usr/bin/brace-supplemental-changes				= change extra default settings
- /usr/sbin/brace-enable-auto-updates				= Fedora: automatic system updates using dnf-plugin-system-upgrade
- /usr/sbin/slingshot-android                   = Fedora: Automatically install & configure tools used for Android debugging
- /usr/sbin/slingshot-brave                     = Fedora: Automatically install & configure the Brave browser
- /usr/sbin/slingshot-fedora-repos				= Fedora: Automatically install & configure RPM Fusion Free & Nonfree, Divested RPM, & Flathub
- /usr/sbin/brace-update-system					= Fedora: helper to update to the next release
- /usr/sbin/slingshot-installer					= unified recommended package installer (TODO)
- /usr/sbin/brace-rpm-verify					= RPM: verifies installed packages for corruption

Known Issues
------------
- A reboot is required on openSUSE after install for dconf changes to take effect.
- Compatibility is best with Fedora, and that is the primary test-bed.

Credits
-------
- Brace
	- Divested Computing Group
	- AGPLv3: https://codeberg.org/divested/brace/src/branch/master/LICENSE
	- https://codeberg.org/divested/brace
	- Donate: https://divested.dev/donate
- userjs-arkenfox.js
	- @thorin-oakenpants + @earthlng + @claustromaniac
	- MIT: https://github.com/arkenfox/user.js/blob/af516315971b7c94075db1e317bee5b12dc3b781/LICENSE.txt
	- https://github.com/arkenfox/user.js
- 99-brace-proc.conf and 99-brace-sys.conf
	- Topi Miettinen (@topimiettinen)
	- GPL-2.0+: https://salsa.debian.org/corsac/hardening-runtime/-/blob/1a315536726cf41b64af6dc65c7cf9b250b5dda1/debian/copyright
	- https://salsa.debian.org/corsac/hardening-runtime/-/commit/1a315536726cf41b64af6dc65c7cf9b250b5dda1
- brace-rpm-verify
	- @doktor5000
	- CC BY-SA 3.0: https://stackoverflow.com/help/licensing
	- https://unix.stackexchange.com/a/217024
- firewalld IPv6 drop zone fix
	- Mark
	- CC BY-SA 3.0: https://stackoverflow.com/help/licensing
	- https://serverfault.com/a/775153
- restic-backup.service
	- Link Dupont
	- CC BY-SA 3.0: https://fedoramagazine.org/terms-and-conditions/
	- https://fedoramagazine.org/automate-backups-with-restic-and-systemd/
- chrony.brace.conf
	- GrapheneOS
	- MIT: https://github.com/GrapheneOS/infrastructure/blob/main/LICENSE
	- https://github.com/GrapheneOS/infrastructure/blob/main/chrony.conf
	- Donate: https://grapheneos.org/donate
- modprobe.d/brace.conf additional module blocking
	- @madaidan
	- List likely uncopyrightable
	- https://madaidans-insecurities.github.io/guides/linux-hardening.html#kasr-kernel-modules
	- Donate: https://madaidans-insecurities.github.io
