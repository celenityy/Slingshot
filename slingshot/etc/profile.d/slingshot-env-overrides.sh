#!/bin/sh
#Copyright (c) 2020 Divested Computing Group
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

#misc
export CRYFS_NO_UPDATE_CHECK=true;

# zero video RAM to prevent leakage
# see (CC BY-SA 4.0): https://www.adlerweb.info/blog/2012/06/20/nvidia-x-org-video-ram-information-leak
export R600_DEBUG=zerovram;
export AMD_DEBUG=zerovram;
export RADV_DEBUG=zerovram;

# enable gstreamer va-api plugin on unsupported drivers
export GST_VAAPI_ALL_DRIVERS=1;

# disable thread local malloc cache
export GLIBC_TUNABLES='glibc.malloc.tcache_count=0';

# Disable Crash Reporting in Mozilla software (Taken from my Phoenix)
# https://firefox-source-docs.mozilla.org/toolkit/crashreporter/crashreporter/index.html#user-specified-environment-variables
export MOZ_CRASHREPORTER=0;
export MOZ_CRASHREPORTER_DISABLE=1;
export MOZ_CRASHREPORTER_NO_REPORT=1;
export MOZ_CRASHREPORTER_URL="data;";

# Enable Wayland in Mozilla software (Taken from my Phoenix)
# Credit to Rasmus: https://askubuntu.com/users/13884/rasmus
# https://askubuntu.com/questions/1456684/how-to-initialize-firefox-on-wayland-always-by-default
if [ "$XDG_SESSION_TYPE" == "wayland" ]; then
    export MOZ_ENABLE_WAYLAND=1
fi

# enable wayland for electron apps
if [ "$XDG_SESSION_TYPE" == "wayland" ]; then
    export ELECTRON_OZONE_PLATFORM_HINT='auto'
fi

# gpg
export GPG_TTY=$(tty);

# disable JIT in GNOME's JavaScript Engine
# https://gitlab.gnome.org/GNOME/gjs/-/blob/master/doc/Environment.md#javascript-engine
export GJS_DISABLE_JIT=1;

# disable JIT in WebKit
# https://trac.webkit.org/wiki/EnvironmentVariables
export JavaScriptCoreUseJIT=0;
export JSC_useFTLJI=0;

# enforce WebKit's web process sandbox
# https://trac.webkit.org/wiki/EnvironmentVariables
export WEBKIT_FORCE_SANDBOX=1;

# disable telemetry for various programs
# https://consoledonottrack.com/
export DO_NOT_TRACK=1;
export AZURE_CORE_COLLECT_TELEMETRY=0;
export DOTNET_CLI_TELEMETRY_OPTOUT=1;
export GATSBY_TELEMETRY_DISABLED=1;
export HOMEBREW_NO_ANALYTICS=1;
export POWERSHELL_TELEMETRY_OPTOUT=1;
export SAM_CLI_TELEMETRY=0;

# harden homebrew (if installed)
export HOMEBREW_NO_INSECURE_REDIRECT=1;
export HOMEBREW_NO_ENV_HINTS=1;

# set restrictive umask
if [ "$(/usr/bin/id -ru)" -ge 1000 ] && [ "$(/usr/bin/id -u)" -ge 1000 ] && [ "$(/usr/bin/id -gn)" = "$(/usr/bin/id -un)" ]; then
    umask 0077;
else
    umask 0022;
fi;
